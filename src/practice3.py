# below is the incorrect version of code. because only considering 2 combinations -
'''def minimum_unhappy_person(input1, input2, input3):
    d={}
    for i in range(len(input2)):
        if input2[i] not in d:
            d[input2[i]]=1
        else:
            d[input2[i]]+=1
    print(d)

    friends_group = []
    for i in d.keys():
        friends_group.append(i)

    comnination_of_friends_group = []

    for i in range(len(friends_group)):
        comnination_of_friends_group.append([friends_group[i]])
        for j in range(i+1, len(friends_group)):
            comnination_of_friends_group.append([friends_group[i], friends_group[j]])

    print(comnination_of_friends_group)

    unhappy_person_list = []

    for i in range(len(comnination_of_friends_group)):
        l1 =0
        s=0
        print(comnination_of_friends_group[i])
        while l1<len(comnination_of_friends_group[i]):
            s+=d[comnination_of_friends_group[i][l1]]
            l1+=1
        unhappy_person_list.append(abs(s - input3))

    print("unhappy_person_list", unhappy_person_list)

    return min(unhappy_person_list)

print(minimum_unhappy_person(7, [1,1,2,2,2,3,3], 3))'''


# correct version of code using dynamic programming

def minimum_unhappy_person(input1, input2, input3):
    # Count people in each group
    d = {}

    for g in input2:
        d[g] = d.get(g, 0) + 1

    groups = list(d.values())

    # DP stores all possible sums
    possible = {0}

    for size in groups:

        new_possible = set()

        for s in possible:
            new_possible.add(s)
            new_possible.add(s + size)

        possible = new_possible

    ans = float("inf")

    for s in possible:
        ans = min(ans, abs(s - input3))

    return ans


print(minimum_unhappy_person(7, [1, 1, 2, 2, 2, 3, 3], 3))
