# 주석 처리 (컨트롤 + /)

# 변수
# => 어떠한 값들을 상자에 담아 이름을 붙이는 것

# 변수 => 문자열
last_name = "이"
print("제 성은 " + last_name)
first_name = "정민"
name = last_name + first_name # 문자열과 문자열은 더할 수 있다.
print(name)

# a = name - last_name # 문자열에서 뺄셈은 할 수 없다.
b = name * 3 # 문자열을 곱할 수 있다. 단, 나누기는 할 수 없다.
print(b)

# 변수 => 정수
age = 23
# 변수 => 실수
pie = 3.141592

# 변수 => 여러줄을 문자열로 쓸 때,
str1 = """
안녕하세요.
반갑습니다.
"""

str2 = '''
안녕하세요.
반갑습니다.
'''
print(str1)

num1 = 2.1
num2 = 4.2
print(num1 + num2) # 그래서 어떻게 바르게 계산을 할 수 있는가?
"""
컴퓨터는 이진수만 저장을 하게 되는데 소수는 정확하게 떨어지는 이진법으로 저장이 불가능하다.
그래서 근사값을 저장하고 연산을 하게 되면서 실제의 값보다 아주 조금 더 크게 나온다.
"""

# boolean
"""
참과 거짓의 변수는 is or has or can 등을 앞에 붙이는게 좋다.
부정은 보통 쓰지 않는다.
"""
is_mz = True
is_empty = False
str3 = "python" # True
str4 = "" # False

# 실습
# 내 정보 출력해보기

name1 = "이정민"
age1 = 23
weight = 44.5
is_university = True

print("제 이름은 " + name1)
print("제 나이는", age1)
print("제 몸무게는", weight)
print("저는 대학교를 다니고 있을까요? ", is_university)

# 강사님의 실습
my_name = "이정민"
my_age = 23
my_weight = 44.5
is_male = False
print("제 이름은 " + my_name)
print("제 나이는", my_age) # ,는 공백을 포함한다.
print("제 몸무게는", my_weight) # 문자열을 출력 하는게 아닐 땐 +가 아니라 ,로 적는다.
print("남자 인가요? :", is_male)

# 한번에 print 할 때, (변수를 print에 넣을 때)
print(f"제 이름은 {my_name}, 제 나이는 {my_age} \n제 몸무게는 {my_weight}, 남자 인가요? : {is_male}") # \n은 줄바꿈이다.

str5 = "\"안녕하세요\"" # \"는 문자열 안에 "를 표현하기 위함이고, \t는 네 칸의 공백을 표현하기 위함이다.
print(str5)

# 출력할 때, 변수를 넣는 것이 정수도 가능하다.
num3 = 10
num4 = 20
print(f"num1 + num2 = {num3 + num4}")