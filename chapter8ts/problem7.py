l = ["harry", "Rohan", "shubham", "an"]
def akan(l,word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

print(akan(l, "an"))