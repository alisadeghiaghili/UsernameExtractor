import os
import re

path = r'D:\aghazadeh\public-users'

files = ['\\'.join([path, file]) for file in os.listdir(path)]

usernames = []

for file in files :
    with open(file, 'r') as fileOpened:
        text = fileOpened.read().lower()
        usernames.append(re.findall(pattern = "['\"']*user\s?name['\"]*\s*[\:\=]\s*['\"]*([a-z.]+)\s*['\"]*.*\n*", string = text))
        

print(usernames)

final = []
for name in usernames:
    if len(name) > 1:
        for n in name:
            final.append(n)
    elif len(name) == 1:
        final.append(name)
        
final = list(set([name[0] if type(name) == list else name for name in final]))
