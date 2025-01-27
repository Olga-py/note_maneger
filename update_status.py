text2 = '1-"выполнено" 2-"в процессе" 3-"отложено": '
text1 = 'Введите цифру соответствующую статусу заметки, где '
text3 = 'Статус заметки успешно обновлён на'
text4 = 'Введено некорректное значение, пожалуйста повторите ввод'
a = 3
while a < 5:
    try:
        status1 = int(input(text1 + text2))
        if status1 == 1:
            print(text3, text2[2:13])
        if status1 == 2:
            print(text3, text2[16:29])
        if status1 == 3:
            print(text3, text2[31:41])
    except ValueError:
            print(text4)

        #break
        #if status1 < 1 or status1 > 3:
            #print(text4)
    #except ValueError:
    #print(text4)


