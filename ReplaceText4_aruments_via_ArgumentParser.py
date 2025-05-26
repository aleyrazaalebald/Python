# to run this program please pass following command with 4 arguments:
# python3 ReplaceText3_all_var_with_string_passed_as_arg.py properties.txt rizvi zaidi properties_modified.txt

# first Argument  (current file): properties.txt rizvi zaidi properties_modified.txt
# second Argument (text to be searched): rizvi
# third Argurment (new text which should replace existing text): zaidi
# fourth Argument (file name to store modified text): properties_modified.txt

import sys
import argparse

parser = argparse.ArgumentParser("Replace Text Example which requires four arguments.")
parser.add_argument("current_file", default="properties.txt", type=str)
parser.add_argument("existing_text", type=str)
parser.add_argument("modified_text", type=str)
parser.add_argument("modified_file", default="properties_modified.txt", type=str)

#reading all arguments given on command line and map to the argument variable defined above.
args = parser.parse_args()
current_file  = args.current_file
existing_text = args.existing_text
modified_text = args.modified_text
modified_file = args.modified_file

# load file in read mode and read complete data from the file
with open(current_file, "r") as file:
	data = file.read()
	print("data read:", data)

	# using string replace method and replace old text with new text
	modified_data = data.replace(existing_text.upper(), modified_text)

	# search other form of old text (like all small and camel case) and replace them as well with the next text.
	#camel case like Aley
	modified_data = modified_data.replace(existing_text.capitalize(), modified_text)

	# small case like aley
	modified_data = modified_data.replace(existing_text.lower(), modified_text)

# load file in write mode and write modified data in to the file.
with open(modified_file, "w") as file:
	print("------- modified data ------- : ", modified_data)
	file.write(modified_data)
	print("modified " + current_file)

# program end


