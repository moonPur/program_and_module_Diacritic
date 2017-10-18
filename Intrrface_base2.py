from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import fileinput
import re
import module
import string
import unicodedata
import nltk
from nltk.corpus import stopwords

#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------- Commands --------------------------------------------------------

def open_file():

    if len(w_for_txt3.get(1.0, END)) > 2:
        showwarning('Warning', 'Файл уже загружен в программу. \n Если хотите загрузить новый файл, \n то отчистите поле «Исходный текст» и «Преобразованный текст» \n через пункт строки меню «Edit».')

    if len(w_for_txt3.get(1.0, END)) < 2:
        op = askopenfilename()
        text = open(op, 'rb').read()
        text1 = text.decode('utf8')   # Декодируем из utf8 в unicode
        w_for_txt.insert(END, text1)


def save_file():
    save_as = asksaveasfilename()
    letter = w_for_txt2.get(1.0, END)
    f = open(save_as, 'w', encoding = 'utf-8')
    f.write(letter)
    f.close()


def quit_from_programm():

    if askyesno('Info', 'Вы сохранили данные перед тем, как покинуть программу?'):
        root.destroy()


def clear_ALL_windows():

    if askyesno('Info', 'Вы уверены, что хотите очистить все окна? \n Несохраненные данные будут потеряны.'):
        w_for_txt.delete(1.0, END)
        w_for_txt2.delete(1.0, END)
        w_for_txt3.delete(1.0, END)
        w_for_txt4.delete(1.0, END)


def clear_w1():

    if askyesno('Info',
                'Вы уверены, что хотите очистить окно «Исходный текст»? \n Для правильной работы программы отчистите окно «Преобразованный текст».'):
        w_for_txt.delete(1.0, END)


def clear_w2():

    if askyesno('Info', 'Вы уверены, что хотите очистить окно «Преобразованный текст»? \n Не сохраненные данные будут потеряны.'):
        w_for_txt2.delete(1.0, END)


def clear_w3():
    w_for_txt3.delete(1.0, END)


def clear_w4():
    w_for_txt4.delete(1.0, END)


def highlight_diac():
    mark_list = ['è', 'à', 'ù', 'é', 'ê', 'â', 'ô', 'î', 'û', 'ë', 'ï', 'ü', 'ÿ', 'ç', 'æ', 'œ','È', 'À', 'Ù', 'É', 'Ê', 'Â', 'Ô', 'Î', 'Û', 'Ë', 'Ï', 'Ü', 'Ÿ', 'Ç', 'Æ', 'Œ', 'Ä', 'ä', 'Ö', 'ö', 'Ü', 'ü', 'ẞ', 'ß']

    for i in range(len(mark_list)):
        start = 1.0
        pattern = mark_list[i]
        pos = w_for_txt.search(pattern, start, stopindex = END)

        while pos:
            length = len(pattern)
            row, col = pos.split('.')
            end = int(col) + length
            end = row + '.' + str(end)
            w_for_txt.tag_add('highlight', pos, end)
            start = end
            pos = w_for_txt.search(pattern, start, stopindex = END)
            print('/n inside, ', pos)
        w_for_txt.tag_config('highlight', background = 'yellow', foreground = 'black')


def show_stop_words_french():
    stop_words = stopwords.words('french')
    stop_words = '\n'.join(stop_words)
    w_for_txt3.insert(END, stop_words)
    if askyesno('Info','Хотите ли вы добавить свои стоп-слова в список, или отредактировать существующий?'):
        showinfo('Info','Введите или удалите слова в окне «Стоп-слова». \n Слова разделять переходами на новую строку (клавиша Enter)')
    else:
        showinfo('Info', 'При нажатии кнопки «Удалить стоп-слова из текста» из «Исходного текста» будут удалены слова, что отображаются в окне «Стоп-слова».')


def show_stop_words_deutsch():
    stop_words = stopwords.words('german')
    stop_words = '\n'.join(stop_words)
    w_for_txt3.insert(END, stop_words)

    if askyesno('Info','Хотите ли вы добавить свои стоп-слова в список, или отредактировать существующий?'):
        showinfo('Info','Введите или удалите слова в окне «Стоп-слова». \n Слова разделять переходами на новую строку (клавиша Enter)ю')
    else:
        showinfo('Info', 'При нажатии кнопки «Удалить стоп-слова из текста» из «Исходного текста» будут удалены слова, что отображаются в окне «Стоп-слова» ')


