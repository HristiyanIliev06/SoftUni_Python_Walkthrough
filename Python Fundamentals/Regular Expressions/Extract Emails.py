import re
text = input()
email = r'\s(([a-z0-9]+([a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+))\b'
output =  re.findall(email,text)
for result in output:
    print(result[0])