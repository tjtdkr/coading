#vacation 입력시 방학동안 할 일 출력
#vacation = 방학
#MK.1 - while 사용

x = input("글자입력:")
vacnum = 0

while True:
    if (x == "vacation"):
        print("1")
        vacnum = vacnum + 1
        if vacnum == 10:
            break