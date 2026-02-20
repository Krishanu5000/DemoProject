def asterik(n):
    for i in range(n):
        s = ""
        mid = n//2
        for j in range(n):
            if i== 0 and ( j == (n//2)):
                s += "*"
            elif i > 0  and (( j == mid-i) or (j == mid+i) or (j == mid)):
                # print("i",i,"j",j)
                s += "*"
            else:
                s += " "
        print(s)
asterik(3)