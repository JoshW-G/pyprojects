"""
example input n = num of words. 
4
bcdef
abcdefg
bcde
bcdef

prints number of unique words and the count
"""

n = int(input())
count = []
words = {}
for i in range(n):
    w = input()
    if w not in words:
        words[w] = 1
    else:
        words[w] = words.get(w) + 1
print(len(words))
for j in words:
    print(words.get(j), end=" ", flush=True)