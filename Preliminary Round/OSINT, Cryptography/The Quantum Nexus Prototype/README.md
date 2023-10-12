# The Quantum Nexus Prototype - CTF Challenge Writeup

Challenge: The Quantum Nexus Prototype  
Points: 50  
Category: OSINT, Cryptography  

## Objective
The objective of "The Quantum Nexus Prototype" challenge is to use your OSINT (Open-Source Intelligence) and cryptography skills to uncover hidden information within a provided YouTube link. At first glance, this challenge may seem confusing, but with careful examination of the link and some cryptography, you can successfully extract the flag.

## Solution
To successfully complete "The Quantum Nexus Prototype" challenge, follow these steps:

1. **Opening the YouTube Link**:
   - Click the provided YouTube link. However, keep in mind that vulnerabilities cannot be hidden within a real rickroll video.

2. **URL Examination**:
   - As the video starts to load, take a close look at the link in the URL bar of your web browser. You will notice that the link is shrinking as the video loads.

3. **Character Extraction**:
   - The link shrinking indicates that some characters within the URL are not part of the actual YouTube link and are omitted. Carefully extract these omitted parts.

4. **Base64 Decoding**:
   - The extracted part, which has been omitted from the YouTube link, appears to be encoded using Base64. Decode this part to reveal the hidden flag.

5. By closely examining the link and decoding the extracted information, you will successfully unveil the flag.

## Flag
The flag for this challenge is in the format: `petgrad2023{XXXXXXXXXX}`.

"The Quantum Nexus Prototype" challenge combines OSINT and cryptography skills to uncover the hidden flag within the provided YouTube link. It's a test of your ability to identify unusual elements in URLs and apply cryptographic techniques to decode hidden information. Good luck!
