import json
def fix_json(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Wrap all lines and add commas between them
    corrected_json = ''.join(lines)

    with open(output_file, 'w') as file:
        file.write(corrected_json)

    print("[+] Corrected JSON written to", output_file)

def main():
    fix_json('../DataSets/threatEvents.json', 'threatEventsFixed.json')

if __name__ == '__main__':
    main()