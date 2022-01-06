import random
## 이진 검색
## 함수
def binSearch(ary, fData):
    pos = -1
    start = 0
    end = len(ary)-1
    while start <= end:
        mid = (start+end) // 2
        if fData == ary[mid] :
            return mid
        elif fData > ary[mid] :
            start = mid+1   
        else :
            end = mid-1
    return pos

## 전역
dataAry = [ random.randint(1, 999) for _ in range(50)]
findData = dataAry[random.randint(0,49)]
dataAry.sort()

## 메인
print('배열 -->', dataAry)
position = binSearch(dataAry, findData)
if position == -1 :
    print(findData, ' 없어요ㅠㅠ')
else :
    print(findData, '는', position, '위치에 있어요')