# p110 예제 4-1 <상하좌우>
# <아이디어>
# N X N 정사각형 -> 가장 왼쪽 위 좌표(1,1) / 가장 오른쪽 아래 좌표(N,N)
# 위치 좌표 (X,Y)라 할 때
# L(왼쪽이동) : Y 의 변화(-)
# R(오른쪽이동) : Y 의 변화 (+)
# U (위로 이동) : X 의 변화 (-) => X=1일때 위로 이동시, 공간범위 벗어남(조건문으로 해결)
# D (아래로 이동) : X의 변화 (+) => X=N일때 아래로 이동시, 공간범위 벗어남(조건문으로 해결)

# <예제>
now = [1,1] #현재위치
N = int(input("공간의 크기를 설정하세요: "))
plan = list(input("어느 방향으로 갈까요?(L,R,U,D): "))

for p in plan:
    if p == 'L':
        now = (now[0], now[1] - 1)
        if now[1] < 1 :
            now = (now[0],now[1]+1)
    elif p == 'R':
        now = (now[0], now[1] + 1) 
        if now[1] < 1 :
            now = (now[0],now[1]-1)   
    elif p == 'U':
        now = (now[0] - 1,now[1])
        if now[0] < 1:
            now = (now[0]+1,now[1])
    elif p == 'D':
        now = (now[0] + 1, now[1])
        if now[0] > N:
            now = (now[0]-1, now[1])

print(now)

# <프로그램구현>
def solution(N,plan):
    now = [1,1]
    for p in plan:
        if p == 'L':
            now = (now[0], now[1] - 1)
            if now[1] < 1 :
                now = (now[0],now[1]+1)
        elif p == 'R':
            now = (now[0], now[1] + 1) 
            if now[1] < 1 :
                now = (now[0],now[1]-1)   
        elif p == 'U':
            now = (now[0] - 1,now[1])
            if now[0] < 1:
                now = (now[0]+1,now[1])
        elif p == 'D':
            now = (now[0] + 1, now[1])
            if now[0] > N:
                now = (now[0]-1, now[1])
    return now

# --------------
# p113 예제 4-2 <시각>
# <아이디어>
# 1) 정수 N = input
# 2) time = ['00','00','00'] ~ ['0N','59','59'] 
# => 첫번째 인덱스는 0~N범위
# => 두번째, 세번째 인덱스는 0~59범위 
# 3) 3이 들어있으면 count

# %%
# <예제>
N = 5
count = 0 #시작점
for i in range(0,N+1): # i = 첫번째 인덱스 범위값
    for j in range(0,60): # j = 두번째 인덱스 범위값
        for z in range(0,60): # z = 세번째 인덱스 범위값
            if '3' in str(i) + str(j) +str(z): # time 리스트(모든 인덱스값) 에서 '3'이 포함된 경우 
                count +=1 

print(count)
            # 처음 시도 : 왜 안될까?
            # if sum(map(lambda x:x.count("3"),[str(i),str(j),str(j)])):
            #   count += 1
# %%

# <프로그램구현>
def solution(N):
    N = input("정수를 입력하세요: ")
    count = 0
    for i in range(0,N+1): 
        for j in range(0,60):
            for z in range(0,60): 
                if '3' in str(i) + str(j) +str(z): 
                    count +=1 
    return count

# --------------
# p115 실전문제 <왕실의 나이트>
# <아이디어>
# N X N => 1~N까지의 정사각형 범위
# now(현재위치) = input
# = 4-1예제 <상하좌우>와 같은 문제라 생각함.
#%%
# <예제>
N = 8 # 8X8
now = c3 #=> c~> 문자를 숫자로 변환(ord()) / 3

direction = [(-1,-2),(-1,2),(1,2),(1,-2),(2,-1),(2,1),(-2,1),(-2,-1)]
# 수평으로(y) 두칸(오른쪽+2, 왼쪽-2) 이동 + 수직으로(x) 한칸 (위-1. 아래+1) 이동 
# 수직으로(x) 두칸(위-2. 아래+2) 이동 + 수평으로(y) 한칸(오른쪽+1, 왼쪽-1) 이동
# 그러나, 현재 위치가(2,3)이므로 (-2,1),(-2,-1)일 경우 N의 범위에서 벗어남.
# 따라서 현재위치(2,3)에서 갈 수 있는 방향의 개수는 [(-1,-2),(-1,2),(1,2),(1,-2),(2,-1),(2,1)] 총 6가지

# print(ord('a')) #97
# print(ord('c')) #99

# # # <프로그램 구현>
N = input("N의 정수값을 입력하세요: ") 
now = input("현재 위치를 입력하세요: ") #a1 = (1,1)
# x = int(now[1]) 
# y = int(ord(now[0])) - int(..........................................................................022222220ord('a'))+1

direction = [(-1,-2),(-1,2),(1,2),(1,-2),(2,-1),(2,1),(-2,1),(-2,-1)]

 #시작점 설정
def solution(N,now):
    x = int(now[1]) 
    y = int(ord(now[0])) - int(ord('a'))+1
    count = 0
    for d in direction:
        x = x + d[0]
        y = y + d[1]
        if 0<x<N+1 and 0<y<N+1:
            count+=1
    return count

result = solution(8,'a1')
print(result)
# ---------------
# p118 실전문제 <게임개발> 아 넘 어렵당~
# <아이디어>

# <예제>

# <프로그램 구현>


