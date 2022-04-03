#импорт нужный функций
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QRadioButton,QLabel,QVBoxLayout,QHBoxLayout,QMessageBox,QPushButton,QGroupBox,QButtonGroup,QLineEdit,QTextEdit,QListWidget,QInputDialog
import json
#создание приложения
app=QApplication([])
win=QWidget()
#создание функций
def show_note():
    name = list_of_note.selectedItems()[0].text()
    text_window.setText(notes[name]['текст'])
    list_of_tags.clear()
    list_of_tags.addItems(notes[name]['теги'])
def add_note():
    note_name, ok=QInputDialog.getText(win,"Добавить заметку","Название заметки:")
    if ok and note_name != "":
        notes[note_name]={'текст': "", "теги":[]}
        list_of_note.addItem(note_name)
def save_note():
    if list_of_note.selectedItems():
        name = list_of_note.selectedItems()[0].text()
        text=text_window.toPlainText()
        notes[name]['текст']=text
        with open("file.json",'w') as file:
            json.dump(notes, file)
def del_note():
    if list_of_note.selectedItems():
        name = list_of_note.selectedItems()[0].text()
        del notes[name]
        list_of_tags.clear()
        list_of_note.clear()
        text_window.clear()
        list_of_note.addItems(notes)
        with open("file.json",'w') as file:
            json.dump(notes, file)
def add_tag():
    if list_of_note.selectedItems():
        name = list_of_note.selectedItems()[0].text()
        tag=text_line.text()
        if tag != '' and not tag in notes[name]['теги']:
            notes[name]['теги'].append(tag)
            list_of_tags.addItem(tag)
            with open("file.json",'w') as file:
                json.dump(notes, file)
            text_line.clear()
def del_tag():
    if list_of_note.selectedItems() and list_of_tags.selectedItems():
        name = list_of_note.selectedItems()[0].text()
        tag= list_of_tags.selectedItems()[0].text()
        notes[name]['теги'].remove(tag)
        list_of_tags.clear()
        list_of_tags.addItems(notes[name]['теги'])
        with open("file.json",'w') as file:
            json.dump(notes, file)
def search_tag():
    tag=text_line.text()
    if but_search_tag.text() == 'Искать по тегу'and tag !='':
        notes_filtred = {}
        for note in notes:
            if tag in notes[note]['теги']:
                notes_filtred[note]=notes[note]
        but_search_tag.setText('Сбросить поиск')
        list_of_tags.clear()
        list_of_note.clear()
        list_of_note.addItems(notes_filtred)
    elif but_search_tag.text() == 'Сбросить поиск':
        text_line.clear()
        list_of_tags.clear()
        list_of_note.clear()
        list_of_note.addItems(notes)
        but_search_tag.setText('Искать по тегу')
#создание кнопок
but_create=QPushButton('Создать заметку')
but_delete=QPushButton('Удалить заметку')
but_save=QPushButton('Сохранить заметку')
but_add_tag=QPushButton('Добавить к заметке')
but_delele_tag=QPushButton('Открепить от заметки')
but_search_tag=QPushButton('Искать по тегу')
#создание списков
list_of_note=QListWidget()
list_of_tags=QListWidget()
#создание текстов
text1=QLabel('Cписок заметок')
text2=QLabel('Cписок тегов')
#Создание текстового окна
text_window=QTextEdit()
#создание строки для поиска тегов
text_line=QLineEdit()
text_line.setPlaceholderText('Введите тег')
#создание направляющи
mainline=QHBoxLayout()
dopline=QVBoxLayout()
#привязка 
mainline.addWidget(text_window)
mainline.addLayout(dopline)
dopline.addWidget(text1)
dopline.addWidget(list_of_note)
dopline.addWidget(but_create)
dopline.addWidget(but_delete)
dopline.addWidget(but_save)
dopline.addWidget(list_of_tags)
dopline.addWidget(text_line)
dopline.addWidget(but_add_tag)
dopline.addWidget(but_delele_tag)
dopline.addWidget(but_search_tag)
win.setLayout(mainline)
#создание словаря
notes={'имя заметки':{"текст":"текст заметки","теги":["тег1","тег2"]}}
#with open("file.json",'w') as file:
#    json.dump(notes, file)
#чтение файла
with open("file.json",'r') as file:
    notes=json.load(file)
list_of_note.addItems(notes)
#привязка действий
list_of_note.itemClicked.connect(show_note)
but_create.clicked.connect(add_note)
but_save.clicked.connect(save_note)
but_delete.clicked.connect(del_note)
but_add_tag.clicked.connect(add_tag)
but_delele_tag.clicked.connect(del_tag)
but_search_tag.clicked.connect(search_tag)
#запуск
win.show()
app.exec_()