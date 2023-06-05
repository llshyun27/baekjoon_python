#5킬로그램 봉지와 3킬로그램 봉지로 옮긴다.
n = int(input())
count =int(0)
count1 = int(0)
if  n % 5 == 0 :   #5로 나눈 나머지가 0이면
    while(n !=0):
        n = n - 5
        count =count+1
    print(count)
   
else : #3과 5를 모두 이용해 나눠진다면
    while n > 0:
      n =n-3
      count += 1
      if n % 5 == 0:
        count1 = n //5
        print(count+count1) 
        break
      elif n == 1 or n == 2:  # 나눠질 수 없음
         print(-1)
         break
      elif n == 0: #3만을 이용해 나눔
         print(count-1)
         break
         

