import re
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

# def removedDuplicates(l):
#     d = {}
#     for i in range(len(l)):
#         if l[i] not in d.keys():
#             d[l[i]] = 1
#         else:
#             d[l[i]] += 1
#
#     return list(d.keys())
#
#
# print(removedDuplicates([1, 1, 1, 8, 2, 2, 3, 4, 5, 6, 6, 7, 7, 2]))

# def leadersInArray(l):
#     curr_leader = l[len(l) - 1]
#     leaders_arr = [curr_leader]
#
#     for i in range(len(l) - 2, -1, -1):
#         if l[i] > curr_leader:
#             curr_leader = l[i]
#             leaders_arr.append(curr_leader)
#     return leaders_arr
#
#
# print(leadersInArray([1, 1, 1, 8, 2, 2, 3, 4, 5, 6, 6, 7, 7, 2]))

# def maxSubarraySum(l):
#     maxending = l[0]
#     res = l[0]
#     for i in range(1, len(l)):
#         maxending = max(maxending + l[i], l[i])
#         res = max(maxending, res)
#     return res
#
#
#
# print(maxSubarraySum([2, 3, -8, 7, -1, 2, 3]))

# def maxlistsequence(l):
#     l1 = []
#     l = sorted(l)
#     #print(l)
#     cnt = 0
#     for i in range(1, len(l)):
#         if l[i] - l[i - 1] == 1:
#             k = l[cnt: i + 1]
#             l1.append(k)
#         else:
#             cnt = i
#     print(l1)
#     max = len(l1[0])
#     for i in range(len(l1)):
#         if len(l1[i]) > max:
#           max = len(l1[i])
#     return max
#
# print(maxlistsequence([1, 3, 4, 5, 2, 30, 31]))

# Write a Python program to count how many words contain only alphabets in a sentence.
'''s = "Hello world 123 Python3 code"
cnt = 0
for i in s.split(" "):
    if i.isalpha():
        cnt+=1
print(cnt)'''

# extract only alphabetic characters from a string
'''s = "Py@th#on123!"
s1 = ""
for i in s:
    if i.isalpha():
        s1 += i
print(s1)'''

# extract all numbers from a string.
s = "Order123 price450 item67"
l1 = []
for i in s.split(" "):
    k = re.sub(r'[a-zA-Z]', '', i)
    l1.append(k)
print(l1)
print(re.findall(r'\d+', s))
print(re.search(r'\d+', s).group())

# If the regex contains groups (), findall() returns tuples.
text = "Jan 2024, Feb 2025"
result = re.findall(r'([A-Za-z]+) (\d+)', text)
print(result)

# Write a program to separate letters, digits, and special characters.
s = "Pyth0n@2026!"
d = {}
d['Letters'] = ''.join(re.findall(r'[a-zA-Z]', s))
d['Digits'] = ''.join(re.findall(r'[0-9]', s))
d['SpecialCharecters'] = ''.join(re.findall(r'[^a-zA-Z0-9]', s))
print(d)
print(re.sub(r'[^a-zA-Z0-9]','',s))

# Find all occurrences of a substring using find().
text = "banana"
start = 0
while True:
    pos = text.find("a", start)
    if pos == -1:
        break
    print(pos)
    start = pos + 1

s = "getAccountName"
s1 = ""
for i in range(len(s)):
    if s[i].isupper():
        print("iteration,", i)
        s1 += s[i]
        cnt = i+1
        print(s1)
        while cnt <= len(s) -1 and s[cnt].islower() :
            s1 += s[cnt]
            cnt += 1
        s1 = s1 + '_'
print(s1[:-1])


#find a missing number
def findmissingnumber(l):
    for i in range(1, len(l)):
        if l[i] - l[i-1]>1:
            print("***",i)
            return l[i-1] + 1
print("missing number")
print(findmissingnumber([1,2,3,5,6]))


##Remove Duplicates While Preserving Order

def removeduplicate(l):
    max_len = max(l)
    l2 = [0] * max_len
    for i in l:
        l2[i-1] += 1
    print(l2)
    for i in range(len(l)-1,-1,-1):
        #print(l[i] -1)
        if l2[l[i] -1] > 1:
            l2[l[i] -1]-=1
            l.pop(i)
    return l

print(removeduplicate([2,4,2,1,5,4,6]))

# Merge Two Sorted Lists
def mergeList(l1, l2):
    pass

print(mergeList([1,3,5], [2,4,6]))


# minimum unhappy person due to limited budget.


def dirmovement(s):
    s = re.sub(r"\./",'/',s)
    print(s)
    s = re.sub(r"/+",'/',s)
    print(s)


    l = s.split('/')

    print(l)

    stack = []
    for i in l:
        if i == '..':
            stack.pop()
        elif i!= '':
            stack.append(i)

    print(stack)

    return '/'+ '/'.join(stack)

print(dirmovement('/a/b////c//././..'))





