n = int(input())
f = open("listin.txt")
f1 = open("listout.txt", "w+")
content = f.readlines()
for line in content:
    result = ""
    line = line.strip().split(":")
    # print([i for i in line[0].split(" ") if i != ""])
    for j in [i for i in line[0].split() if i != ""]:
        result += j + " "
    result = result.strip()
    # print(result)

    result1 = ""
    for s in [r for r in line[1].split() if r != ""]:
        result1 += s + " "
    result1 = result1.strip()

    f1.write(result.rjust((n - 2), " ") + " " + ":" + " " + result1 + "\n")

f.close()
f1.close()
