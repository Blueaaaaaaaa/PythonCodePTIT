s,c=input(),input()
if not s.find(c): print('0')
else: print(s.find(c),len(s)-s[::-1].find(c)-1)
