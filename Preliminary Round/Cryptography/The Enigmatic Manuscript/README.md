# The Enigmatic Manuscript - CTF Challenge Writeup

Challenge: The Enigmatic Manuscript
Points: 50
Category: Cryptography

## Objective
The objective of The Enigmatic Manuscript challenge is to uncover a hidden flag concealed within an image. Your task is to utilize cryptographic techniques to decipher the flag hidden within the image.

## Solution
To successfully complete The Enigmatic Manuscript challenge, follow these steps:

1. **Image Analysis**:
   - Begin by examining the provided image. In this challenge, images often hide clues or messages within their metadata or content.

2. **Exiftool Inspection**:
   - Use the `exiftool` utility to inspect the image's metadata and content for any hidden information.

3. **Base64 Encoding**:
   - Upon using `exiftool` on the image, you may discover a base64 encoded message within the image's metadata or content.

4. **Message Decryption**:
   - Decode the base64 encoded message to reveal the hidden flag.

5. After following these steps and decoding the base64 message, you will successfully uncover the flag concealed within the image.

## Flag
The flag for this challenge is in the format: `petgrad2023{XXXXXXXXXX}`.

In The Enigmatic Manuscript challenge, your cryptography skills come into play as you decode the base64 message hidden within the image to unveil the flag. Best of luck!
