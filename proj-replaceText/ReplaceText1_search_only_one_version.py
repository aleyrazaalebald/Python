MyLists = []

#prepare a list with "FileName", "Text To Be Searched" and "Text To Be Replaced"
MyLists.append(["properties.txt", 
                "RIZVI",
                "ZAIDI"])

for x in MyLists:
	print("x[0]", x[0]) # file name
	print("x[1]", x[1]) # existing text 
	print("x[2]", x[2]) # new text

	current_file  = x[0]  # properties.txt

	# load file in read mode and read complete data from the file	
	with open(current_file, "r") as file:
		data = file.read()
		print("data read:", data)

		# using string replace method an replace old text with new text
		modified_data = data.replace(x[1], x[2])

	# load file in write mode and write modified data in to the file.
	with open(current_file, "w") as file:
		print("data to be writte: ", modified_data)
		file.write(modified_data)
		print("modified " + current_file)

	# program end


