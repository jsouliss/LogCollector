import pandas as pd
import json

def main():
    data = pd.read_json('../DataSets/cleanedThreatEvents.json')
    print(data.info())


if __name__ == '__main__':
    main()
