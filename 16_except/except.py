# print(10/0)

try:
    print(10/0)
except:
    print("예외 발생!!")

try:
    num = int(input("숫자를 입력해주세요:"))
    print(10/num)
except ValueError: # 값 데이터 오류
    print("문자 말고 숫자를 넣어주세요.")
except ZeroDivisionError:
    print("0말고 다른 숫자를 넣어주세요.")