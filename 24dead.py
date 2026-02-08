f = open("2.txt").read()

min_len = 100_000
for l in range(len(f)):
    for r in range(l + min_len, l, -1):
        if f[l:r].count("A") < 2024:
            break
        if f[l:r].count("A") == 2024:
            min_len = len(f[l:r])
            print(min_len)
print(min_len) 