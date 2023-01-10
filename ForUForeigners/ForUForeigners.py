from tkinter import *
""" ----------FOR COMBO-BOX---------- """
from tkinter import ttk



"""(SRH) ----------Our - Programming - Part---------- (SRH)"""
from googletrans import Translator,LANGUAGES

"""(SRH) ----------Translating---------- (SRH)"""
def change(text="type",src="bengali",dest="nepali"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text

"""(SRH) ----------Getting Data---------- (SRH)"""
def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0,END)
    textget = change(text = msg, src=s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)


root = Tk()
root.title("For U Foreigners!")
root.geometry("500x800")
root.config(bg='#D51264')

""" ----------Labeling For Header---------- """
lab_txt=Label(root,text="Translator!",font=("cascadia code",30,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

""" ----------Framing---------- """
frame = Frame(root).pack(side=BOTTOM)

""" ----------Labeling for source text---------- """
lab_txt=Label(root,text="Source Text:",font=("cascadia code",20),bg='yellow')
lab_txt.place(x=100,y=100,height=20,width=300)

""" ----------Source_Text-BOX---------- """
Sor_txt = Text(frame,font=("cascadia code",20,"bold"),wrap=WORD)
Sor_txt.place(x=10,y=130,height=150,width=480)

"""(SRH) ----------Combo-Box-For Source Text---------- (SRH)"""
list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,values=list_text)
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("select")

"""(SRH) ----------Buttoning---------- (SRH)"""
button_change=Button(frame, text="Translate",relief=RAISED,command=data)
button_change.place(x=170,y=300,height=40,width=150)

"""(SRH) ----------Combo-Box-For Destination Text---------- (SRH)"""
comb_dest= ttk.Combobox(frame,values=list_text)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("select")

"""(SRH) ----------Labeling for Destinatin Box---------- (SRH)"""
lab_txt=Label(root,text="Translated Text:",font=("cascadia code",20),bg='yellow')
lab_txt.place(x=100,y=360,height=20,width=300)

"""(SRH) ----------Destination Text-Box---------- (SRH)"""
dest_txt = Text(frame,font=("cascadia code",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)



root.mainloop()