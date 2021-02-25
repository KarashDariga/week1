# palindrome?
# aba abba - Yes
# abb aabc - No
line = input()

new_line = ''.join(reversed(line)) # split(',')
if line == new_line:
    print('Yes')
else:
    print('No')    

