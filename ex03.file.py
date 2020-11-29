#6. 파일 전체 내용 읽기
f = open('새파일.txt','r', encoding='urf-8')
print(f.read())
f.close()

#7.with문 사용(자동으로 파일 닫기)
with open('새파일.txt','r', encoding='urf-8') as f:
    print(f.read())