def delete_stop_words():
    stop_words = w_for_txt3.get(1.0, END)
    stop_words2 = stop_words.title()  # делаем слова с заглавной буквы, чтобы удалить слова, если они стоят в начале предложения, а перед этим их не привели к одному регистру
    stop_words = stop_words + stop_words2
    stop_words = stop_words.split('\n')
    text2 = w_for_txt2.get(1.0, END)
    text = w_for_txt.get(1.0, END)
    if len(text) < 2:
        showwarning('Warning', 'Вы не загрузили файл в программу. \n Пожалуйста сделайте это.')

    if len(text) > 2 and len(stop_words) < 4:
        showwarning('Warning', 'Вы не загрузили в программу стоп-слова \n Пожалуйста сделайте это, нажав кнопку «Показать список стоп-слов ФРАНЦУЗСКОГО языка» \n или «Показать список стоп-слов НЕМЕЦКОГО языка».')

    if len(text) > 2 and len(stop_words) > 3:

            if askyesno('Info', 'Хоти ли вы, чтобы программа удалила из вашего текста стоп-слова из списка в окне «Стоп-слова»? \n'
                        'Нажимая «Нет», Вы можете дополнить/отредактировать список в окне «Стоп-слова».'):

                if len(text) > 2 and len(text2) < 2:
                    text1 = [i for i in text.split() if i not in stop_words]
                    text1 = ' '.join(text1)
                    w_for_txt2.insert(END, text1)

                if len(text) > 2 and len(text2) > 2:
                    text1 = [i for i in text2.split() if i not in stop_words]
                    text1 = ' '.join(text1)
                    w_for_txt2.delete(1.0, END)
                    w_for_txt2.insert(END, text1)


def show_punctuation_mark():
    test_p = w_for_txt4.get(1.0, END)
    punctuation = ' . , : « » – ! ( ) ? ; { } [ ] * & ^ \' | \" _ / % $ # @ № \\ \n Δ Ω α β γ δ ε ζ η θ Ω'

    if len(test_p) < 2:
        w_for_txt4.insert(END, punctuation)

        if askyesno('Info','Хотите ли вы добавить свои символы в список, или отредактировать существующий?'):
            showinfo('Info','Введите или удалите символы в окне «Дополнительные символы». \n Символы разделять пробелами.')
        else:
            showinfo('Info', 'При нажатии кнопки «Убрать пунктуационные знаки и доп. символы» из текста будут удалены символы, что отображаются в окне «Дополнительные символы».')

    if len(test_p) > 2:
        w_for_txt4.delete(1.0, END)
        w_for_txt4.insert(END, punctuation)


def delete_punctuation_mark():
    text = w_for_txt.get(1.0, END)
    text2 = w_for_txt2.get(1.0, END)
    punctuation = w_for_txt4.get(1.0, END)  # знаки берем из четвертого окна
    punctuation = punctuation.split()

    if len(text) < 2:
        showwarning('Warning', 'Вы не загрузили файл в программу. \n Пожалуйста сделайте это.')

    if len(punctuation) < 2:
        showwarning('Warning', 'Вы не загрузили пунктуационные знаки и дополнительные символы в программу. \n Пожалуйста, сделайте это, нажав кнопку «Показать пунктуационные знаки и доп. символы».')

    if len(punctuation) > 2:

        if len(text) > 2 and len(text2) < 2:

            str = module.delete_punctuation(text, punctuation)
            w_for_txt2.insert(END, str)

        if len(text) > 2 and len(text2) > 2:

            str = module.delete_punctuation(text2, punctuation)
            w_for_txt2.delete(1.0, END)
            w_for_txt2.insert(END, str)


def lower_case():
    text = w_for_txt.get(1.0, END)
    text2 = w_for_txt2.get(1.0, END)

    if len(text) < 2:
        showwarning('Warning', 'Вы не загрузили файл в программу. \n Пожалуйста сделайте это.')

    if len(text) > 2 and len(text2) < 2:
        text = text.lower()                                                    # метод позволяющий провести строку к одному регистру, нижнему
        w_for_txt2.insert(END, text)

    if len(text) > 2 and len(text2) > 2:
        text2 = text2.lower()
        w_for_txt2.delete(1.0, END)
        w_for_txt2.insert(END, text2)


