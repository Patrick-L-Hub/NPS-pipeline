
import json
from scripts.nps_api_scrape import api_scrape

def main():
    data_dict = api_scrape()

    with open('raw_json/nps_json_data.json', 'w') as outfile:
        json.dump(data_dict, outfile, indent = 4)


if __name__ == '__main__':
    main()
