import re

def extract_emails(text):
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    matches = re.findall(pattern, text)
    return matches

def extract_phones(text):
    pattern = r'\+?\d{1,3}[\s\-.]?\d{2,4}[\s\-.]?\d{2,4}[\s\-.]?\d{2,6}'
    matches = re.findall(pattern, text)
    return matches




with open("reviews.txt", 'r', encoding='utf-8') as f:
    content = f.read()

emails = extract_emails(content)
phones = extract_phones(content)

with open("emails.txt", 'w', encoding='utf-8') as f:
    for email in emails:
        f.write(email + '\n')

with open("phone_numbers.txt", 'w', encoding='utf-8') as f:
    for phone in phones:
        f.write(phone + '\n')
