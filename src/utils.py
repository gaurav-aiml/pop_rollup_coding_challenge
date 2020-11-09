import re
def init_new_entry(cbsa_code, data_dict):
    data_dict[cbsa_code] = {}
    data_dict[cbsa_code]["CODE"] = cbsa_code
    data_dict[cbsa_code]["TITLE"] = ""
    data_dict[cbsa_code]["TRACTS"] = set()
    data_dict[cbsa_code]["POP_00"] = 0.0
    data_dict[cbsa_code]["POP_10"] = 0.0


def process_row(row, data_dict):
    cbsa_code = row[7]
    if cbsa_code == "":
        return
    if cbsa_code not in data_dict:
        init_new_entry(cbsa_code, data_dict)
        data_dict[cbsa_code]["TITLE"] = row[8]

    data_dict[cbsa_code]["TRACTS"].add(row[3])
    data_dict[cbsa_code]["POP_00"] += float(row[12])
    data_dict[cbsa_code]["POP_10"] += float(row[14])

def generate_op_string(code, title, tracts, pop00, pop10, per_change):
    return f'{code},{title},{tracts},{pop00},{pop10},{per_change}'

def split_on_comma(line):
    regex = r",(?=(?:[^\"]*\"[^\"]*\")*(?![^\"]*\"))"
    return re.split(regex, line)

def read_csv(input_path):
    data_dict = {}

    with open(input_path) as f:
        _ = f.readline()

        while True:
            row = f.readline().strip()
            if row == "":
                # reached end of file
                break

            row = split_on_comma(row)
            process_row(row, data_dict)

    f.close()

    return data_dict

def to_csv(data_dict, output_path):
    with open(output_path, "x") as f:
        for key, val in data_dict.items():
            title = val["TITLE"]
            tracts = len(val["TRACTS"])
            pop00 = val["POP_00"]
            pop10 = val["POP_10"]
            per_change = round(100 * ((pop10 - pop00) / pop00), 2)

            op = generate_op_string(val['CODE'], title, tracts, pop00, pop10, per_change)
            f.write(op + "\n")

    f.close()
