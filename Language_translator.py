from gettext import translation
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from translate import Translator

Screen = Tk()


Screen.title("Language Translator - Ajay")


Screen.geometry("919x847")


upload= Image.open("3.jpg")
image=ImageTk.PhotoImage(upload)
label= Label(Screen,image=image,height = 900, width =920)
label.place(x=0,y=0)


InputLanguageChoice = StringVar()


TranslateLanguageChoice = StringVar()


LanguageChoices = { 'Afrikaans',
'Albanian',
'Amharic',
'Arabic',
'Armenian',
'Assamese',
'Aymara',
'Azerbaijani',
'Bambara',
'Basque',
'Belarusian',
'Bengali',
'Bhojpuri',
'Bosnian',
'Bulgarian',
'Catalan',
'Cebuano',
'Chichewa',
'Chinese (Simplified)',
'Chinese (Traditional)',
'Corsican',
'Croatian',
'Czech',
'Danish',
'Dhivehi',
'Dogri',
'Dutch',
'history',
'English',
'Esperanto',
'Estonian',
'Ewe',
'Filipino',
'Finnish',
'French',
'Frisian',
'Galician',
'Georgian',
'German',
'Greek',
'Guarani',
'Gujarati',
'Haitian Creole',
'Hausa',
'Hawaiian',
'Hebrew',
'Hindi',
'Hmong',
'Hungarian',
'Icelandic',
'Igbo',
'Ilocano',
'Indonesian',
'Irish',
'Italian',
'Japanese',
'Javanese',
'Kannada',
'Kazakh',
'Khmer',
'Kinyarwanda',
'Konkani',
'Korean',
'Krio',
'Kurdish (Kurmanji)',
'Kurdish (Sorani)',
'Kyrgyz',
'Lao',
'Latin',
'Latvian',
'Lingala',
'Lithuanian',
'Luganda',
'Luxembourgish',
'Macedonian',
'Maithili',
'Malagasy',
'Malay',
'Malayalam',
'Maltese',
'Maori',
'Marathi',
'Meiteilon (Manipuri)',
'Mizo',
'Mongolian',
'Myanmar (Burmese)',
'Nepali',
'Norwegian',
'Odia (Oriya)',
'Oromo',
'Pashto',
'Persian',
'Polish',
'Portuguese',
'Punjabi',
'Quechua',
'Romanian',
'Russian',
'Samoan',
'Sanskrit',
'Scots Gaelic',
'Sepedi',
'Serbian',
'Sesotho',
'Shona',
'Sindhi',
'Sinhala',
'Slovak',
'Slovenian',
'check',
'Somali',
'history',
'Spanish',
'Sundanese',
'Swahili',
'Swedish',
'Tajik',
'history',
'Tamil',
'Tatar',
'Telugu',
'Thai',
'Tigrinya',
'Tsonga',
'Turkish',
'Turkmen',
'Twi',
'Ukrainian',
'Urdu',
'Uyghur',
'Uzbek',
'Vietnamese',
'Welsh',
'Xhosa',
'Yiddish',
'Yoruba',
'Zulu',}

InputLanguageChoice.set('English')

TranslateLanguageChoice.set('Telugu')

def Translate():
    translator = Translator(from_lang= InputLanguageChoice.get(),to_lang=TranslateLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)

#title

Title=Label(Screen,text="Language Translator", bg = 'light green', font = ("ariel", 69, "bold"))

Title.place(x=125,y=20)

#choice for input language

InputLanguageChoiceMenu = OptionMenu(Screen,InputLanguageChoice,*LanguageChoices)

SelectLanguage=Label(Screen,text="Select a Language", bg='light blue',font=("ariel",21," bold") )

SelectLanguage.place(x=50,y=150)

InputLan=InputLanguageChoiceMenu
 
InputLan.place(x=100,y=200)
 
#choice in which the language is to be translated

NewLanguageChoiceMenu = OptionMenu(Screen,TranslateLanguageChoice,*LanguageChoices)

To=Label(Screen,text="Translate To", bg='light blue',font=("ariel",21," bold"))

To.place(x=710,y=150)

TransSelect=NewLanguageChoiceMenu

TransSelect.place(x=746,y=200)

Text=Label(Screen,text="Enter Text Here", bg='orange2',font=("ariel",21," bold"))

Text.place(x=413,y=250)

TextVar = StringVar()

TextBox = Entry(Screen,textvariable=TextVar,bg="silver")
 
TextBox.place(x=400,y=300)

Output=Label(Screen,text="Output",bg='gold',font=("ariel",21," bold"))

Output.place(x=457,y=500)

OutputVar = StringVar()

TextBox = Entry(Screen,textvariable=OutputVar,bg="silver")
 
TextBox.place(x=400,y=550)

#Button for calling function

B = Button(Screen,text="Translate", command = Translate, relief = GROOVE, bg="silver",font=("ariel",40," bold"))

B.place(x=410,y=400)
    
mainloop()