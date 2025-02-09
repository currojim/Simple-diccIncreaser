## DiccIncreaser

DiccIncreaser is my first project in the field of cybersecurity. This Python script is designed to generate modified versions of a password dictionary in `.txt` format by making small changes to the words, such as alternating between uppercase and lowercase letters, and adding numbers at the beginning or end of each word.

This project is useful for users learning about brute-force attacks who are not familiar with specialized tools but need larger dictionaries for testing.

# Features:
- Modifies the dictionary words with uppercase and lowercase variations.
- Adds numbers at the beginning and end of each word.
- Generates a new dictionary based on the original with the modifications.

# Usage example:
```bash
python diccIncreaser.py dicc.txt
```
This command will create an output file called dicc2.txt containing the modified versions of the original dictionary.

# Requirements:
- Python 3.x
- Dictionary file in .txt format
