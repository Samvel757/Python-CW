import re

emails = ["example@gmail.com", "user@yahoo.com", "admin@outlook.com"] 
domains = [re.search(r"@([a-zA-Z0-9.-]+)", email).group(1) for email in emails]
print(domains)
