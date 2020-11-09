import re
def init_new_entry(cbsa_code, data_dict):
    '''
    This function is called when a new CBSA (Core Based Statistical Area) code is found.
    Use this function to add a new entry to the data_dict corresponding to the CBSA code

    :param cbsa_code: String :
    The new CBSA code for which an entry is created

    :param data_dict: Dict :
    The main dictionary which holds all the information about the population roll-up

    :return:None
    '''
    data_dict[cbsa_code] = {}
    data_dict[cbsa_code]["CODE"] = cbsa_code
    data_dict[cbsa_code]["TITLE"] = ""
    data_dict[cbsa_code]["TRACTS"] = set()
    data_dict[cbsa_code]["POP_00"] = 0.0
    data_dict[cbsa_code]["POP_10"] = 0.0


def process_row(row, data_dict):
    '''
    Use this function to convert a list of information into an entry in the data_dict

    :param row : List :
    The list obtained after splitting the line on comma

    :param data_dict: Dict :
    The main dictionary which holds all the information about the population roll-up

    :return: None

    '''
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
    '''
    Function to concat parameters into a csv row.

    :param code: String : The CBSA code
    :param title: String : The CBSA title
    :param tracts: Integer : Number of tracts in the CBSA
    :param pop00: Float : Population in 2000
    :param pop10: Float : Population in 2010
    :param per_change: Float : Percentange change in populationf rom 2000 to 2010

    :return: String :
    A comma seperated row that is to be appended to the csv file
    '''
    return f'{code},{title},{tracts},{pop00},{pop10},{per_change}'

def split_on_comma(line):
    '''
    Function to convert csv row to list

    :param line: String : A String which has to split on comma
    :return: List : List of values resulting after splitting on comma
    '''
    regex = r",(?=(?:[^\"]*\"[^\"]*\")*(?![^\"]*\"))"
    return re.split(regex, line)

def read_csv(input_path):
    '''
    Function to read from a csv file

    :param input_path: String : Path to the input file
    :return: Dict : Dictionary (JSON) representation of each row in csv file
    '''
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
    '''
    Function to write to a csv file
    :param data_dict: Dict : The data dictionary whose contents need to be written to the csv file
    :param output_path: String : The path and filename of the output file. The file should not exist before calling this function
    :return: None
    '''
    with open(output_path, "x") as f:
        for key, val in data_dict.items():
            title = val["TITLE"]
            tracts = len(val["TRACTS"])
            pop00 = val["POP_00"]
            pop10 = val["POP_10"]
            per_change = get_percent_change(pop00, pop10)

            op = generate_op_string(val['CODE'], title, tracts, pop00, pop10, per_change)
            f.write(op + "\n")

    f.close()

def get_percent_change(ele1, ele2):
    '''
    Function to compute percent change from ele1 to ele2, rounded to 2 decimal places
    :param ele1: Float : Initial Value
    :param ele2: Float : Final Value
    :return: Float : Percentage change from Initial Value to Final Value, rounded to 2 decimal places
    '''
    return round(100 * ((ele2 - ele1) / ele1), 2)