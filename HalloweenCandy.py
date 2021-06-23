import math
houses = int(input())

dollar = (2 / houses)*100

if houses >= 3:
    print(math.ceil(dollar))