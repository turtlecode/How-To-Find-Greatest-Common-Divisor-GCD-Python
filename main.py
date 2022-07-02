number1 = int(input("Enter a number :"))
number2 = int(input("Enter a number :"))
number3 = int(input("Enter a number :"))


def solution(number1, number2, number3):
    list1 = []
    list2 = []
    for i in range(1,11):
        if number1 % i == 0:
            list1.append(i)
    for i in range(1,11):
        if number2 % i == 0:
            list1.append(i)
    for i in range(1,11):
        if number3 % i == 0:
            list1.append(i)

    if number1 >= 10 and number2 >= 10 and number3 >= 10:
        for i in range(1,11):
            x = list1[i]
            if x in list1[i+1:]:
                if x not in list2:
                    list2.append(x)

    else:
        for i in range(1,4):
            x = list1[i]
            if x in list1[i+1:]:
                if x not in list2:
                    list2.append(x)
    
    print(max(list2))

solution(number1, number2, number3)