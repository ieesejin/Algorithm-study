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

# 8. list에서 특정 원소 바꾸기 (대체하기)
list.replace("찾을값", "바꿀값", 바꿀횟수)

바꿀횟수 -> 왼쪽부터 몇번째까지 값을 바꿀것 인가
  
  ex)
  
  text = '1111,2222,3333,4444'
  
  replaceAll= text.replace(",","") # 1111222233334444
  
  replace_t1 = text.replace(",", "",1) # 11112222,3333,4444
  
  replace_t2 = text.replace(",", "",2) # 111122223333,4444
  
  replace_t3 = text.replace(",", "",3) # 1111222233334444
  
# 9. for - else문
else -> for문이 중간에 break 등으로 끊기지 않고, 끝까지 수행 되었을 때 수행하는 코드

테스트 변수를 둬서 확인할 필요가 없다.

주의! : else의 들여쓰기는 for와 일치해야 한다.
  
  ex)
  data = [2, 4, 5, 11, 3]
  for i in data:
	   if i > 10:
		   break
     else:
       print('10 보다 큰 수 없음')
