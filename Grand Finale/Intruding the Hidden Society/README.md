# Intruding the Hidden Society - CTF Challenge Writeup

Challenge: Intruding the Hidden Society
Points: 200
Category: None (Category information is not provided)

## Objective
The objective of the "Intruding the Hidden Society" challenge is to extract hidden information from the provided pcap file and uncover the flag.

## Solution
To solve the "Intruding the Hidden Society" challenge, I followed these steps:

1. **Identified Patterns in DNS Packets**:
   - Upon analyzing the pcap file, I noticed that a significant portion of the packets were DNS (Domain Name System) packets.
   - I started by filtering and analyzing these DNS packets.

2. **Pattern Identification**:
   - Pay attention to the DNS packets with base64-like encodings.
   - These packets had accompanying numbers, indicating an order for reconstruction.

3. **Packet Extraction**:
   - The goal was to extract and reconstruct the base64-like encoded data. However, with more than 10,000 packets, manual extraction would be impractical.
   - I used the "tshark" command-line tool to extract relevant packets. The following query is an example of how I extracted packets related to the challenge:
     ```
     tshark -nr hiddensociety.pcap -Y '(ip.dst == 8.8.8.8) && (dns.qry.name contains "challange.petronasgraduate.ctfd.io")' > output.txt
     ```
   - The output of the query was saved in the "output.txt" file.

4. **Data Extraction and Reconstruction**:
   - I created a Python script to process the "output.txt" file and extract the base64-like encoded data.
   - The extracted data was reconstructed and written into a separate file.
```python
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
```

5. **Identified the Data Type**:
   - Using the `file` command to determine the type of data contained in the reconstructed file.

6. **Flag Retrieval**:
   - The reconstructed base64 is an image file.
   - Open and view the image

By following these steps, I was able to successfully uncover the hidden flag within the pcap file and complete the "Intruding the Hidden Society" challenge.

## Flag
The flag for this challenge is in the format: `petgrad2023{XXXXXXXXXX}`.

In the "Intruding the Hidden Society" challenge, my goal was to decode and reconstruct base64-like encoded data found in DNS packets within a pcap file and reveal the flag concealed within the data.
