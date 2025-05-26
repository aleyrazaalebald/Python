MyLists = []

#prepare a list with "FileName", "Text To Be Searched" and "Text To Be Replaced"
MyLists.append(["properties.txt",
                "RIZVI",
                "ZAIDI",
		"properties_modified.txt"])

for x in MyLists:
	print("x[0]", x[0]) # file name
	print("x[1]", x[1]) # existing text
	print("x[2]", x[2]) # new text
	print("x[3]", x[3]) # modified file name

	current_file  = x[0]  # properties.txt
	modified_file = x[3] # properties_moified.txt

	# load file in read mode and read complete data from the file
	with open(current_file, "r") as file:
		data = file.read()
		print("data read:", data)

		# using string replace method and replace old text with new text
		modified_data = data.replace(x[1].upper(), x[2])

		# search other form of old text (like all small and camel case) and replace them as well with the next text.
		#camel case like Aley
		modified_data = modified_data.replace(x[1].capitalize(), x[2])

		# small case like aley
		modified_data = modified_data.replace(x[1].lower(), x[2])

	# load file in write mode and write modified data in to the file.
	with open(modified_file, "w") as file:
		print("------- modified data ------- : ", modified_data)
		file.write(modified_data)
		print("modified " + current_file)
# program end


