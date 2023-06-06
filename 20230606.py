# # <숫자 카드 게임>

# # 1. 내가 생각하는 구성
# #  = 리스트로 생각해보자..!
# #  m개의 열을 리스트화 => [[첫번째 열의 값들],[두번째 열의 값들],[세번째 열의 값들],,,,[N번째 열의 값들]] => n개가 있는 것
# #  [[],[],[],,,[]] => 즉, 각각의 리스트 안에는 M개의 수가 있고 / 리스트는 N개의 리스트가 있는 것.
# # 1) 각각의 리스트를 정렬하기
# # 2) 사용자가 행(n) 선택 ! =input 
# # 3) 가장 큰 수 구하기 = index 활용 !!


# # 2. 예시로 파악하기
# #  - 안에 있는 각각의 리스트를 정렬 시키자. 
# n = 3
# m =3
# lista=[[3,1,2],[4,1,4],[2,2,2]]
# for a in range(0,3): #a= list_n[0],list_n[1],list_n[2] #for a in range(0,n)
#     lista[a].sort()
# print(lista)
#     # 결과 :[[1, 2, 3],[1, 4, 4],[2, 2, 2]]


# # - 사용자가 행(n)을 선택 = > lista[n-1] 의 값을 선택하는 것
# #  가장 작은 수 선택하기 => 인덱스 활용
# # choose_n = int(input("몇 번째 행을 선택하시겠습니까?: ")) 
# # print(lista[m-1][0])

# # - 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 하기
# # 빈리스트를 만들어서 각각의 리스트 안에 있는 가장 작은 수를 append시킨다.
# # 조건문 if ~ else를 사용해서 새로만든 리스트의 가장 큰 수와 앞서 선택한 가장 작은 수를 비교
# #  

# # 3. 프로그램 구현
# # 1) M=3, N=3, choose_n = 2인경우
# m = 3
# n = 3
# choose_n = 2
# listb = []

# lista=[[3,1,2],[4,1,4],[2,2,2]]
# for a in range(0,3):
#     lista[a].sort()

# for b in range(len(lista)):
#     listb.append(lista[a][0])

# if listb[-1] >= lista[choose_n-1][0]:
#     print(listb[-1])
# else:
#     print(lista[n-1][0])

# # 결과 : 2

# # # 2) M=2, N=4 choose_n = 1
# m = 2
# n = 4
# choose_n = 1
# listb = []

# lista = [[7,3,1,8],[3,3,3,4]]
# for a in range(0,2):
#     lista[a].sort()

# for b in range(len(lista)):
#     listb.append(lista[a][0])

# if listb[-1] >= lista[choose_n-1][0]:
#     print(listb[-1])
# else:
#     print(lista[n-1][0])

# #결과 3

# # ---------------------------------------------
# # <1이 될 때까지>
# 1. 내가 생각하는 구성
#  1) 크게 N이 K로 나눠지는 경우 와 N이 K로 나눠지지 않는 경우로 나눌 수 있다.
#  2) N이 K로 나눠지는 경우에 2번과정 -> 실행과정 count
#  3) N이 K로 나눠지지 않는 경우엔 1번과정 후 N이 K로 나눠지는 경우에 2번과정 실행 -> 실행과정 count

# 2. 예시로 파악하기 하 모르겠따....
n = 17 
k = 4
cnt = 0
while n>0:
    if n % k == 0:
        cnt += 1
        print(cnt)
    else :
        for a in range(1, n):
            n -= a
            cnt += 1
            if n % k == 0:
                cnt += 1
        print(cnt)


# 3. 프로그램 구현