def transform_diacritic_french():
    text = w_for_txt.get(1.0, END)
    text2 = w_for_txt2.get(1.0, END)

    if len(text) < 2:
        showwarning('Warning', 'Вы не загрузили файл в программу. \n Пожалуйста сделайте это.')

    if len(text) > 2 and len(text2) < 2:
        french = module.french_diac(text)
        w_for_txt2.insert(END, french)

    if len(text) > 2 and len(text2) > 2:
        french = module.french_diac(text2)  # используем собственноручно написанный модуль
        w_for_txt2.delete(1.0, END)
        w_for_txt2.insert(END, french)


def transform_diacritic_deutsch():
    text = w_for_txt.get(1.0, END)
    text2 = w_for_txt2.get(1.0, END)

    if len(text) < 2:
        showwarning('Warning', 'Вы не загрузили файл в программу. \n Пожалуйста сделайте это.')

    if len(text) > 2 and len(text2) < 2:
        french = module.deutsch_diac(text)
        w_for_txt2.insert(END, french)

    if len(text) > 2 and len(text2) > 2:
        french = module.deutsch_diac(text2)  # используем свой модуль
        w_for_txt2.delete(1.0, END)
        w_for_txt2.insert(END, french)


#------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------END commands-----------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------Create a GENERAL/MAIN  window-----------------------------------
root = Tk()
root.title('Диакритик')
frame1 = Frame(root, background = '#f5fffa')
frame1.grid(row = 0, column = 0)
frame2 = Frame(root, background = '#f5fffa')
frame2.grid(row = 0, column = 1)
# ------- кнопки, располагающиеся справа
button1 = Button(frame2, text='Выделить диакритические знаки',command = highlight_diac, pady = 3, padx = 50, bg = '#f0f8ff')
button1.grid(row = 0, column = 4)
button2 = Button(frame2, text = 'Показать список стоп-слов \n ФРАНЦУЗСКОГО языка',command = show_stop_words_french, pady = 3, padx = 62, bg = '#f8f4ff')
button2.grid(row = 1, column = 4)
button3 = Button(frame2, text = 'Показать список стоп-слов \n НЕМЕЦКОГО языка',command = show_stop_words_deutsch, pady = 3, padx = 62, bg = '#f0f8ff')
button3.grid(row = 2, column = 4)
button4 = Button(frame2, text = 'Удалить стоп-слова из текста', command = delete_stop_words, pady = 3, padx = 58, bg = '#f8f4ff')
button4.grid(row = 3, column = 4)
button5 = Button(frame2, text = 'Показать пунктуационные знаки и доп. символы', command = show_punctuation_mark, pady = 3, padx = 3, bg = '#f0f8ff')
button5.grid(row = 4, column = 4)
button6 = Button(frame2, text = 'Убрать пунктуационные знаки и доп. символы', command = delete_punctuation_mark, pady = 3, padx = 9, bg = '#f8f4ff')
button6.grid(row = 5, column = 4)
button7 = Button(frame2, text = 'Привести текст к одному регистру', command = lower_case, pady = 3, padx = 43, bg = '#f0f8ff')
button7.grid(row = 6, column = 4)
button8 = Button(frame2, text = 'Произвести обработку диакритических знаков \n ФРАНЦУЗСКОГО языка', command = transform_diacritic_french, pady = 3, padx = 8, bg = '#f8f4ff')
button8.grid(row = 7, column = 4)
button9 = Button(frame2, text = 'Произвести обработку диакритических знаков \n НЕМЕЦКОГО языка', command = transform_diacritic_deutsch, pady = 3, padx = 8, bg = '#f0f8ff')
button9.grid(row = 8, column = 4)

#------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------END GENERAL/MAIN  window----------------------------------------

#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------Строка MAIN-меню-------------------------------------------------
menu = Menu(root) #создается объект строки Меню на главном окне
root.config(menu = menu)  #окно конфигурируется с указанием меню для него

