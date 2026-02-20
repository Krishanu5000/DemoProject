def pattern_searching(numbers, pattern):
    s=0
    flg = False
    for i in range(len(numbers) - len(pattern) + 1):
        k = i
        for j in range(len(pattern)):
            if i==0:
                break
            elif numbers[i + j] > numbers[i + j-1] and pattern[j] == 1:
                flg = True
            elif numbers[i + j] == numbers[i + j-1] and pattern[j] == 0:
                flg = True
            elif numbers[i + j-1] < numbers[i + j]  and pattern[j] == -1:
                flg = True
            else:
                flg = False
                break
        if flg:
            s+=1
    return s

print(pattern_searching([4,5,5,7,9,9,10],[1,0,-1]))
print(pattern_searching([4,3,3,7,9,9,10],[-1,0,-1]))

