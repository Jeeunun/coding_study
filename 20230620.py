# # # <만들 수 없는 금액>
# # # 만들 수 있는 금액(tot) 을 생각해보자.
# # # tot과 비교할 수 있는 값 x 설정
# # # coins 정렬 후 차례대로 동전을 추가해가며 만들 수 없는 금액을 찾아보자 !

# # # 1. 예제
# # coins = [3,2,1,1,9]
# # coins.sort() #[1,1,2,3,9]

# #     #1) tot = 1 
# #     #
# #     #2) 1원을 추가했을 때 
# #     #  tot = 2 
# #     #  x = 2 + 1 = 3
# #     #
# #     #3) 2원을 추가했을 때  
# #     #  tot = 4
# #     #  x=  3 + 2 = 5
# #     #   
# #     #4) 3원을 추가 했을 때
# #     #  tot = 7
# #     #  x = 5 + 3 = 8
# #     #
# #     #5) 9원을 추가 했을 때  
# #     # x보다 크다. => 만들 수 없는 최솟값은 8 !

# # # 2. 프로그램 구현
# # coins = list(map(int, input("가지고 있는 화폐 단위를 입력하세요: ")))
# # coins.sort() 

# # x = 1 # 만들 수 없는 금액과의 비교를 위해 만들 수 없는 금액 가상 설정
# # tot = 0 # 만들 수 있는 금액의 범위(누적합)


# # for coin in coins :
# #     tot+=coin
# #     if coin > x :
# #         break
# #     x += coin
# # print(x)
# #     # coins = [1,1,2,3,9] 일 때 
# #     # coin 1 -> x = 1, tot = 1 -> x = 2 #=최솟값 1을 만들 수 있다. 
# #     # coin 1 -> tot = 2, x = 2 -> x = 3 #=최솟값 2을 만들 수 있다.
# #     # coin 2 -> tot = 4, x = 3 -> x = 5 #=최솟값 3을 만들 수 있다.
# #     # coin 3 -> tot = 7, x = 5 -> x = 8 #=최솟값 5를 만들 수 있다.
# #     # coin 9 -> tot =16, x = 8 -> break #=최솟값 8 !

# # # 3. 함수
# # def solution(coins):   
# #     coins.sort() 
# #     x = 1
# #     tot = 0
# #     for coin in coins :
# #         tot+=coin
# #         if coin > x :
# #             break
# #         x += coin
# #     return x

# # coins = list(map(int, input("가지고 있는 화폐 단위를 입력하세요: ").split(' ')))
# # result = solution(coins)
# # print(result)

# def solution(x : list,n: int):
#     x.sort()
#     if x[0]!=1:
#         return 1
#     else:
#         #dictionary 완성
#         use_dict=dict.fromkeys(x,0)
#         for number in use_dict:
#             use_dict[number]=list(map(lambda i:number*i,range(x.count(number)+1)))
#         print(use_dict)
#         result=[0]
#         for plus_num in use_dict:
#             result=list(set(sum([list(map(lambda x:x+y,use_dict[plus_num])) for y in result],[])))
#             print(result)
        
#         return result
    
# result= solution([1,1,2,2,3],2) 
# n = 3
# print(result)
#         # #아랜 정답 채크용
#         # answer=sum(x)+1
#         # for final in range(1,answer+1):
#         #     if final not in result:
#         #         answer=final
#         #         break
#         # return answer

def money(prices):
    prices.sort()
    minimum = 1 # 만들 수 없는 최솟값의 초기 값
    for a in prices:
        
        if a <= minimum:
            # print(minimum)
            minimum += a
            

    return minimum
prices1 = [3, 2, 1, 1, 9]
print(money(prices1))

prices2 = [1, 3, 5, 7]
print(money(prices2))

# # # 궁금한 점 : N은 언제 써야 하는지..?

# # --------------------------------------------------------------------------------------
# # # <볼링공 고르기>
# # # 1. 예제
# # # n = 5
# # # m = 3
# # # weight = [1,3,2,3,2]
# # # 가능 : (1,3),(1,2),(1,3),(1,2),(3,2),(3,2),(2,3)
# # # 불가능 : (3,3),(2,2)

# # # 2. 프로그램구현
# # # 방법1 ) 기본 라이브러리 이용
# # from itertools import combinations
# # weight = [1,3,2,3,2]
# # case = []
# # for i in combinations(weight, 2):
# #     # print(i)  #출력 결과 <class 'tuple'> (1, 3) (1, 2) (1, 3) (1, 2) (3, 2) (3, 3) (3, 2) (2, 3) (2, 2) (3, 2)
# #     # print(i[0]) # 출력결과 : 1 1 1 1 3 3 3 2 2 3
# #     # print(i[1]) # 출력결과 :3 2 3 2 2 3 2 3 2 2
# #     if i[0] != i[1]:
# #         case.append(i)
# # print(len(case)) # 출력결과 : 8

# # 방법 2 ) 
# weight = [1,3,2,3,2]
# case = []
# result = []

# # 반복문을 통해 빈 리스트 case에 원소 넣기 
# for x in range(0,len(weight)): #x=0~4
#     for y in range(1,len(weight)):
#         case.append(weight[x])
#         case.append(weight[y]) 
# # 출력결과 : [1, 3, 1, 2, 1, 3, 1, 2, 3, 3, 3, 2, 3, 3, 3, 2, 2, 3, 2, 2, 2, 3, 2, 2, 3, 3, 3, 2, 3, 3, 3, 2, 2, 3, 2, 2, 2, 3, 2, 2]

# # 반복문을 통해 빈 리스트 result에 원소 묶음(2개씩) 넣기
# for z in range(0,len(case),2): #z=0,2,4
#     result.append(case[z:z+2]) #case[0:2] case[2:4] case[4:6]
# # 출력결과 : [[1, 3], [1, 2], [1, 3], [1, 2], [3, 3], [3, 2], [3, 3], [3, 2], [2, 3], [2, 2], [2, 3], [2, 2], 
# # [3, 3], [3, 2], [3, 3], [3, 2], [2, 3], [2, 2], [2, 3], [2, 2]]

# # 얕은 복사
# answer = result.copy()
# print(answer)

# # # 인덱스 접근 -> 같은 원소를 가진 인덱스값 삭제.
# for i in range(len(answer)): #i=0~19
#     if answer[i][0] == answer[i][1]:
#         del result[i]
# print(len(result)) 

# # ----------------------------------------------------------------------------------------
# # <무지의 먹방 라이브>
