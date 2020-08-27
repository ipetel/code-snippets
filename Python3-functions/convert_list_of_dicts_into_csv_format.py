import csv

def convert_list_of_dicts_into_csv_format(list_of_dicts):
	class Pipe:
		value = ""
		def write(self, text):
			self.value = self.value + text
	
	pipe = Pipe()
	writer = csv.DictWriter(pipe, list_of_dicts[0].keys())
	
	writer.writeheader()
	for entry in list_of_dicts:
		writer.writerow(entry)
	
	return pipe.value
