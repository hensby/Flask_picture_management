import csv

import app

if __name__ == '__main__':

    with open('data/people.csv', encoding='utf8') as r:
        d = csv.reader(r, delimiter=',', skipinitialspace=True)
        all_data_dict = {}
        for k, line in enumerate(d):
            if k == 0:
                continue
            all_data_dict[str(k)] = line


    app.addCSV()