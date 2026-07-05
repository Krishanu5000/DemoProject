def string_augment(s):
    n = len(s)
    result = []

    # Prefix + Suffix
    for i in range(1, n):
        left = int(s[:i])
        print(left)
        right = int(s[i:])
        print(right)
        result.append(left + right)

    # Sum of individual digits
    result.append(sum(int(ch) for ch in s))

    # Original number
    result.append(int(s))

    return result


print(string_augment("125"))