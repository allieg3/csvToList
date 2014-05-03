def csvToList:
	with open("csv.csv", "r") as openCsv:
	csvToList = openCsv.read().split("\n")

	for index, item in enumerate(csvToList): 
		csvToList[index] = item.split(",")

	return csvToList
