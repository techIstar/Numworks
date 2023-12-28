from kandinsky import *
from ion import *

def appui(touche=range(53)): # Merci cent20
    while True:
        for i in touche:
            if keydown(i):
                while keydown(i): True
                return i

def menu(titre,options):
    for i in range(len(options)):
        options[i]=options[i][:22]
    index = 0
    commande = 0
    gris=(106,101,115)
    noir=(0,0,0)
    blanc=(255,255,255)
    selec=(213,214,230)
    fill_rect(35,18,252,18*(1+len(options))+1,gris)
    draw_string(titre,int(160-10*len(titre)/2),18,blanc,gris)
    fill_rect(36,36,250,18*(len(options)),blanc)
    while (commande!=4 and commande!=5 and commande!=52):
        for i in range(len(options)):
            if i == index:
                draw_string("  "+options[i]+"                          "[:(23-len(options[i]))],36,36+18*i,noir,selec)
            else:
                draw_string("  "+options[i]+"                          "[:(23-len(options[i]))],36,36+18*i,noir,blanc)
        commande=appui((1,2,4,5,52))
        #draw_string(str(commande),0,0)
        if commande == 1 and index>0:index-=1
        if commande == 2 and index<len(options)-1:index+=1
    if commande==5:index=-1
    return index

choix=['Choix 1','Choix 2','Choix 3','Choix 4']
a=menu('Choisissez...',choix)
print("Option choisie :",a,":",choix[a])
bidon=input('truc:?')
