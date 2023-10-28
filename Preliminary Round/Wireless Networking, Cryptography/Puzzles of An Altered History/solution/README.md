# Puzzles of An Altered History - CTF Challenge Writeup

Challenge: Puzzles of An Altered History
Points: 150
Category: Wireless Networking

## Objective
The objective of the "Puzzles of An Altered History" challenge is to crack the password for a given wireless network, which is stored in a provided pcap (packet capture) file. You will need to use a tool called "aircrack-ng" to successfully recover the network's password.

## Solution
To solve the "Puzzles of An Altered History" challenge, follow these steps:

1. **Download and Open the pcap File**:
   - Begin by downloading the provided pcap file, which contains the network traffic data.
   - Open the pcap file using a network analysis tool like Wireshark.

2. **Cracking the Password**:
   - Use the "aircrack-ng" tool to attempt to crack the wireless network's password.
   - The basic command structure for "aircrack-ng" is as follows:
     ```
     aircrack-ng <pcap file> -w <wordlist>
     ```
     - `<pcap file>`: Replace this with the name of the pcap file you are analyzing.
     - `<wordlist>`: Specify the path to a wordlist file that "aircrack-ng" will use to attempt password combinations.

3. **Wordlist Selection**:
   - For the wordlist, you can use a common password dictionary like "rockyou.txt," which is available in various locations. You should specify the full path to the wordlist file.

4. **Run aircrack-ng**:
   - Execute the "aircrack-ng" command in your terminal, providing the pcap file and wordlist as arguments. For example:
     ```
     aircrack-ng ctfwifi.cap -w /usr/share/wordlists/rockyou.txt
     ```

5. **Password Recovery**:
   - "aircrack-ng" will attempt to recover the password by testing combinations from the wordlist.
   - When aircrack-ng successfully finds the correct password, it will display the password in the terminal.

6. **Flag Retrieval**:
   - The cracked password will resemble the format specified in the challenge. Retrieve and present it as the flag to complete the challenge.

By following these steps and using "aircrack-ng," you can successfully crack the password for the wireless network captured in the pcap file and obtain the flag.

## Flag
The flag for this challenge is in the format: `petgrad2023{XXXXXXXXXX}`.

In the "Puzzles of An Altered History" challenge, your goal is to utilize network analysis tools to crack the wireless network's password, revealing the flag upon successful recovery.
