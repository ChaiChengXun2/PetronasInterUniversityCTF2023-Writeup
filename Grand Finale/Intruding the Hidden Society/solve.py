import base64

base64_reconstructed = ""

with open("output.txt", "r") as file:
	content = file.readlines()

	for line in content: 
		extract_number_and_base64 = line[:-1].split(" ")[-1].replace(".challange.petronasgraduate.ctfd.io", "")

		extract_base64 = extract_number_and_base64.split(".")[1]

		base64_reconstructed += extract_base64

with open("output", "wb") as file: 
	file.write(base64.b64decode(base64_reconstructed))