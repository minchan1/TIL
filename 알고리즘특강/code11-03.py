import random
## 함수
def selectionSort(ary) :
    n = len(ary)
    for cy in range(0, n-1) :
        minIdx = cy
        for i in range(cy+1, n):
            if (ary[minIdx] > ary[i]):
                minIdx = i
        ary[cy], ary[minIdx] = ary[minIdx], ary[cy]
    return ary

## 전역
dataAry = [ random.randint(10, 99) for _ in range(20)]

## 메인
print('정렬 전 -->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 -->', dataAry)