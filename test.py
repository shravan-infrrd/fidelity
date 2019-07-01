file_path = "/Users/shravanc/learning_pyt/fidelity/fidelity_2/working/temp_files/fidelity_2/page-17.txt"

contents = None
with open(file_path) as fp:
		contents = fp.readlines()

for content in contents:
		words = content.split('  ')
		valid_words = list(filter(None, words))
		print(valid_words)
