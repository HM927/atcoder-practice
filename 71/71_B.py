dictionary =  {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
S = input()

S_set = set()
for i in range(len(S)):
    S_set.add(S[i])

if dictionary - S_set:
    print(min(dictionary - S_set))
else:
    print("None")