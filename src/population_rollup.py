import utils
import sys

if len(sys.argv != 3):
    raise ValueError("Please enter input file and output file to be created as arguments")

input_path = sys.argv[1]
output_path = sys.argv[2]

