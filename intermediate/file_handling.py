"""
📂 Python Practice: File Handling
This script demonstrates basic and intermediate file handling tasks in Python.
Each function handles a common real-world file operation.
"""

import os
import csv

# 1. ✅ Open and read contents of a text file
def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

# 2. ✅ Write user input to a file
def write_input_to_file(filename):
    user_input = input("Enter some text to write into the file: ")
    with open(filename, 'w') as file:
        file.write(user_input)

# 3. ✅ Append data to a file
def append_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

# 4. ✅ Count number of lines in a file
def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file)

# 5. ✅ Count total number of words in a file
def count_words(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    return len(words)

# 6. ✅ Replace a word in a file with another
def replace_word_in_file(filename, old_word, new_word):
    with open(filename, 'r') as file:
        content = file.read()
    content = content.replace(old_word, new_word)
    with open(filename, 'w') as file:
        file.write(content)

# 7. ✅ Copy content from one file to another
def copy_file(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dest:
        dest.write(src.read())

# 8. ✅ Read a file line-by-line and print
def print_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

# 9. ✅ Find the longest word in a file
def longest_word(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    return max(words, key=len) if words else None

# 10. ✅ Read CSV file and print rows
def read_csv_file(csv_filename):
    with open(csv_filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(', '.join(row))

# === Example Usage ===
if __name__ == "__main__":
    sample_txt = "sample.txt"
    sample_copy = "copy.txt"
    csv_file = "sample.csv"

    # Write and Append
    write_input_to_file(sample_txt)
    append_to_file(sample_txt, "This is an appended line.")

    # Read and Process
    print("\nFile Content:")
    print(read_file(sample_txt))

    print("\nLine Count:", count_lines(sample_txt))
    print("Word Count:", count_words(sample_txt))
    print("Longest Word:", longest_word(sample_txt))

    # Replace word
    replace_word_in_file(sample_txt, "appended", "updated")

    # Print updated lines
    print("\nUpdated File Content:")
    print_lines(sample_txt)

    # Copy file
    copy_file(sample_txt, sample_copy)
    print(f"\nContents copied to {sample_copy}")

    # Read CSV file
    print("\nCSV File Content:")
    read_csv_file(csv_file)
