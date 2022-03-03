
import tkinter as tk
from tkinter import Y, StringVar, ttk
import tkinter
import tkinter.font as tkFont
from pytube import YouTube
from PIL import Image, ImageTk
import re
def hide_button(widget): 
    textTitle.set('')
    textViews.set('')
    
    widget.place_forget()
  
  
def show_button(widget): 
    widget.pack() 

    botonGetTitle.place(x=150, y=130)

    botonDownload.place(x=150, y=170)

    botonGetDescription.place(x=150, y=210)
    botonGetViews.place(x=150, y=380)
    #botonDownloadAudio.place(x=270, y=170)
    T.place(x=265,y=210)

def download():
    link = entry.get()
    video = YouTube(link)
    video = video.streams.get_highest_resolution()
    video.download()

def title():
    link = entry.get()
    video = YouTube(link)
    textTitle.set(video.title)
def views():
    link = entry.get()
    video = YouTube(link)
    textViews.set(video.views)
def description():
    link = entry.get()
    video = YouTube(link)
    T.delete("1.0","end")
    
    T.insert(tk.END,video.description)

    

def ObtenerLink():
    link = entry.get()
    x = [a for a in str(link)]
    hide_button(botonDownload)
    hide_button(botonGetDescription)
    hide_button(botonGetTitle)
    #hide_button(botonDownloadAudio)
    hide_button(T)
    T.delete("1.0","end")
    LINK(x)

def LINK(link):
    ECorrect=False
    TCorrect=False
    ECorrect = E(link,ECorrect)
    TCorrect = TC(link,TCorrect)
    if(ECorrect & TCorrect):
        #aqui busca el video o nose q chuchas haga xdd
        show_button(botonDownload)
        show_button(botonGetDescription)
        show_button(botonGetTitle)
        show_button(botonGetViews)
        textValido.set("Link Correcto")
        #show_button(botonDownloadAudio)
    else:
        hide_button(botonDownload)
        hide_button(botonGetDescription)
        hide_button(botonGetTitle)
        hide_button(botonGetViews)
        #hide_button(botonDownloadAudio)
        textValido.set("Revisa bien tu link")
def E(link,ECorrect):
    Dcorrect=False
    Ycorrect=False
    Wcorrect=False
    Dcorrect=D(link,Dcorrect)
    Ycorrect=Y(link,Ycorrect)
    Wcorrect=W(link,Wcorrect)
    if(Dcorrect&Ycorrect&Wcorrect):
        ECorrect = True
        print("Estructura del link correcta")
    else:
        ECorrect = False 
        print("Estructura del link incorrecta")
    return ECorrect

def D(link,Dcorrect):
    http=[]
    
    for i in range (8):
        http.append(link[i])
    texto="".join(http)
    if(re.search("https://",texto)==None):
        Dcorrect = False
        textDominio.set("Dominio incorrecto")
    else:
        Dcorrect= True
        textDominio.set("Dominio correcto")
        
    print("".join(http))
    return Dcorrect
    
    
def Y(link,Ycorrect):
    yout=[]
    rango=8
    for i in range(16):
        yout.append(link[rango])
        rango=rango+1
    texto = "".join(yout)
    if(re.search("www.youtube.com/",texto)==None):
        Ycorrect = False
        textYoutube.set("Youtube incorrecto")
    else:
        Ycorrect= True
        textYoutube.set("Youtube correcto")
        
    print("".join(yout))
    return Ycorrect
    
def W(link,Wcorrect):
    watch=[]
    rango=24
    for i in range(8):
        watch.append(link[rango])
        rango = rango+1
    texto = "".join(watch)
    print(texto)
    if(re.match("watch\?v=",texto)==None):
        Wcorrect = False
        textWatch.set("watch incorrecto")
    else:
        Wcorrect= True
        textWatch.set("watch correcto")
        
    print("".join(watch))
    return Wcorrect
    
def TC(link,TCorrect):
    code=[]
    rango = 32
    for i in range(32,len(link)):
        code.append(link[rango])
        rango=rango+1
    cadena="".join(code)
    result  = re.match("^[0-9a-zA-Z\-\_]{11}$", "".join(code))
    if result:
        TCorrect = True
        textCodigo.set("codigo correcto")
    else:
        TCorrect =False
        textCodigo.set("codigo incorrecto")
    print("".join(code))
    return TCorrect
if __name__ == "__main__":

    root = tk.Tk()
    root.config(width=830, height=600,background='#49A')
    root.title("Verificador de links de Youtube")
    # Crear caja de texto.
    entry = ttk.Entry(root)
    entry.config(width=50)
    # Posicionarla en la ventana.
    entry.place(x=150, y=50)
    T = tk.Text(root, height = 10, width = 52)

    boton = ttk.Button(text="VERIFICAR LINK", command=ObtenerLink)
    boton.place(x=150, y=90)
    botonGetTitle = ttk.Button(text="obtener titulo", command=title)
    botonDownload = ttk.Button(text="descargar video", command=download)
    #botonDownloadAudio = ttk.Button(text="descargar audio", command=downloadAudio)
    botonGetDescription = ttk.Button(text="obtener descripcion", command=description)
    botonGetViews = ttk.Button(text="obtener vistas", command=views)
    textTitle=StringVar()
    texto1 = tkinter.Label(root,text="",font=12,textvariable= textTitle,background='#49A').place(x=260,y=130) 
    textViews=StringVar()
    texto1 = tkinter.Label(root,text="a",font=12,textvariable= textViews,background='#49A').place(x=260,y=380) 
    textDownload=StringVar()
    texto1 = tkinter.Label(root,text="",font=12,textvariable= textDownload,background='#49A').place(x=260,y=170)
    textValido=StringVar()
    texto1 = tkinter.Label(root,text="",font=12,textvariable= textValido,background='#49A').place(x=260,y=90)
    textDominio=StringVar()
    texto1 = tkinter.Label(root,text="",font=12,textvariable= textDominio,background='#49A').place(x=450,y=50)
    textYoutube=StringVar()
    texto1 = tkinter.Label(root,text="",font=12,textvariable= textYoutube,background='#49A').place(x=600,y=50)
    textWatch=StringVar()
    texto1 = tkinter.Label(root,text="",font=12,textvariable= textWatch,background='#49A').place(x=450,y=90)
    textCodigo=StringVar()
    texto1 = tkinter.Label(root,text="",font=12,textvariable= textCodigo,background='#49A').place(x=600,y=90) 
    root.mainloop()
