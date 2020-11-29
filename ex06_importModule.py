# print("모든 약수를 프린트합니다")
# a = int(input("n= "))
# for i in range(1, a+1):
#     if a % i == 0:
#         print(i, end= '')


def sum_digit(number):
    result = 0    #result값을 사용하기위해 초기화
    for i in str(number): #str(변수) 글자를 문자형으로 변환
        result = result + int(i) #문자형으로 각자 나눈 숫자를 더하기 위하여 정수형으로 변환하여 덧셈
    return result    #계산이 끝났으니 result값 
 


