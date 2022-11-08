import json

INPUT_FILE = "../task3/output.csv"


def csv_to_list_dict(file, delimiter=',', new_line='\n') -> str:
    with open(file) as f:
        list_ = []
        lines = f.readlines()
        rows = []
        headers = lines[0].rstrip(new_line).split(delimiter)
        for line in lines[1:]:
            rows.append(line.rstrip(new_line).split(delimiter))
        for row in rows:
            my_dict = {}
            for index, value in enumerate(row):
                my_dict[headers[index]] = value
            list_.append(my_dict)
    return json.dumps(list_, indent=4)


print(csv_to_list_dict(INPUT_FILE))
