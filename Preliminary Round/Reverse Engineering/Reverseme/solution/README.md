# Reverseme - CTF Challenge Writeup

Challenge: Reverseme
Points: 150
Category: Reverse Engineering

## Objective
The objective of the "Reverseme" challenge is to reverse engineer an Android APK file and retrieve the hidden flag. You need to understand how APK files are structured, how strings are stored, and how resources are referenced in Android app development.

## Solution
To successfully complete the "Reverseme" challenge, follow these steps:

1. **Analyze the APK File**:
   - Start by examining the APK file using jadx-gui or a similar tool. You will need to navigate through the app's code to find the flag.

2. **Flag Identification**:
   - During your analysis, you will come across a reference to the flag as `R.string.flag`. This indicates that the flag is retrieved from the app's string resources.
![R.String.Flag](<r string.png>)

3. **Accessing Resources**:
   - In Android app development, the `R.string` is a reference to a string resource defined in the app's resources. An APK file contains all the resources and code needed to run an Android application.
   - When you see `R.string.some_string`, it refers to a string resource defined in the app's `res/values/strings.xml` file.

4. **Strings.xml Examination**:
   - You need to locate the `strings.xml` file within the APK's resources. Navigate to the Resources folder, then to `resources.arsc`, and finally, to `res/values`.
   - Use the search function (`CTRL+F`) to look for the "flag" string. This will allow you to find the flag in plain text.

5. **Flag Retrieval**:
   - By examining the content of the `strings.xml` file, you can retrieve the hidden flag.

6. **Flag Discovery**:
   - As you extract and decipher the flag, you will reveal the complete hidden flag. The flag follows the format: `petgrad2023{XXXXXXXXXX}`.

7. By following these steps, you will successfully reverse engineer the APK and uncover the hidden flag.

## Flag
The flag for this challenge is in the format: `petgrad2023{XXXXXXXXXX}`.

In the "Reverseme" challenge, understanding how Android APK files store resources and references to string resources is crucial. By navigating the app's code and examining the `strings.xml` file, you can retrieve the flag and complete the challenge.
