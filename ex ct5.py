import math


#size 종류 15개 중복조합
print(math.factorial(15) / (math.factorial(7) * math.factorial(15 - 7)) / 
    (math.factorial(21) / (math.factorial(7) * math.factorial(21 - 7))) * 100, "%")
