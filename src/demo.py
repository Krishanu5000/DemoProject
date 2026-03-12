# from where jon group by having select union order by

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

1. read data from s3 folder
2. filter the data
3. aggregare the dataclasses
4. show result

df =spark.read.format().load()  -- stg1
df = df.filter().groupbY().agg(max()).show() -- job2
stage1 stge2

O/P : [["eat", "ate", ""]]

