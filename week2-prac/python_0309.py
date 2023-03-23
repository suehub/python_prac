Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import keyword
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
for=1
SyntaxError: invalid syntax
for_=1
print(for_)
1
weight=100
weight
100
print(weight)
100
weight=50
print(weight)
50
// 코드 클릭하고 엔터하면 불러오기 가능
SyntaxError: invalid syntax
type(weight)
<class 'int'>
weight=50.5
type(weight)
<class 'float'>
## 코드 클릭하고 엔터하면 불러오기 가능
## type은 자료형을 알려줌






## int : 정수형, float : 부동소수점(실수), str : 문자열, bool : 불린, list : 다중 데이터형, tuple : 추가삭제수정 불가능한 리스트, dic : '키:값'구조의 자료형, set : 순서 상관없이 나열한 집합










## 파이썬 자료형은 동적으로 변함.
weight = "Lee"
type(weight)
<class 'str'>
print(weight)
Lee

weight = Lee
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    weight = Lee
NameError: name 'Lee' is not defined. Did you mean: 'len'?
>>> Lee=65
>>> weight = Lee
>>> weight
65
>>> print(Lee)
65
>>> print("Lee")
Lee
>>> print(65)
65
>>> 65 = weight
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> 
>>> 
>>> 
>>> w = 163
>>> w = 48
>>> h = 1.63
>>> BMI = w / h * h
>>> print(BMI)
48.0
>>> BMI = w / (h * h)
>>> print(BMI)
18.06616733787497
>>> bmi = w / (h ** 2)
>>> print(bmi)
18.06616733787497
>>> bmi = w / h ** 2
>>> print(bmi)
18.06616733787497
