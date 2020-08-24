n = int(input())

array = list(map(int, input().split())) #모든 식량 정보 입력받기
#import sys
#sys.stdin.readline().rstrip()

d = [0] * 100 #앞서 계산된 결과를 저장하기 위한 테이블 초기화

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])
