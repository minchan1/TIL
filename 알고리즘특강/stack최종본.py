if __name__ == '__main__':
    select = input("삽입(I), 추출(E), 확인(V), 종료(X) 중 하나를 선택 : ")

    while select != 'X' and select != 'x':
        if select == 'I' or select =='i':
            data = input('입력할 데이터 : ')
            push(data)
            print('스택의 상태 : ', stack)
        elif select == 'E' or select == 'e':
            data = pop()
            print('추출된 데이터 : ', data)
            print('스택의 상태 : ', stack)
        elif select == 'V' or select == 'v':
            data = peek()
            print('확인된 데이터 : ', data)
            print('스택의 상태 : ', stack)
        else :
            print('입력이 잘못됨')
        
        select = input("삽입(I), 추출(E), 확인(V), 종료(X) 중 하나를 선택 : ")

    print('프로그램 종료')
