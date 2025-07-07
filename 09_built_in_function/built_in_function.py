# 내장함수
# 파이썬에서 기본적으로 지원 하는 함수(Built-in Function)

# abs()
# 숫자의 절댓값을 리턴 하는 함수
print(abs(-10))
print(abs(-1.2))

# all()
# all(x)는 반복 가능한 데이터 x를 입력 값으로 받으면
# 이 x의 요소가 모두 참이면 True, 거짓이 하나 라도 있으면 False를 리턴
# 모든 요소가 참이가?
num_list = [1, 2, 0, 4] # 0은 False, 그 외의 숫자는 전부 True
print(all(num_list)) # 모든 요소가 참이 아니 기에 False
num_list = [] # 빈 리스트는 불리언 타입 으로 봤을 때, False
print(all(num_list))
# 빈 리스트 같은 경우, 안에 어떤 요소도 존재 하지 않는다.
# 따라서 "거짓인 요소가 하나 라도 있는가?" => "거짓인 요소가 없다."
# 거짓인 요소가 없기 때문에 모든 요소가 참 이라는 조건이 위배 되지 않는다.

# any()
# any(x)는 반복 가능한 데이터 x를 입력 값으로 받으면
# 이 x의 요소가 하나 라도 참이면 True, 요소가 모두 거짓 이면 False
num_list = [1, 2, 0, 4]
print(any(num_list))
num_list = [0, 0, 0, 0]
print(any(num_list)) # 모두 거짓 이기에 False

# chr()
# chr(i)는 유니코드를 넣으면 해당 문자로 리턴을 하는 함수
print(chr(97)) # a
print(chr(44032)) # 가

# dir
# 객체가 지닌 변수나 함수를 보여 주는 함수
name = "pyton"
print(dir(name))

# divmod()
# 2개의 숫자 a, b를 입력 받고 a를 b로 나눈 몫과 나머지를
# 튜플 형태로 리턴
print(divmod(7,3))

# enumerate()
# 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력 받아서 인덱스 값을
# 포함 하는 enumerate 객체를 리턴
# 인덱스와 값을 두개의 변수로 언팩
a_list = ["name", "age", "birth"]

for i, value in enumerate(a_list):
    print(f"{i + 1}. {value}")

# eval()
# 문자열로 구성 되어 있는데 해당 문자열을 실행한 값
a_str = "1 + 2"
print(eval(a_str))
print(eval("divmod(7,2)"))

# filter()
# 첫번째 인수로 함수, 두번째 인수로 반복 가능한 데이터
# 그리고 반복 가능한 데이터의 요소 순서 대로 함수를 호출 했을때,
# 리턴 값이 참 인것만 묶어서 리턴
def postive(x):
    return x > 0

print(list(filter(postive, [1, -2, 5, -3, 8])))

# hex()
# 정수를 입력 받아 16진수 문자열로 변환 하여 리턴 하는 함수
print(hex(234))
print(hex(12))

# id()
# 객체를 입력 받아서 고유 주소값(reference)를 리턴 하는 함수
a = 3
print(id(a))

# map()
# map은 입력 받은 데이터의 각 요소에 함수를 적용한 결과를
# 리턴 하는 함수
def two_time(x):
    return x * 2

print(list(map(two_time, [1, 2, 3, 4])))

# max()
# 반복 가능한 데이터 중에서 최댓값을 리턴
num_list = [1, 2, 13, 15, 23, 18, 55, 17, 46]
print(max(num_list))

# min()
# 반복 가능한 데이터 중에서 최솟값을 리턴
print(min(num_list))

# oct()
# oct()는 정수를 8진수 문자열로 바꾸어 리턴하는 함수
print(oct(34))
print(oct(12345))

# open()
# open(파일 이름, 모드)은 파일 이름과 모드를 입력 받아
# 파일 객체를 리턴 하는 함수
# w 쓰기 모드
# r 읽기 모드
# a 추가 모드
file = open("예시.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()

with open("예시.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# ord() <=> chr()
# ord()는 문자의 유니코드 숫자 값을 리턴 하는 함수
print(ord("가"))
print(ord("a"))

# pow()
# 첫번째 인수의 두번째 인수만큼 거듭제곱 한 값을 리턴
print(pow(3, 10))
print(pow(2, 10))

# range()
# range(시작, 끝, 간격) for문과 함께 자주 사용
# 반복 가능한 객체로 만들어서 리턴
print(list(range(5, 100, 5)))

# round()
# 반올림
print(round(4.4))
print(round(8.9))
print(round(5.1284, 2))

# sum()
# 합계를 구하는 함수
num_list = [123, 5820, 475, 863]
print(sum(num_list))

# 실습

# 내가 한 실습
data = ["apple", "banana", "cherry", "grape", "mango", "blueberry", "lemon"]

for i, value in enumerate(data):
    print(f"{i + 1}. {value}")

# 강사님이 한 실습
for i, item in enumerate(data):
    print(f"{i + 1}. {item}")

# 출력되어야 하는 값
# 1. apple
# 2. banana


# 인덱스가 짝수인 요소만 출력(인덱스: 요소)
data = [1, -2, 5, -3, 8]
for index, value in enumerate(data):
    if index % 2 == 0:
        print(f"{index}: {value}")