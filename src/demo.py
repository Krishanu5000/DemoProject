# from join where  group by having select union order by

# A
# id value
# 1  A1
# 2  A2
# 3  A3
# null A4
# 5   A5
#
# B
# id value
# 1  B1
# 2  B2
# 4  B3
# null B4
# 6   B5
#
# inner 1 , 2
# left A join B - 1, 2, 3, 5
# right join A join B 1, 2, 4, null, 6
# full outer A join B 1, 2, 3, 4, null, null , 5 , 6
#
# sales
# year product_id product_name month sale ytd
# 2026 1          A            1      10  10
# 2026 1          A            2      11  21
# 2026 1          A            3      9   30
# 2026 1          A            4      5   35
#
# select year,product_id,product_name,month,sale, sum(sale)over(partition by product_id, year order by month) as ytd
# from sales
#
# team_score
# player1 10
# player2 15
# player3 40

l = [10, 10 , 20 ,20 , 20 , 30 ,31, 40, 40, 40 ,40]

# def maxoccuringelemnet(l):
#     d = {}
#     for i in range(len(l)):
#         if l[i] not in d.keys():
#             d[l[i]] = 1
#         else:
#             d[l[i]] +=1
#     print(d)
#
#     max = d[l[0]]
#
#     for i in d.keys():
#         if d[i]>max:
#             max=d[i]
#     print(max)
#
#     return max,i
#
# maxoccuringelemnet(l)
#
# s = ["eat", "tea", "tan", "ate", "nat", "bat"]
#
# 0, n
# 1, n
#
#  ate

# 1. read data from s3 folder
# 2. filter the data
# 3. aggregare the dataclasses
# 4. show result
#
# df =spark.read.format().load()  -- stg1
# df = df.filter().groupbY().agg(max()).show() -- job1
# stage1 stge2

# O/P : [["eat", "ate", ""]]

def dacade_in_words(s, decimal_dict):
    if len(s) == 2:
        q = int(s)//10
        r = int(s)%10
        if decimal_dict[q] == 1:
            return "Ten" + decimal_dict[r]
        elif decimal_dict[q] == 2:
            return "Twenty" + decimal_dict[r]
        elif decimal_dict[q] == 3:
            return "Thirty" + decimal_dict[r]
        elif decimal_dict[q] == 4:
            return "Fourty" + decimal_dict[r]
        elif decimal_dict[q] == 5:
            return "Fifty" + decimal_dict[r]
        elif decimal_dict[q] == 6:
            return "Sixty" + decimal_dict[r]
        elif decimal_dict[q] == 7:
            return "Seventy" + decimal_dict[r]
        elif decimal_dict[q] == 8:
            return "Eighty" + decimal_dict[r]
        elif decimal_dict[q] == 9:
            return "Ninety" + decimal_dict[r]

# def number_to_words(n):
#     decimal_dict= {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
#     if len(str(n)) == 1:
#         return decimal_dict[n]
#     s = ""
#     while len(str(n)) <= 3:
#         if len(str(n)) == 3:
#             multiple_of_hundred = decimal_dict
#             n = n//10
#             k = dacade_in_words(n , decimal_dict)
#
#             return



def number_to_words(n):
    ones = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    teens = {11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
    tens = {1:"ten",2:"twenty", 3:"thirty", 4:"fourty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}

    if n < 10:
        return ones[n]
    elif n<20:
        return teens[n]
    elif n<100:
        return tens[n//10] + number_to_words(n%10)
    elif n<1000:
        return  ones[n//100] + " hundred " + number_to_words(n%100)



print(number_to_words(121))

