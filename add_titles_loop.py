list1 = []
while True:
    title = input('Введите заголовок заметки/Если заметок нет введите "стоп": ')
    list1.append(title)
    if title == "стоп" :
        break
print(*list1[0:-1], sep="\n")