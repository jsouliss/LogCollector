import json

def validate_json(input_file):
    with open(input_file, 'r') as file:
        try:
            json.load(file)
            print("[+] JSON is valid")
        except json.JSONDecodeError as e:
            print("[-] JSON is invalid:", e)

def main():
    validate_json('../DataSets/threatEventsFixed.json')

if __name__ == '__main__':
    main()