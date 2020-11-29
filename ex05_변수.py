#변수가지정한 메모리 주소값 확인하기
a = [1,2,3]
print(id(a))

#얇은 복사
b = a
print(id(b))


b.append(4)
print(a,b)
print(f'a==b : {a==b}')

#깊은 복사
# a = [1,2,3]
# b = a[:]
# print(f'a==b')

#region 변수를 만드는 여러가지 방법
a, b = ('python', 'life')
print(a,b)

a,b = 'node', 'js' 
print(a,b) 

