import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    with open(filename) as f:
        headers = f.readline().rstrip("\n")
        data = f.readlines()
    headers = headers.split(',')
    list_of_values = []
    for row in data:
        list_of_values.append(row.rstrip("\n").split(','))
    list_ = []
    for item in list_of_values:
        dict_ = {}
        for i in range(len(headers)):
            dict_[headers[i]] = item[i]
        list_.append(dict_)
    return list_

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
