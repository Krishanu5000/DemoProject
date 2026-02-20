import sys
# def getnumber(arr,val):
#     if val == 0:
#         return 0
#     res = sys.maxsize
#     for i in range(len(arr)):
#         print("i",i)
#         if arr[i]<=val:
#             print(arr[i])
#             # print("befor call:","i",i,"arr[i]",arr[i],"val",val,"arr[i]-val",val-arr[i])
#             subres = getnumber(arr,val-arr[i])
#             print("after return:","i",i,"arr[i]",arr[i],"val",val,"arr[i]-val",val-arr[i],"subres",subres)
#             if subres!= sys.maxsize:
#                 res = min(res,subres + 1)
#     return res
#
# getnumber([25,10,5],30)

def get(val):
    print(val)
    if val == 0:
        return 0
    res = sys.maxsize
    for i in range(1,val+1):
        # print("i",i,"val - i",val - i)
        subres = get(val - i)

        print("i",i,"subres",subres)
        if subres!=sys.maxsize:
            res = min(res,subres+1)
        print("i",i,"res",res)
    return res
print(get(3))


