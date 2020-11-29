##파이썬 예외 처리
#1. 에러가 발생하는 경우 프로그램은 중지됨
n = 4/0

#region try, except문 기본 구조
#try:
 #오류가 날 것 같은 실행 문장
  #except 발생 에러 as 변수 :
  #pass

#try ~ except문을 통해 에러가 발생해도 프로그램
try:
    n = 4/0
except:
    pass #아무것도 안하고 넘어감

#3. zeroDivisionError 예외 처리
try:
    n = 4/0
except ZeroDivisionError as err:
    print(f"0으로 나눌 수 없습니다:(err)")

#4.IndexError 예이ㅚ 처리
try:
    a = []
    a[0] = 100
except ZeroDivisionError as err:
    print(f"인덱스 에러 발생 :(err)")


#5. Exception 예외 처리
try:
    a = []
    a[0]=100
    n= 4/0
except Exception as err:
    print(f"에러 발생 :{err}")

#6.try - excep - finally
#에러의 발생 여부에 상관없이 실행해야되는 코드를 
try:
    f = open('readme.txt','r','urf-8')
    except Exception as err:
        print(f'에러 발생: {err}')
finally:
    print('finally 구문 실행')

#7. 여러개의 오류 처리
try:
    4/0
    a = [1,2]
    print(a[3])
except ZeroDivisionError as err:
    print('ZeroDivisionError 발생')
except IndexError as arr:
    print('IndexError 발생')
except Exception as err:
    print('Exception 발생')