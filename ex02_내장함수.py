#파이썬 내장함수는 외부 모듈과 달리 import가 필요없다

#type(object) => 자료형을 알려줌.
print(type("abcd"))
print(type[])

#id(object) => 객체의 주소 값 반환
a = 3
print(id(a))
print(type(a))

#pow(x,y) => x를 y만큼 제곱한 결과 반환
print(pow(3,4),pow(2,3))

#sum(iterable) => 합계 반환
print(sum((1,2,3,4,5)),sum([1,2,3]))

#round(number) => 반올림 수 반환
print(round(4.6))
print(round(4.1))
print(round(3.141592,3))

#eval(계산 가능한 문자열) => 문자열을 계산한 결과값 반환
print(eval('1+2'))

#list(열거형 자료) => 리스트 반환
print(list('python'))
print(list(1,2,3))

#enumerate() => 열거형 자료형
for i, char in enumerate('python'):
    print(i, char)


#filter(함수, 열거형 자료) => 열거형 자료가 주어진 함수에서 실행되었을 때 참인 값만 반환
def positive(n):
    return n>0


#map(함수f, 열거형 자료) => 함수f가 수행한 결과를 반환
def two_times(x):
    return x*2

print(list(map(two_times, [1,2,3,4])))
print(list(map(two_times, [1,2,3,4])))

#sorted(열거형 자료)
print(sorted([3,1,2]))
print(sorted([3,1,2]))