from tkinter import *
import random, string
def clicked():
    global counter           #Нужен как счётчик для количества раз нажатий на кнопку, чтобы я мог заменять надпись, при повторном нажатии
    global title_key                #Нужен, чтобы заменять выведенную уже запись на новую (Ошибку на новый код например)
    flag = 0                 #Нужен будет для проверки состоит ли строка только из заглавных букв (решил заморочиться и добавить проверку на маленькие и большие буквы) :)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    word = txt.get()
    first_block = ''
    second_block = ''
    thirty_block = ''
    key = ''
    if word.isalpha() == True:         #Проверка на то, чтобы в строке были только буквы (да тоже решил заморочиться и сделать проверку на глупого пользователя) :)
        for i in range(3):
            first_block += random.choice(word)
        for i in range(3):
            thirty_block += random.choice(word)
        number_letters = []
        for letter in range(len(word)):
            index_letter = alphabet.index(word[letter]) + 1
            if index_letter > 26:              #Поднимаю флаг если появилась маленькая буква
                flag = 1
            else:
                number_letters.append(index_letter % 10)
        if flag != 1:
            for i in range(6):
                second_block += str(random.choice(number_letters))
        key = first_block + '-' + second_block + '-' + thirty_block
    if counter == 0:
        if word.isalpha() == True and len(word) == 6 and flag != 1:
            title_key = Label(window, text = "Ваш новый ключ: " + key, background="gray19", foreground="white", font = ("Times New Roman", 30))
            title_key.place(relx=0.02, rely=0.8)
        else:
            title_key = Label(window, text = "ОШИБКА! Проверьте корректный ввод слова", background="gray19", foreground="red", font = ("Times New Roman", 30))
            title_key.place(relx=0.02, rely=0.8)
    else:
        if word.isalpha() == True and len(word) == 6 and flag != 1:
            title_key.configure(text="Ваш новый ключ: " + key, background="gray19", foreground="white", font = ("Times New Roman", 30))
        else:
            title_key.configure(text="ОШИБКА! Проверьте корректный ввод слова", background="gray19", foreground="red", font = ("Times New Roman", 30))
    counter += 1
counter = 0
window = Tk()
window.title("Генератор ключа")
window.geometry('1250x700')
window.resizable (width=False, height=False)    #Чтобы нельзя было поменять размер экрана, т.к. поставил как надо по картинке
image_ETS2 =  PhotoImage(file = 'image.png')
window_image = Label(window, image = image_ETS2)
window_image.grid(row=0, column=0)
txt = Entry(window, width=20, font=("Times New Roman", 12))  
txt.place(relx=0.26, rely=0.15)
txt.focus()    #Ставит курсор сразу на поле
title_word = Label(window, text = "Введите 6-ти буквенное слово", background="midnightblue", foreground="white", font = ("Times New Roman", 30))
title_word.place(relx=0.13, rely=0.05)
button = Button(window, text="Enter", width=7, font = ("Times New Roman", 10), bg = "midnightblue", fg = "white", command = clicked)
button.place(relx = 0.36, rely = 0.15)
window.mainloop()     #Чтобы приложение не закрывалось, пока не дадут такую команду