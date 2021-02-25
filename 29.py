# palindrome?
# aba abba - Yes
# abb aabc - No
line = input()

ok = True
for i in range(int(len(line)/2)):
    if line[i] == line[len(line) - i - 1]:
     ok = False

if ok:
    print('Yes')
else:
    print('No')    