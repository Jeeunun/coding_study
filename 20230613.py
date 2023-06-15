# <모함가 길드>
# import math
# math.gcd

# 예시로 풀어보기
n = 5
fear_level = 2,3,1,2,2

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
# ---------------------------------------------------------------
# <문자열 뒤집기>
def solution(x):
    numlist=list(x)
    re_idx=[]
    for i in range(len(numlist)):
        if numlist[i]!=numlist[0]:
            re_idx.append(i)

    #특수사항 000 or 001
    # if re_idx==[]:
    #     return 0 #=문자열 모두 같은 값이다.
    # # if len(re_idx)==1:
    #     return 1 #= 값이 다른 것이 하나 = 한번만 뒤집으면 된다. 
    
    # n,result=0,0
    # while n<len(re_idx)-1:
    #    if re_idx[n]+1!=re_idx[n+1]:
    #        result+=1
    #     n+=1
    # return result+1
    return len(set([x[1]-x[0] for x in enumerate(re_idx)])) if re_idx else 0

# # numlist = list('00011000')
# # i=0,1,2,3,4,5,6,7
# # 첫번째 인덱스 값과 다른 값을 찾아서 re_idx에 append 
# # re_idx가 뜻하는 것 -> 첫번째 값과 다른 값의 인덱스 re_idx => (3,4)
# # enumerate(re_idx) -> {(인덱스,인덱스의 값) ....} print(list(enumerate(re_idx))) => [(0, 3), (1, 4)]
# # 이걸 하나씩 꺼내서(=x) 인덱스값 - 인덱스 => 3,3 = 이 의미는 값이 같다는 것 = 연속된 값.

x = '00011000'
numlist=list(x)
re_idx=[]
for i in range(len(numlist)):
    if numlist[i]!=numlist[0]:
        re_idx.append(i)
print(list(enumerate(re_idx)))