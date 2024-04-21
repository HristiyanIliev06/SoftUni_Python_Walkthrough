import re

pattern = r'\d+'
line = input()
while line:
    match = re.findall(pattern, line)
    if match:
        print(' '.join(match), end=' ')
    line = input()