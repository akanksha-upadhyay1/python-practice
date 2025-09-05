with open ("poem.txt") as f:
    content = f.read()

if("twinkle" in content):
    print("The word twinkle is in the content")
else:
    print("The word twinkle is not in the content")

