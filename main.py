from tkinter import Label, Tk, PhotoImage, Entry, Button
import random, string

def new_key(text):
    flag = 0
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    first_block = ''
    second_block = ''
    thirty_block = ''
    key = ''
    if text.isalpha():         
        for i in range(3):
            first_block += random.choice(text)
        for i in range(3):
            thirty_block += random.choice(text)
        number_letters = []
        for letter in range(len(text)):
            index_letter = alphabet.index(text[letter]) + 1
            if index_letter > 26:              
                flag = 1
            else:
                number_letters.append(index_letter % 10)
        if flag != 1:
            for i in range(6):
                second_block += str(random.choice(number_letters))
        key = first_block + '-' + second_block + '-' + thirty_block
    return key, flag

def clicked():  
    global COUNTER
    global TITLE_KEY                        
    word = txt.get()
    key, flag = new_key(word)
    
    if COUNTER == 0:
        if word.isalpha() and len(word) == 6 and flag != 1:
            TITLE_KEY = Label(window, text="Ваш новый ключ: " + key,
                              background="gray19", foreground="white", font=("Times New Roman", 30))
            TITLE_KEY.place(relx=0.02, rely=0.8)
        else:
            TITLE_KEY = Label(window, text="ОШИБКА! Проверьте корректный ввод слова", 
                              background="gray19", foreground="red", font=("Times New Roman", 30))
            TITLE_KEY.place(relx=0.02, rely=0.8)
    else:
        if word.isalpha() and len(word) == 6 and flag != 1:
            TITLE_KEY.configure(text="Ваш новый ключ: " + key, background="gray19", 
                                foreground="white", font=("Times New Roman", 30))
        else:
            TITLE_KEY.configure(text="ОШИБКА! Проверьте корректный ввод слова", 
                                background="gray19", foreground="red", font=("Times New Roman", 30))
    COUNTER += 1

COUNTER = 0

window = Tk()
window.title("Генератор ключа")
window.geometry('1250x700')
window.resizable (width=False, height=False)

image_ETS2 = PhotoImage(file='image.png')
window_image = Label(window, image=image_ETS2)
window_image.grid(row=0, column=0)

txt = Entry(window, width=20, font=("Times New Roman", 12))  
txt.place(relx=0.26, rely=0.15)
txt.focus() 

title_word = Label(window, text="Введите 6-ти буквенное слово", background="midnightblue", foreground="white", font=("Times New Roman", 30))
title_word.place(relx=0.13, rely=0.05)

button = Button(window, text="Enter", width=7, font=("Times New Roman", 10), bg="midnightblue", fg="white", command=clicked)
button.place(relx = 0.36, rely = 0.15)

window.mainloop()     