file_menu = Menu(menu)
menu.add_cascade(label = 'Файл', menu = file_menu)
file_menu.add_command(label = 'Открыть', command = open_file)
file_menu.add_command(label = 'Сохранить', command = save_file)
file_menu.add_command(label = 'Выйти', command = quit_from_programm)

edit_menu = Menu(menu)
menu.add_cascade(label = 'Правка', menu = edit_menu)
edit_menu.add_command(label = 'Очистить ВСЕ текстовые  поля', command = clear_ALL_windows)
edit_menu.add_command(label = 'Очистить  текстовое поле окна «Исходный текст»', command = clear_w1)
edit_menu.add_command(label = 'Очистить  текстовое поле окна «Стоп-слова»', command = clear_w3)
edit_menu.add_command(label = 'Очистить текстовое поле окна «Дополнительные символы»', command = clear_w4)
edit_menu.add_command(label = 'Очистить текстовое поле окна «Преобразованный текст»', command = clear_w2)

help_menu = Menu(menu)
menu.add_cascade(label = 'Справка', menu = help_menu)
#------------------------------------------------------------------------------------------------------------------
#--------------------------------------END строка MAIN меню--------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#------------------------------------- Описание текстового окна «Исходный текст» ----------------------------------
lbl = Label(frame1, text = 'Исходный текст', background = '#f5fffa', font = 'Arial')
lbl.grid(row = 0, column = 0)

w_for_txt = Text(frame1, width = 40, height = 15, font = '12')
vscrollbar = Scrollbar(frame1, orient = 'vert', command = w_for_txt.yview)
w_for_txt['yscrollcommand'] = vscrollbar.set
w_for_txt.grid(row = 1, column = 0, sticky = 'nsew')
vscrollbar.grid(row = 1, column = 1, sticky = 'ns')
frame1.rowconfigure(0, weight = 1)
frame1.columnconfigure(0, weight = 1)
#------------------------------------------------------------------------------------------------------------------
#----------------------------------END описание текстового окна «Исходный текст»-----------------------------------

#------------------------------------------------------------------------------------------------------------------
#-------------------------------Описание текстового окна «Преобразованный текст»-----------------------------------
lb2 = Label(frame1, text = 'Преобразованный текст', background = '#f5fffa', font = 'Arial')
lb2.grid(row = 0, column = 2)

w_for_txt2 = Text(frame1, width = 40, height = 15, font = '12')
w_for_txt2.grid(row = 1, column = 2, sticky = 'nsew')
vscrollbar = Scrollbar(frame1, orient = 'vert', command = w_for_txt2.yview)
w_for_txt2['yscrollcommand'] = vscrollbar.set
vscrollbar.grid(row = 1, column = 3, sticky = 'ns')
#-----------------------------------------------------------------------------------------------------------------
#---------------------------------END текстового окна «Преобразованный текст»-------------------------------------

#-----------------------------------------------------------------------------------------------------------------
#-----------------------------------------Описание окна «Стоп-слова»----------------------------------------------
lb3 = Label(frame1, text = 'Cтоп-слова', background = '#f5fffa', font = 'Arial')
lb3.grid(row = 2, column = 0)

w_for_txt3 = Text(frame1, width = 50, height = 10, font = '12')
w_for_txt3.grid(row=3, column = 0, sticky = 'nsew')
vscrollbar = Scrollbar(frame1, orient = 'vert', command = w_for_txt3.yview)
w_for_txt3['yscrollcommand'] = vscrollbar.set
vscrollbar.grid(row = 3, column = 1, sticky = 'ns')
#------------------------------------------------------------------------------------------------------------------
#----------------------------------------END описание окна «Стоп-слова»--------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------Описание окна «Дополнительные символы»----------------------------
lb4 = Label(frame1, text = 'Дополнительные символы', background = '#f5fffa', font = 'Arial')
lb4.grid(row = 2, column = 2)

w_for_txt4 = Text(frame1,width = 50, height = 10, font = '12')
w_for_txt4.grid(row = 3, column = 2, sticky = 'nsew')
vscrollbar = Scrollbar(frame1, orient = 'vert', command = w_for_txt4.yview)
w_for_txt4['yscrollcommand'] = vscrollbar.set
vscrollbar.grid(row = 3, column = 3, sticky = 'ns')
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------END описание окна «Дополнительные символы»------------------------

root.mainloop()   # the end of program (создание окна)
