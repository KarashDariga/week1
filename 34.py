# palindrome?
# aba abba - Yes
# abb aabc - No
line = input()
if line == line[::-1]:
    print('Yes')
else:
    print('No')