import re
string = input()
"""matches = re.findall(r'_\w+', string)
result = []
for match in matches:
    new_match = re.search(r'[^_]\w+', match)
    result.append(str(new_match.group()))
print(','.join(result))"""
matches = re.findall(r'\b_([a-zA-Z0-9]+)\b', string)
print(','.join(matches))