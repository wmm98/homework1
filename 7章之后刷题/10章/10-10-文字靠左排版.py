pos = int(input())
line_list = []
# line_list.append('Digital Intermediate by :   EFILM')
# line_list.append('Supervising    Digital Colorist : STEVEN J. SCOTT')
with open("listin.txt") as in_file:
    line_list = in_file.readlines()

with open("listout.txt", "w") as out_file:
    for line in line_list:
        left, right = line.split(':')
        print(left, type(left))
        left = ' '.join(left.split())
        print(left)
        left_out = ("%-" + str(pos - 2) + "s") % left
        print(left_out)
        right = right.strip()
        right = ' '.join(right.split())
        result = left_out + " : " + right + "\n"
        # print(result)
        # result = left + ":" + right + "\n"
        out_file.write(result)
