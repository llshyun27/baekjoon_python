#끊어진 기타줄의 개수 n, 기타줄 브랜드 m
n,m = map(int,input().split())

# 6줄 패키지가격, 1줄 낱개 가격
package =[]
single =[]
for _ in range(m):
    a,b = map(int,input().split())
    package.append(a)
    single.append(b)
    
# n개의 끊어진 기타줄을 바꾸는데 필요한 최소 가격을 구한다.
min_package = min(package)
min_single = min(single)

if (min_package >= min_single*6):
   total = min_single * n
   print(total)
else:
   n1 = n // 6  #패키지의 개수
   total_package= min_package * n1
   n2 = n % 6  # 나머지의 개수
   total_single = min_single * n2
   if total_single <= min_package:
     print(total_package + total_single)
   else:
     print(total_package + min_package)




