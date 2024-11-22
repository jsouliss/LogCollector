import pandas as pd

def main():
    # Read the JSON file and store it in a DataFrame
    data = pd.read_json('../DataSets/threatEvents.json')

    # Flatten any nested columns (example: agent, host)
    agent_data = pd.json_normalize(data['agent'])
    host_data = pd.json_normalize(data['host'])
    winlog_data = pd.json_normalize(data['winlog'])
    log_data = pd.json_normalize(data['log'])
    ecs_data = pd.json_normalize(data['ecs'])
    event_data = pd.json_normalize(data['event'])
    related_data = pd.json_normalize(data['related'])
    user_data = pd.json_normalize(data['user'])
    process_data = pd.json_normalize(data['process'])
    source_data = pd.json_normalize(data['source'])
    powershell_data = pd.json_normalize(data['powershell'])
    group_data = pd.json_normalize(data['group'])
    file_data = pd.json_normalize(data['file'])
    service_data = pd.json_normalize(data['service'])

    # Print the first few rows of the DataFrame
    print(agent_data.head())
    print(host_data.head())
    print(winlog_data.head())
    print(log_data.head())
    print(ecs_data.head())
    print(event_data.head())
    print(related_data.head())
    print(user_data.head())
    print(process_data.head())
    print(source_data.head())
    print(powershell_data.head())
    print(group_data.head())
    print(file_data.head())
    print(service_data.head())

    # Defining a threshold for the number of NaN values in a column
    threshold = 0.9 # Drop columns with more than 90% NaN values
    data = data.dropna(axis=1, thresh=int((1- threshold) * data.shape[0]))

    # Handle the remaining missing data
    # Fill missing values with a placeholder (like None or Unknown)
    columns_to_fill = ['agent', 'host', 'winlog', 'log', 'ecs', 'event', 'related', 'user', 'process', 'source', 'powershell', 'group', 'file', 'service']
    for col in columns_to_fill:
        if col in data:
            data[col].fillna('Unknown')

    data['@timestamp'] = pd.to_datetime(data['@timestamp'])
    data.to_json('cleanedThreatEvents.json', orient='records', lines=True)

    # Clean the messages
    # newlines and tabs can complicate parsing and training
    data['message'] = data['message'].str.replace('\n', ' ').str.replace('\t', ' ')
    # Drop duplicate messages
    data = data.drop_duplicates(subset=['message'])

    print(data['message'].iloc[0])
    print(data['message'].iloc[1])
    print(data['message'].iloc[2])

    # After performing the above steps, we inspect the cleaned data
    print("\n\nCLEANED DATA: ")
    print(data.isna().sum())
    print(data.info())

    print(f"\n\nNumber of rows {len(data)}")

if __name__ == '__main__':
    main()