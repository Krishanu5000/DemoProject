# def moveZeoAtEnd(l):
#     cnt = 0
#     for i in range(len(l)):
#         if i ==0 and l[i] != 0:
#             l[cnt] = l[i]
#             cnt+=1
#         elif i != 0 and l[i] != 0:
#             temp = l[i -1]
#             l[cnt] = l[i]
#             l[i] = temp
#             cnt+=1
#     return l
#
# print(moveZeoAtEnd([10, 0 ,30 ,25]))
# print(moveZeoAtEnd([0, 0 ,30, 0 ,25]))