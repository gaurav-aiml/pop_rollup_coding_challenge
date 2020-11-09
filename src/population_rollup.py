import utils
import sys

if len(sys.argv != 3):
    raise ValueError("Please enter input file and output file to be created as arguments")

input_path = sys.argv[1]
output_path = sys.argv[2]

data_dict = utils.read_csv(input_path)
data_dict = dict(sorted(data_dict.items(), key=lambda x: x[0]))
utils.to_csv(data_dict, output_path)