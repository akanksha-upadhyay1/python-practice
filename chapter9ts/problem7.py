with open("log.txt") as f:
    kaddu = f.readlines()
lineno = 1
for line in kaddu:
    if("odio" in line):
        print(f"yes, odio is present. Line no:{lineno}")
        break
    lineno = lineno + 1
else:
    print("No, odio is not present")
    # print(kaddu)