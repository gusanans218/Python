#region 리스트의 인덱싱과 슬라이싱
# a=[1,2,3]
# print(a[0], a[-1])

# a = [1,2,3,['a', 'b', 'c']]
# print(a[-1][0])
#endregion

#region 리스트 수정과 삭제
#수정하기
# a = [1,2,3]
# a[2] = 4
# print(a)

# #삭제하기
# del a[1]
# print(a)
#endregion

#region 리스트 관련 변수
# a = [1,2,3]
# a.append(4)
# print(a)

# a.insert(0,5)
# print(a)
#endregion

#region 튜플
t = (1,2, 'a', 'b')
print(t)

#슬라이싱
print(t[1:])
