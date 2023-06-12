# <모함가 길드>
# import math
# math.gcd

# <곱하기 혹은 더하기>
# split /  for in 

# 예시로 풀어보기 
numInput = (input("숫자 0부터 9로 이루어진 문자열을 입력하세요: "))
#5294068
numInput2 = numInput.split("0")
#['5294', '68']
first = list(map(int, list(numInput2[0]))) 
#[5, 2, 9, 4]
second = list(map(int, list(numInput2[1]))) 
#[6,8]

multiply = 1
for i in first:
    multiply = multiply * i
print(multiply)
# numInput2[0]부분끼리의 곱

multiply2 = 1
for j in second:
    multiply2 = multiply2 * i
print(multiply2)
# numInput2[1]부분끼리의 곱

result = multiply + multiply2
#최종 정답은 곱셈끼리 더하는 것.
print(result)

# 프로그램 구현
