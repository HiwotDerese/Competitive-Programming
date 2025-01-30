# """
# Convert a non-negative integer num to its English words representation.

# Example 1:

# Input: num = 123
# Output: "One Hundred Twenty Three"
# Example 2:

# Input: num = 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:

# Input: num = 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

# 1,234,567
 
# 0 - 19
# 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000, 1000,000, 1,000,000,000


# Constraints:

# 0 <= num <= 231 - 1
# """
# import math

# def conver_to_word(num):
#     number_words = {
#         "0": "zero",
#         "1": "one",
#         "2": "two",
#         "3": "three",
#         "4": "four",
#         "5": "five",
#         "6": "six",
#         "7": "seven",
#         "8": "eight",
#         "9": "nine",
#         "10": "ten",
#         "11": "eleven",
#         "12": "twelve",
#         "13": "thirteen",
#         "14": "fourteen",
#         "15": "fifteen",
#         "16": "sixteen",
#         "17": "seventeen",
#         "18": "eighteen",
#         "19": "nineteen",
#         "20": "twenty",
#         "30": "thirty",
#         "40": "forty",
#         "50": "fifty",
#         "60": "sixty",
#         "70": "seventy",
#         "80": "eighty",
#         "90": "ninety",
#         "100": "one hundred",
#         "1000": "one thousand",
#         "1000000": "one million",
#         "1000000000": "one billion",
#     }

#     str_ = str(num)
#     if num <= 20:
#         return number_words[str(num)]
    
#     if len(str_) < 3:
#         curr = "".join([str_[0], '0'])
#         return number_words[curr] + str_[1]
    
#     def hundred_digit(digit_):
#         temp = digit_[1:].int()
#         ans = number_words[digit_[0]] + 'hundred' + number_words[temp.str()]
    
#         return ans
    
#     len_ = math.ceil(len(str) / 3)

#     digits = {1: 'thousand', 2: 'million', 3: 'billion'}

#     arr = [0] * len_

#     for i in range(len(num), -1, -1):
#         curr = num[i - 3, i]
#         if i in digits:



    


