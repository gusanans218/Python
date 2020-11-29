#딕셔너리 추가하기
a = {1: 'a'}
a[2]= 'b'
print(a)

a['name'] = 'dongyun'
print(a)

a[3] = [1,2,3]
print(a)

#key값으로 value값 가져오기
print(a[1], a['name'], a[3])

#region 딕셔너리 함수
print(a.keys())

for k in a.keys():
    print(k, end=' ')
print()
print(list(a.keys()))

print(a.values())

print(a.items())

#모두 지우기
a.clear()
print(a)

#key값으로 value값 얻기
print(a.get('name'))
