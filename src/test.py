# list = [1,2,3,4,4,5,2,4,6,8,3,5,2,4]
#
# d = {}
# for i in list:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
#
# for key, value in d.items():
#     print(key,":", value)

dict1 = {1:'a', 2:'b', 3:'c'}

dict2= {1:'d', 2:'e'}

dict3 = {}

for key, value in dict1.items():
    if key in dict2:
        dict3[key] = (dict1[key], dict2[key])
    else:
        dict3[key] = dict1[key]

print(dict3)


