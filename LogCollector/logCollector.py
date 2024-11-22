import json
from elasticsearch import Elasticsearch

def logo():
    print(
        """
 ██▓     ▒█████   ▄████     ▄████▄  ▒█████   ██▓     ██▓    ▓█████ ▄████▄  ▄▄▄█████▓ ▒█████   ██▀███  
▓██▒    ▒██▒  ██▒██▒ ▀█▒   ▒██▀ ▀█ ▒██▒  ██▒▓██▒    ▓██▒    ▓█   ▀▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒██░    ▒██░  ██▒██░▄▄▄░   ▒▓█    ▄▒██░  ██▒▒██░    ▒██░    ▒███  ▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
▒██░    ▒██   ██░▓█  ██▓   ▒▓▓▄ ▄██▒██   ██░▒██░    ▒██░    ▒▓█  ▄▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░██████▒░ ████▓▒░▒▓███▀▒   ▒ ▓███▀ ░ ████▓▒░░██████▒░██████▒░▒████▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░ ▒░▓  ░░ ▒░▒░▒░ ░▒   ▒    ░ ░▒ ▒  ░ ▒░▒░▒░ ░ ▒░▓  ░░ ▒░▓  ░░░ ▒░ ░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
░ ░ ▒  ░  ░ ▒ ▒░  ░   ░      ░  ▒    ░ ▒ ▒░ ░ ░ ▒  ░░ ░ ▒  ░ ░ ░  ░ ░  ▒       ░      ░ ▒ ▒░   ░▒ ░ ▒░
  ░ ░   ░ ░ ░ ▒ ░ ░   ░    ░       ░ ░ ░ ▒    ░ ░     ░ ░      ░  ░          ░      ░ ░ ░ ▒    ░░   ░ 
    ░  ░    ░ ░       ░    ░ ░         ░ ░      ░  ░    ░  ░   ░  ░ ░                   ░ ░     ░     
                           ░                                      ░                                   
        """
    )

def get_logs(client, index, max_logs, batch_size=1000):
    all_logs = []
    total_retrieved = 0
    # Initialize the scroll
    response = client.search(index=index, scroll='2m', size=batch_size, body={"query": {"match_all": {}}})
    scroll_id = response['_scroll_id']
    hits = response['hits']['hits']

    while True:
        all_logs.extend(hits) # Add the current batch of logs
        total_retrieved += len(hits)
        print(f"[+] Retrieved {total_retrieved} logs, total: {total_retrieved}")

        if total_retrieved >= max_logs:
            break

        # Get the next batch of logs
        response = client.scroll(scroll_id=scroll_id, scroll='2m')
        scroll_id = response['_scroll_id']
        hits = response['hits']['hits']
    client.clear_scroll(scroll_id=scroll_id)
    return all_logs

# This may prolong the execution time if there are a lot of logs
# Not used for now since we save data to a file instead
def print_logs(logs):
    for log in logs:
        print(log['_source'])

def save_logs_to_file(logs, file_path='./logs.json'):
    with open(file_path, 'w') as file:
        json.dump([log["_source"] for log in logs], file, indent=2)

def list_indices(client):
    indices = client.cat.indices(format='json')
    print("[+] Available indices:")
    for idx in indices:
        print(f"- {idx['index']}")

def main():
    logo()
    while True:
        try:
            hosts = input("[i] Enter the host(s) you want to collect logs from: ")
            username = input("[i] Enter the username: ")
            password = input("[i] Enter the password: ")

            client = Elasticsearch(hosts, basic_auth=(username, password))
            print(client.info())
            print("[+] Successfully connected to the Elasticsearch cluster.")
            list_indices(client)
            index = input("[i] Enter the index (or wildcard) you want to collect logs from: ")
            max_logs = int(input("[i] Enter the maximum number of logs you want to retrieve: "))

            logs = get_logs(client, index, max_logs)
            print("[+] Logs collected, storing to file, this may take some time...")
            save_logs_to_file(logs, file_path='./logs.json')
            print("[+] Logs saved to logs.json")
        except Exception as e:
            print(f"[!] Error invalid input: {e}.")
            choice = input("[i] Would you like to continue (y/n): ")
            if choice.lower() == 'n' or choice.lower() == 'no':
                break

if __name__ == '__main__':
    main()