# <큰 수의 법칙 p92>
# 구조파악하기 ] 6+6+6+5+6+6+6+5 => [6+6+6+5] / [6+6+6+5] 일정하게 반복 => [6+6+6][+5] 일정하게 반복
 
# input값 설정
num_list = input("숫자배열을 입력하세요: ")
M = int(input("몇 번을 더할까요?: "))
K = int(input("하나의 수를 최소 몇 번 더할까요?: "))

# 가장 큰 수 구하기
num_list.sort(reverse = True)
first_num = num_list[0]
second_num = num_list[1]

# 반복문
sum=0
while True:
    for i in range(K):
        if M!= 0:
                sum+=first_num      
                M-=1
        else: 
            break               
        print(sum)
                            # 이 부분의 반복문은 가장 큰 수가 반복되는 부분.
                            # 만약 K=4라면,,,
                            # i = 0
                                # sum = 6 / M =4 (앞으로 4번 더 반복)
                            # i = 1
                                # sum = 12 / M =3 (앞으로 3번 더 반복)
                            # i = 2
                                # sum = 18 / M =2 (앞으로 2번 더 반복)
                            # i = 3
                                # sum = 24 / M = 1 (앞으로 1번 더 반복)
                            # i = 4
                                # sum = 6 / M = 0 => break
    if M != 0:
        sum+=second_num      
        M-=1 
    else:
        break    
                            # 이 부분의 반복문은 조건에 의하여 두번째로 큰 값이 반복되는 부분
                 
print(sum)      # 첫번째 반복문과 두번째 반복문의 합
