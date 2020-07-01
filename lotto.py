import random

print("로또 번호 생성기")
num = int(input("게임수 입력 :"))

for i in range(0, num):
    lotto = random.sample(range(1, 46), 6)
    lotto.sort()
    print(lotto)