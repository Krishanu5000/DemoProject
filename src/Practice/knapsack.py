def knapsack(W, val, wt):
    # code here
    s = 0
    l1 = []
    l2 = []
    for i in range(len(val)):
        l1.append((val[i]/wt[i],wt[i],val[i]))


    for i in range(len(val)):
        l2.append(val[i]/wt[i])

    l3 = sorted(l2)
    # print(l2)
    print(l3)
    print(l1)



    for i in range(len(l3)-1,-1,-1):
        cnt = 1
        for j in range(len(l1)):
            # print(l1[j][0])
            # print("i",i,"l3[i]",l3[i])
            if l3[i] == l1[j][0] and cnt==1:
                # print("inside case")
                if l1[j][1]<=W:
                    s+=(l1[j][0] * l1[j][1])
                    W-=l1[j][1]
                    print(l3[i],"i",i,"j",j,"s",s,"w",W,"cnt",cnt)
                    cnt+=1

                elif l1[j][1]>W and W>0 and cnt==1:
                    print((l1[j][0] * (W/l1[j][1])))
                    if (l1[j][0] * (W/l1[j][1]))>0 and (l1[j][0] * (W/l1[j][1]))<1:
                        s+0
                    else:
                        s+=round(l1[j][0] * (W/l1[j][1]))
                    W-=(W/l1[j][1])
                    print(l3[i],"i",i,"j",j,"s",s,"w",W,"cnt",cnt)
                    cnt+=1



    return int(s)

# print(knapsack(4,[6,3,8,6,9,8,2,4,10,9],[2,1,3,1,4,1,2,2,5,7]))
# print(knapsack(5,[1,9,2,9,4,4],[5,2,3,4,9,6]))
print(knapsack(7,[10,8,6],[1,7,9]))




