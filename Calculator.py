print ("기본기능 계산기 / 나눗셈은 몫밖에 안나옴.")

def a(e, f):
    return e+f

def b(e, f):
    return e-f

def c(e, f):
    return e*f

def d(e, f):
    return e/f

print("--------------------------------------------------------------")
print("1 = 더하기\n2 = 빼기\n3 = 곱하기\n4 = 나누기\n5 = 종료")
print("--------------------------------------------------------------")

while True:
    menu = int(input("원하는 기능을 입력하세요: "))
    if(menu <= 4):
        A = int(input("첫번째 숫자를 입력하세요: "))
        B = int(input("두번째 숫자를 입력하세요: "))
        if(menu == 1):
            result = a(A, B)
            print("결과는 %d 입니다."%result)
        elif(menu == 2):
            result = b(A, B)
            print("결과는 %d 입니다."%result)
        elif(menu == 3):
            result = c(A, B)
            print("결과는 %d 입니다."%result)
        elif(menu == 4):
            result = d(A, B)
            print("결과는 %d 입니다."%result)
        elif(menu == 5):
            break
else:
    print("잘못 입력하셨습니다.")
