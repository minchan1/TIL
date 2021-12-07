# 03장 연습문제



## Q1

- 다음 코드의 결과값은 무엇일까?

- ```python
  a = "Life is too short, you need python"
  
  if "wife" in a: print("wife")
  elif "python" in a and "you" not in a: print("python")
  elif "shirt" not in a: print("shirt")
  elif "need" in a: print("need")
  else: print("none")
  ```

- ```python
  # if문 : wife가 a에 없으니 출력 x
  # elif문 1 : python은 있지만 you가 없으니 출력 x
  # elif문 2 : shirt가 a에 없으므로 문자열 shirt가 출력 O
  # elif문 3 : elif문 2가 이미 출력 되었으므로 실행되지 않음. 출력 x
  # else : elif문 2가 이미 출력 되었으므로 실행되지 않음. 출력 x
  답 : shirt
  ```

- 



## Q2

- while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

- ```python
  s = 0
  n = 1
  while n-1000 :
      if not n%3==0 :
          n += 1
      if n%3==0 :
          s = s+n
          n += 1
  print(s)        
  # 답 : 166833
  ```

- 







## Q3

- while문을 사용하여 다음과 같이 별(`*`)을 표시하는 프로그램을 작성해 보자.

- ```
  *
  **
  ***
  ****
  *****
  ```

- ```python
  n = 1
  while n-6 :
      print('*' * n,end='\n')
      n += 1
  ```

- 





## Q4

- for문을 사용해 1부터 100까지의 숫자를 출력해 보자.

- ```python
  for i in range(1,101) :
      print(i)
  ```

- 





## Q5

- A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.

  [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

  for문을 사용하여 A 학급의 평균 점수를 구해 보자.

- ```python
  a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
  n = 0
  m = int(len(a))
  for i in a :
      n += i
  print(int(n/m))    
  ```

- 







## Q6

- 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.

- ```python
  numbers = [1, 2, 3, 4, 5]
  result = []
  for n in numbers:
      if n % 2 == 1:
          result.append(n*2)
  ```

- 위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.

- ```python
  numbers = [1, 2, 3, 4, 5]
  result = [2*i for i in numbers if i%2==1]
  ```

- 

















