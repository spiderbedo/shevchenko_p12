s1 = input()
s2 = input()
s3 = input()

set1 = set(s1)
set2 = set(s2)
set3 = set(s3)

usym = (set1 - set2 - set3) | (set2 - set1 - set3) | (set3 - set1 - set2)
print("".join(usym))

