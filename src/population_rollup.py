import utils
import sys


'''
 This file accepts command line argument. Processes the contents in the input and generates the report in a csv format
 
 Command Line Arguments  
 Input Path : String : Path to the input file
 Output Path : String : Path to which the report has to be written
 
'''
if len(sys.argv) != 3:
    raise ValueError("Please enter input file and output file to be created as arguments")

input_path = sys.argv[1]
output_path = sys.argv[2]

data_dict = utils.read_csv(input_path)
data_dict = dict(sorted(data_dict.items(), key=lambda x: x[0]))
utils.to_csv(data_dict, output_path)