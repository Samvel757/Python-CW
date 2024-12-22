import re

def extract_domains(emails):
    domains = [re.search(r'@([\w.-]+)', email).group(1) for email in emails]
    return domains

emails = ["test@example.com", "user@gmail.com", "info@yandex.ru"]
print(extract_domains(emails))