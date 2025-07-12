"""
📘 Python Practice: Regular Expressions (Regex)
This script includes 10 common regex-based tasks using the 're' module.
Each task is wrapped in a clean function with sample usage.
"""

import re

# 1. ✅ Validate an email address
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

# 2. ✅ Validate a phone number (Pakistani format or general format)
def is_valid_phone(phone):
    pattern = r'^(\+92|0)?3\d{9}$'  # Pakistani mobile format
    return bool(re.match(pattern, phone))

# 3. ✅ Extract all email addresses from a string
def extract_emails(text):
    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    return re.findall(pattern, text)

# 4. ✅ Find all dates in a string (formats: DD/MM/YYYY, DD-MM-YYYY)
def extract_dates(text):
    pattern = r'\b\d{2}[/-]\d{2}[/-]\d{4}\b'
    return re.findall(pattern, text)

# 5. ✅ Replace special characters with space
def replace_special_chars(text):
    return re.sub(r'[^\w\s]', ' ', text)

# 6. ✅ Extract hashtags from a sentence
def extract_hashtags(text):
    return re.findall(r'#\w+', text)

# 7. ✅ Check if string is valid IP address (IPv4)
def is_valid_ip(ip):
    pattern = r'^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$'
    return bool(re.match(pattern, ip))

# 8. ✅ Extract all capitalized words
def extract_capitalized_words(text):
    return re.findall(r'\b[A-Z][a-z]*\b', text)

# 9. ✅ Check password strength using regex
def is_strong_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'
    return bool(re.match(pattern, password))

# 10. ✅ Match all numbers in a paragraph
def extract_numbers(text):
    return re.findall(r'\b\d+\b', text)

# === Example Usage ===
if __name__ == "__main__":
    sample_text = """
    Contact us at support@example.com or admin@domain.org.
    The meeting is on 30/06/2025. Backup date is 01-07-2025.
    Follow us on #Python #Regex. My number is 03001234567.
    My password is StrongP@ss123 and IP is 192.168.1.1.
    """

    print("Valid Email:", is_valid_email("test@email.com"))
    print("Valid Phone:", is_valid_phone("03001234567"))
    print("Extracted Emails:", extract_emails(sample_text))
    print("Extracted Dates:", extract_dates(sample_text))
    print("Cleaned Text:", replace_special_chars(sample_text))
    print("Hashtags:", extract_hashtags(sample_text))
    print("Valid IP:", is_valid_ip("192.168.1.1"))
    print("Capitalized Words:", extract_capitalized_words(sample_text))
    print("Strong Password:", is_strong_password("StrongP@ss123"))
    print("Numbers in Text:", extract_numbers(sample_text))
