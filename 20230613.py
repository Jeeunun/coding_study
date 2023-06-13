# <모함가 길드>
# import math
# math.gcd

# <곱하기 혹은 더하기>
# replace /  for in 

# 예시로 풀어보기 
numInput = (input("숫자 0부터 9로 이루어진 문자열을 입력하세요: ")) #02984
numInput2 = list(map(int, numInput.replace("0",''))) #2984

multiply = 1
for i in numInput2:
    multiply = multiply * i 
print(multiply)

# 프로그램 구현
def solution(numInput):
    numInput2 = list(map(int, numInput.replace("0",'')))
    multiply = 1
    for i in numInput2:
        multiply = multiply * i
    return multiply

result = solution('567')
print(result)