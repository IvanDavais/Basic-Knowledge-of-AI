row = 1
while row <= 9:
    col = 1
    while col <= row:
        result = col * row
        print("%d * %d = %d " %(col, row, result), end="\t")
        col += 1
    print("")
    row += 1