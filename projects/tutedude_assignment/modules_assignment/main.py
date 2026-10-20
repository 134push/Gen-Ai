import math_utils
import string_utils
import shop_packages.discount as disc 
additions = math_utils.add(4,3)
print("the addition of the number : ",additions)

substraction = math_utils.sub(7,89)
print("the substraction of the number : ",substraction)

capitalize_words = string_utils.capitalize_words("hello world")
reverse_string = string_utils.reverse_string("hello world")
words_count = string_utils.words_count("hello world")

print(capitalize_words)
print(reverse_string)
print(words_count)

from math_utils import sqar
square = sqar(5)
print("the square of the number : ",square)

print("the apply_discount  is : ",disc.apply_discount(500,10))

print("the flat_discount is : ",disc.flat_discount(500))

from shop_packages.billing import Calculate_total
final_bill = Calculate_total(500,10)
print("your total bill : ",final_bill)