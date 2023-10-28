# Cryptic Raven - CTF Challenge Writeup

Challenge: Cryptic Raven
Points: 100
Category: Cryptography

## Objective
The objective of the Cryptic Raven challenge is to decrypt a given message, which is encoded using an undisclosed encryption technique. Your task is to decipher the message and reveal the hidden flag.

## Solution
To successfully complete the Cryptic Raven challenge, follow these steps:

1. **Message Deciphering**:
   - Begin by examining the provided message. The challenge does not disclose the specific encryption technique used.
![Encrypted Text](Challenge.png)

2. **Caesar Cipher Brute Force**:
   - Given the lack of information about the encryption method, you can try a brute force approach, specifically the Caesar cipher brute force.
   - The Caesar cipher is a simple and widely used substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

3. **Brute Force Decryption**:
   - Implement a brute force decryption approach by trying all possible shifts within the Caesar cipher.
   - Continue shifting the letters and evaluating the results until you find a meaningful message.

4. **Flag Discovery**:
   - After trying various shift values, you will eventually discover the flag concealed within the decrypted message.

5. By successfully using the Caesar cipher brute force method, you'll unveil the hidden flag.

## Flag
The flag for this challenge is in the format: `petgrad2023{XXXXXXXXXX}`.

In the Cryptic Raven challenge, your cryptography skills are tested as you employ a brute force approach to decipher the message and reveal the flag. Best of luck!
