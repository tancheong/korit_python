# print(10/0)

# try:
#     print(10/0)
# except:
#     print("예외 발생!!")

# try:
#     num = int(input("숫자를 입력해주세요:"))
#     print(10/num)
# except ValueError: # 값 데이터 오류
#     print("문자 말고 숫자를 넣어주세요.")
# except ZeroDivisionError:
#     print("0말고 다른 숫자를 넣어주세요.")

# IndexError, ValueError
# try:
#     my_list = [1, 2, 3]
#     index = int(input("리스트에서 가져올 인덱스 : "))
#     print(my_list[index])
# except ValueError:
#     print("숫자만 입력하세요.")
# except IndexError:
#     print("그런 인덱스는 없습니다.")

# 파일 입출력 예외 처리: FileNotFoundError
# file = None
# try:
#     file = open("hi.txt", "r", encoding="utf-8")
#     content = file.read() # 파일의 내용을 읽어 온다.
#     print(content)
# except FileNotFoundError:
#     print("그런 파일은 없습니다.")
# finally:
#     if file is not None and not file.closed:
#         file.close()
#         print("정상적으로 파일이 닫혔습니다.")
#     elif file is None:
#         print("애초에 열리지 않았습니다.")

# 리스트 요소 5개 선언하고 index로 찾는 로직
# IndexError, ValueError 예외 처리
# 정상적이면 해당 리스트 값 출력 else
# 마지막은 항상 끝!! 출력 finally
# try:
#     color_list = ["red", "blue", "orange", "black", "yellow"]
#     index_input = input("인덱스를 입력하세요:")
#     index = int(index_input)
#     result = color_list[index]
# except IndexError as message:
#     print("해당 인덱스가 없습니다.")
#     print(message)
# except ValueError as message:
#     print("숫자를 입력해주세요.")
#     print(message)
# else:
#     print(f"해당 인덱스의 값 : {result}")
# finally:
#     print("끝!!")

# raise 키워드 : 강제로 예외 발생
# 특정 조건에서 개발자가 직접 예외를 발생시키는데 사용
# try:
#     age = int(input("나이를 입력하세요 : "))
#
#     if age < 0 or age > 150:
#         raise Exception("0이상 150미만 숫자만 입력해주세요:")
# except Exception as e:
#     print(e)
# else:
#     print(f"입력된 나이 : {age}")
# finally:
#     print("끝!!")

# 사용자 정의 예외 클래스
# class AgeException(Exception):
#     def __init__(self):
#         super().__init__("0이상 150미만 숫자만 입력하세요.")
#
# try:
#     age = int(input("나이를 입력하세요 : "))
#
#     if age < 0 or age > 150:
#         raise AgeException()
# except AgeException as e:
#     print(e)
# else:
#     print(f"입력된 나이 : {age}")
# finally:
#     print("끝!!")

# 출금을 할 때, 잔액이 부족하면 발생되는 예외
# FundsError => 잔액이 부족합니다. 현재 잔액 : ***원, 출금 시도 금액 ***원
# Account 클래스 만들고 메소드 withdraw 출금
# 출금을 할 때, 잔액이 부족하면 FundsError를 발생
# class FundsError(Exception):
#     def __init__(self, balance, amount): # 생성자에서 현재 잔액과 출금 시도 금액을 받습니다.
#         super().__init__(f"잔액이 부족합니다. 현재 잔액 : {balance}원, 출금 시도 금액 {amount}원")
#
# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance
#
#     def withdraw(self, amount):
#         try:
#             if amount > self.balance:
#                 raise FundsError(self.balance, amount)
#         except FundsError as e:
#             print(e)
#         else:
#             self.balance -= amount
#             print(f"정상적으로 출금 되었습니다. 남은 잔액 {self.balance}")
#
# account1 = BankAccount(100000)
# account1.withdraw(50000)
# account1.withdraw(80000)

# 딕셔너리 요소 찾기
# 딕셔너리 키를 입력 받음(숫자로)
# result 변수에 해당 키의 값을 넣음
# 예외 처리 => 해당 키가 존재 하지 않을 때 "KeyError" 처리: "해당 키는 존재 하지 않습니다." 출력
# 숫자가 아닌 문자를 입력 했을 때, "ValueError" 처리: "숫자를 입력해 주세요" 출력
# 정상적으로 실행 된다면 해당 키의 값을 넣어둔 result 출력
# 마지막은 항상 "완료!!"를 출력
my_dict = {
    1: "apple",
    2: "banana",
    3: "cherry",
    4: "durian",
    5: "blueberry"
}

try:
    key = int(input("키(숫자)를 입력하세요: "))
    result = my_dict[key]
except KeyError:
    print("해당 키가 존재 하지 않습니다.")
except ValueError:
    print("숫자를 입력해주세요.")
else:
    print(result)
finally:
    print("완료!!")