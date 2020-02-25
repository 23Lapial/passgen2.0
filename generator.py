#!/usr/bin/env python3

temp_pass = str(input())

password = []

# Upper every other character(starts at index 0)
for index, character in enumerate(temp_pass.lower()):
    if index % 2 == 1:
        password.append(temp_pass[index].lower())
    else:
        password.append(temp_pass[index].upper())

print(''.join(sorted(password, reverse=True)))

# ALL THAT IN ONE LINE
print(''.join(sorted([character.upper() if index % 2 == 0 else character.lower() for index, character in enumerate(input().lower())], reverse=True)))
