# palindrome?
# aba abba - Yes
# abb aabc - No
line = input()
#if line == line[::-1]:
#   print('Yes')
#else:
#    print('No')
print('Yes') if line == line[::-1] else print('NO')
# cout << 2 == 2 ? Yes: No