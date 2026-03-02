l = [1, 3, 4, 5, 2, 30 ,31]

l2 = sorted(l)
print(l2)
l3 = [[]]
print(l2)
print(len(l2))

# print(l2[0:1])
# print(l2[0:2])
# print(l2[::-1])

k=0
for i in range(1, len(l2)):
    # print(i)
    if l2[i] - l2[i-1] ==1:

        v = l2[k: i+1]
        print(v)
        l3.append(v)
    else:
        k=i
        continue
print(l3)

# l3 = []
# s = str(l2[0]) + ","
# for i in range(1, len(l2)):
#     if l2[i] - l2[i-1] ==1:
#         s = s + str(l2[i]) + ","
#         l3.append(s)
#
#     else:
#         s = str(l2[i]) + ","
#
# print(l3)
# max = len(l3[0].split(","))
# for i in l3:
#     if len(i.split(","))>max:
#         max = len(i.split(","))
# print(max -1 )





