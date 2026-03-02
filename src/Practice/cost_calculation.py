def cost_estimation(input1, input2, input3, input4, input5):
    cost = []
    tot_cost = []
    for i in range(input2):
        for j in range(len(input1)):
            cost.append(input1[j])
    print("cost - ", cost)
    M = (10 ** 9) + 7
    print(M)
    for i in range(input5):
        s = 0
        for j in range(input3[i]-1,input4[i]):
            s += cost[j] % M
        tot_cost.append(s)
    return tot_cost


print(cost_estimation([4,5,1] , 3, [1,3], [4,5], 2))