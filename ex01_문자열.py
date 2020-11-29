### 문자열 ###

# food = 'Python\'s favorite food is perl'
# say =  "\"Python is very easy \" he says"

# ##여러줄의 문자열을 변수에 대입하고 싶을 떄

# multiline = """life is too short\n you need python"""
# print(multiline)


 #region
# # 1. 문자열 연산하기

# head = 'python'
# tail = ' is fun'
# print(head+tail)

# # 2. 문자열 곱하기
# print((head +'\n')*5)

# # 3. 문자열 길이 곱하기
# print(len(head))
 ##endregion


 #region 
# # 1. 문자열 인덱싱
# str = "life is oo short, you need python"
# print(str[3])
# print(str[-1])
# print(str[-2])

# # 2. 문자열 슬라이싱
# print(str[0:4])
# print(str[:6])
# print(str[5:])
# print(str[19: -7])
 #endregion


#region 문자열 포매팅

# print("I eat %d apples." % 3)
# print("I eat %d apples. so I was for %s days." % (3, 'three'))

# #format 함수를 이용한 포매팅
# print("I eat {0} apples" .format(3))
# print("I eat {0} apples. so I was sick for {1} days.")

# f 문자열 포매팅
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다')
#endregion

#region 문자 개수 세기
str = 'hobby'
print(str.count('b'))

#위치 알려주기
str = 'python is the best choice'
print(str.find('b'))
print(str.upper('b'))

# 문자열  나누기
print(str.split())

str2 = 'a:b:c:d'
print(str2.split(':'))


#endregion