def all_variants(text):
    for i in range(1, len(text) + 1):
        char = 0
        while char < len(text):
            if char + i <= len(text):
                yield(text[char:char + i])
            char += 1

a = all_variants('abc')
for i in a:
    print(i)