# Unearth the Enigmatic Codebreaker's Challenge - CTF Challenge Writeup

Challenge: Unearth the Enigmatic Codebreaker's Challenge
Points: 150
Category: Memory Forensics

## Objective
The objective of the "Unearth the Enigmatic Codebreaker's Challenge" is to leverage memory forensics skills to crack Jerry's hashed NTLM password. Your task is to find the hashdump, extract Jerry's hashed password, and use a tool like hashcat to crack it and reveal the hidden flag.

## Solution
To successfully complete the "Unearth the Enigmatic Codebreaker's Challenge," follow these steps:

1. **Prerequisite - Complete m3m0irs**:
   - This challenge is the third installment in the memory forensics series. While it is recommended to complete the previous challenges as a prerequisite, it's not necessary to have completed it to proceed, especially since the CTF has ended.

2. **Jerry's Password Hash**:
   - Jerry's password is hashed, and you need to crack it. Hashcat, which didn't work for Dexter's password in the previous challenge, is effective for Jerry's.

3. **Locating the Hashdump**:
   - To find the hashes to be cracked, you first need to locate the hashdump within the memory dump. You can achieve this using the following command: `volatility -f <memory file> --profile=<architecture> hashdump`.

4. **Cracking Jerry's Hashed Password**:
   - After extracting Jerry's hashed NTLM password from the hashdump, use a tool like "hashcat" to crack it. The objective is to reveal the plaintext of Jerry's password.

5. **Flag Discovery**:
   - Once you have successfully cracked Jerry's hashed password, you will discover the flag. It will adhere to the specified format: `petgrad2023{XXXXXXXXXX}`.

6. By following these steps and employing memory forensics techniques, you will uncover Jerry's password and unveil the hidden flag in the "Unearth the Enigmatic Codebreaker's Challenge."

## Flag
The flag for this challenge is in the format: `petgrad2023{XXXXXXXXXX}`.

In this memory forensics challenge, you must use your skills to crack Jerry's hashed NTLM password and reveal the hidden flag. Best of luck!
