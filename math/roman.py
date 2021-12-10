def int_to_roman(n):
    ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    nums = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    result = []

    for i in range(len(nums)):
        count = int(n / ints[i])
        result.append(nums[i] * count)
        n -= ints[i] * count

    return "".join(result)


print(int_to_roman(13))
