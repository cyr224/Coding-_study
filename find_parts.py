def binary_search(array, target, start, end): #이진 탐색 소스코드 구현(반복문)
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target: #찾은 경우 중간점 인덱스 반환
             return mid
        elif array[mid] > target: #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
            end = mid - 1
        else: #중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
            start = mid + 1
        return None 

n = int(input()) #N(가게의 부품 개수) 입력
array = list(map(int, input().split())) #가게에 있는 전체 번호를 공백으로 구분하여 입력
array.sort() #이진 탐색을 수행하기 위해 사전에 정렬 수행

m = int(input()) #M(손님이 확인 요청한 부품 개수) 입력
x = list(map(int, input().split())) #손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력

for i in x: #손님이 확인 요청한 부품 번호를 하나씩 확인
    result = binary_search(array, i, 0, n - 1) #해당 부품이 존재하는지 확인
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')



    