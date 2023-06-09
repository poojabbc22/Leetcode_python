#1.reverse number
# def reverse(x):
#     if x == 0:
#         return 0
#     elif x > 0:
#         sign = 1
#     else:
#         sign = -1
#         x = -x
#     rev = 0
#     while x > 0:
#         rev = rev * 10 + x % 10
#         x //= 10
#     if rev > 2**31 - 1:
#         return 0
#     return sign * rev
# ring=reverse(278)
# print(ring)
#2.palindrome
# def is_palindrome(x):
#     if x < 0:
#         return False
#     original = x
#     rev = 0
#     while x > 0:
#         rev = rev * 10 + x % 10
#         x //= 10
#     return original == rev
# number = 123
# print(is_palindrome(number))
#3.permutation of strings
# def is_permutation(x, y):
#     if len(x) != len(y):
#         return False
#     x_chars = [0] * 256
#     for char in x:
#         x_chars[ord(char)] += 1
#     for char in y:
#         x_chars[ord(char)] -= 1
#         if x_chars[ord(char)] < 0:
#             return False
#     return True
# string1 = 'abcdef'
# string2 = 'pooja'
# print(is_permutation(string1, string2))
#3.generate roman numbers
# def int_to_roman(num):
#     val = [
#         1000, 900, 500, 400,
#         100, 90, 50, 40,
#         10, 9, 5, 4,
#         1
#         ]
#     syb = [
#         "M", "CM", "D", "CD",
#         "C", "XC", "L", "XL",
#         "X", "IX", "V", "IV",
#         "I"
#         ]
#     roman_num = ''
#     i = 0
#     while  num > 0:
#         for _ in range(num // val[i]):
#             roman_num += syb[i]
#             num -= val[i]
#         i += 1
#     return roman_num

# # test the function with a sample input
# print(int_to_roman(9))
#4.roman to integer.
# def roman_to_int(s):
#     roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
#                  'C': 100, 'D': 500, 'M': 1000}
#     int_val = 0
#     for i in range(len(s)):
#         if i > 0 and roman_val[s[i]] > roman_val[s[i - 1]]:
#             int_val += roman_val[s[i]] - 2 * roman_val[s[i - 1]]
#         else:
#             int_val += roman_val[s[i]]
#     return int_val

# # test the function with a sample input
# print(roman_to_int("IV"))
# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         if dividend == 0:
#             return 0
#         if divisor == 0:
#             return float('inf')

#         sign = -1 if ((dividend < 0) != (divisor < 0)) else 1
#         dividend = abs(dividend)
#         divisor = abs(divisor)

#         quotient = 0
#         while dividend >= divisor:
#             temp = divisor
#             multiple = 1
#             while dividend >= (temp << 1):
#                 temp <<= 1
#                 multiple <<= 1
#             quotient += multiple
#             dividend -= temp

#         if sign == -1:
#             quotient = -quotient
#         return min(max(-2147483648, quotient), 2147483647)
#     divide(9,3,3)
# solution = Solution()
# dividend = 10
# divisor = 3
# print(solution.divide(dividend, divisor))
#multiply two strings and output it as string
# def multiply(num1, num2):
#     return str(int(num1) * int(num2))
# sol=multiply("8","7")
# print(sol)
#claculate power of an int for eg 2^6
# def pow(x, n):
#     if n == 0:
#         return 1
#     if n < 0:
#         x = 1 / x
#         n = -n
#     result = 1
#     while n:
#         if n % 2 == 1:
#             result *= x
#         x *= x
#         n //= 2
#     return result
# sol=pow(10,-9)
# print(sol)
#duplicate in array
def removeDuplicates(nums):
    nums_set = set()
    i = 0
    for num in nums:
        if num not in nums_set:
            nums_set.add(num)
            nums[i] = num
            i += 1
    return i

nums = [1, 1, 2, 2, 3, 4, 4, 5, 6, 6]
length = removeDuplicates(nums)
print(nums[:length])

