n1 = int(input("현재 소유한 현금은 얼마입니까? :"))

n2 = input("카드를 소유하고 있습니까? yes/no :")


if n1 >= 4000 or n2 == "yes" or n2 == "Yes":
    print("택시를 탈 수 있다.")
else:
    print("택시를 탈 수 없다.")
