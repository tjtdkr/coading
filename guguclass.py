#반응형 구구클래스-thanks to facebook 생활코딩
#edited by tjtdkr(Jang)
while True:
    print("구구단 전체는 1번, 특정 단을 보려면 2번을 누르십시오")
    select = int(input("번호를 입력하세요: "))
    if(select == 1):
        for x in range(2, 10):
            for y in range(1, 10):
                print("%d X %d = %d" %(x, y, x * y))
    elif(select == 2):
        a = int(input("구구단을 보고 싶은 숫자를 입력하세요: "))
        n = 0
        while n < 9:
            n = n + 1
            multiple = a * n
            print("%d X %d = %d" %(a, n, multiple))
    else:
        print("잘못 입력하셨습니다.")