import json

def convert_jsonl(input_file, output_file):
    with open(input_file, 'r') as infile:
        data = json.load(infile)
        with open(output_file, 'w') as outfile:
            for record in data:
                json.dump(record, outfile)
                outfile.write('\n')

def main():
    convert_jsonl('../DataSets/threatEventsFixed.json', 'threatEvents.jsonl')

if __name__ == '__main__':
    main()