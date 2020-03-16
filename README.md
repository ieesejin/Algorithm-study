# Algorithm-study
Programmers Algorithm practice page

# 1. 두 정수 사이의 합
if a>b: a, b = b, a // a, b 대소비교를 위해서 
sum(range(a,b))


# 2. 문자열 리스트에서 문자열의 n번째 인덱스를 이용해서 정렬
sorted(a, key=lambda x: x[n])


# 3. 문자열 집계
str.lower() // 소문자로 바꾸기
str.count('p')

from collections import Counter
c=Counter(str)
c['p']


# 4. join()
x=['a', 'b', 'c', 'd']
''.join(x) --> abcd
'/'.join(x) --> a/b/c/d


# 5. 문자열이 정수인지 확인하는 함수
str.isdigit() --> return True or False


# 6. format을 이용한 print
print("김서방은 {}에 있다".format(1))


# 7. list에서 특정 원소 인덱스 찾기
list.index('찾고싶은 것')
