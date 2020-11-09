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