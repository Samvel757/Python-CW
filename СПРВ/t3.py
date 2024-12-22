import re

def split_by_delimiters(string, delimiters):
    regex = '|'.join(map(re.escape, delimiters))
    return re.split(regex, string)

string = "abc,def;ghi jkl"
delimiters = [',', ';', ' ']
print(split_by_delimiters(string, delimiters))
