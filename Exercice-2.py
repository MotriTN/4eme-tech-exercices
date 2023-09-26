ch = input("Donner ch : ")
while not ((ch[-1] == ".") and (ch != ".")):
    ch = input("Donner ch : ")
k = " "
s = ""
p = 0
for i in range(len(ch)):
    if ch[i] != k:
        s += ch[i]
    else:
        if i + 1 < len(ch) and ch[i + 1] != k:
            s += k
            p += 1
if (s[-2] != k):
    p += 1
else:
    s = s[0:-2] + "."

print("mots: ", p)
print(s)
#correction
"""ch = input("Donner ch : ")
while not ((ch[-1] == ".") and (ch != ".")):
    ch = input("Donner ch : ")
i = 0
while i < len(ch) - 1:
    if ch[i] == ch[i + 1] == " ":
        ch = ch[:i] + ch[i + 1:]
    else:
        i += 1
print(ch)
"""
