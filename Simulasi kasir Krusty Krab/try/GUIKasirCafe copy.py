from cProfile import label
import string
from tkinter import *
import random
import csv
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime
from tkinter import messagebox
from tkinter import filedialog
from turtle import clear;
from PIL import ImageTk, Image 
from pygame import mixer

from Total import *
from Print import *
from Save import *
from Reset import *
from Menu import *

def play_background_music():
    mixer.init()
    mixer.music.load("krustykrab.mp3")  # Replace "background_music.mp3" with the path to your music file
    mixer.music.play(1)  # -1 will make the music loop indefinitely

# Start playing background music
play_background_music()

#Membuat Frame aplikasi
root = Tk()

from Var import *

root.geometry("1540x760+0+0") # menentukan ukuran window aplikasi
root.resizable(0,0)
root.title("Krusty Krab Cashier") # nama aplikasi

topFrame=Frame(root,bd=10,relief=RIDGE,bg='white') # frame judul
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Krusty Krab',font=('Krabby Patty',39,'bold'),fg='#461912',bg='#ffeec2', bd=15,width=30) #judul aplikasi
labelTitle.grid(row=0,column=10)

root.config(bg='#784c12') # warna dasar / background
# batas Frame aplikasi
tax=(11/100)

# FRAME KIRI
# Membuat frame kiri untuk menu cafe
menuFrame=Frame(root,bd=10,relief=RIDGE,bg='#8ca2d2')
menuFrame.pack(side=LEFT)

hargaFrame=Frame(menuFrame,bd=9,relief=RIDGE,bg='#ffeec2',pady=12)
hargaFrame.pack(side=BOTTOM)
MealsDealsFrame = LabelFrame(menuFrame, text='Meals Deals', font=('Krabby Patty', 19, 'bold'), bd=10, relief=RIDGE, fg='#2f2f2f', bg='#7d6536')
MealsDealsFrame.pack(side=LEFT)

DrinksFrame=LabelFrame(menuFrame,text=' Drinks ',font=('Krabby Patty',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#7d6536')
DrinksFrame.pack(side=LEFT)

SeadSideshargadariSeadSidesFrame=LabelFrame(menuFrame,text=' Sea Sides ',font=('Krabby Patty',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#7d6536')
SeadSideshargadariSeadSidesFrame.pack(side=LEFT)
# batas frame kiri (menu cafe)


# membuat tampilan daftar menu makanan
KrabbyPatty = Checkbutton(MealsDealsFrame, text=' Krabby Patty ', font=('Krabby Patty', 14, 'bold'), onvalue=1, offvalue=0, variable=var1, command=KrabbyPatty, bg='#7d6536')
KrabbyPatty.grid(row=0, column=0, sticky=W)

KrabbyPattySeaCheese = Checkbutton(MealsDealsFrame, text=' Krabby Patty with Sea Cheese ', font=('Krabby Patty', 14, 'bold'), onvalue=1, offvalue=0, variable=var2, command=KrabbyPattySeaCheese, bg='#7d6536')
KrabbyPattySeaCheese.grid(row=1, column=0, sticky=W)

DoubleKrabbyPatty = Checkbutton(MealsDealsFrame, text=' Double Krabby Patty ', font=('Krabby Patty', 14, 'bold'), onvalue=1, offvalue=0, variable=var3, command=DoubleKrabbyPatty, bg='#7d6536')
DoubleKrabbyPatty.grid(row=2, column=0, sticky=W)

TripleKrabbyPatty = Checkbutton(MealsDealsFrame, text=' Triple Krabby Patty ', font=('Krabby Patty', 14, 'bold'), onvalue=1, offvalue=0, variable=var4, command=TripleKrabbyPatty, bg='#7d6536')
TripleKrabbyPatty.grid(row=3, column=0, sticky=W)

KrabbyMeal = Checkbutton(MealsDealsFrame, text=' Krabby Meal ', font=('Krabby Patty', 14, 'bold'), onvalue=1, offvalue=0, variable=var5, command=KrabbyMeal, bg='#7d6536')
KrabbyMeal.grid(row=4, column=0, sticky=W)

DoubleKrabbyMeal = Checkbutton(MealsDealsFrame, text=' Double Krabby Meal ', font=('Krabby Patty', 14, 'bold'), onvalue=1, offvalue=0, variable=var6, command=DoubleKrabbyMeal, bg='#7d6536')
DoubleKrabbyMeal.grid(row=5, column=0, sticky=W)

SailorsSurprise = Checkbutton(MealsDealsFrame, text=' Sailors Surprise ', font=('Krabby Patty', 14, 'bold'), onvalue=1, offvalue=0, variable=var7, command=SailorsSurprise, bg='#7d6536')
SailorsSurprise.grid(row=6, column=0, sticky=W)

SaltySeaDog = Checkbutton(MealsDealsFrame, text=' Salty Sea Dog', font=('Krabby Patty', 14, 'bold'), onvalue=1, offvalue=0, variable=var8, command=SaltySeaDog, bg='#7d6536')
SaltySeaDog.grid(row=7, column=0, sticky=W)

FootLong = Checkbutton(MealsDealsFrame, text=' Foot Long ', font=('Krabby Patty', 14, 'bold'), onvalue=1, offvalue=0, variable=var9, command=FootLong, bg='#7d6536')
FootLong.grid(row=8, column=0, sticky=W)

textKrabbyPatty = Entry(MealsDealsFrame, font=('Krabby Patty', 14, 'bold'), bd=7, width=8, state=DISABLED, textvar=e_KrabbyPatty)
textKrabbyPatty.grid(row=0, column=1)

textKrabbyPattySeaCheese = Entry(MealsDealsFrame, font=('Krabby Patty', 14, 'bold'), bd=7, width=8, state=DISABLED, textvar=e_KrabbyPattySeaCheese)
textKrabbyPattySeaCheese.grid(row=1, column=1)

textDoubleKrabbyPatty = Entry(MealsDealsFrame, font=('Krabby Patty', 14, 'bold'), bd=7, width=8, state=DISABLED, textvar=e_DoubleKrabbyPatty)
textDoubleKrabbyPatty.grid(row=2, column=1)

textTripleKrabbyPatty = Entry(MealsDealsFrame, font=('Krabby Patty', 14, 'bold'), bd=7, width=8, state=DISABLED, textvar=e_TripleKrabbyPatty)
textTripleKrabbyPatty.grid(row=3, column=1)

textKrabbyMeal = Entry(MealsDealsFrame, font=('Krabby Patty', 14, 'bold'), bd=7, width=8, state=DISABLED, textvar=e_KrabbyMeal)
textKrabbyMeal.grid(row=4, column=1)

textDoubleKrabbyMeal = Entry(MealsDealsFrame, font=('Krabby Patty', 14, 'bold'), bd=7, width=8, state=DISABLED, textvar=e_DoubleKrabbyMeal)
textDoubleKrabbyMeal.grid(row=5, column=1)

textSailorsSurprise = Entry(MealsDealsFrame, font=('Krabby Patty', 14, 'bold'), bd=7, width=8, state=DISABLED, textvar=e_SailorsSurprise)
textSailorsSurprise.grid(row=6, column=1)

textSaltySeaDog = Entry(MealsDealsFrame, font=('Krabby Patty', 14, 'bold'), bd=7, width=8, state=DISABLED, textvar=e_SaltySeaDog)
textSaltySeaDog.grid(row=7, column=1)

textFootLong = Entry(MealsDealsFrame, font=('Krabby Patty', 14, 'bold'), bd=7, width=8, state=DISABLED, textvar=e_FootLong)
textFootLong.grid(row=8, column=1)

# membuat tampilan daftar menu Drinks
KelpShake =Checkbutton(DrinksFrame,text='Kelp Shake',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var10,
                        command=KelpShake , bg='#7d6536')
KelpShake .grid(row=0,column=0,sticky=W)

SmallSeafoamSoda=Checkbutton(DrinksFrame,text='Small Seafoam Soda',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var11,
                        command=SmallSeafoamSoda, bg='#7d6536')
SmallSeafoamSoda.grid(row=1,column=0,sticky=W)

MediumSeafoamSoda=Checkbutton(DrinksFrame,text='Medium Seafoam Soda',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var12,
                        command=MediumSeafoamSoda, bg='#7d6536')
MediumSeafoamSoda.grid(row=2,column=0,sticky=W)

LargeSeafoamSoda=Checkbutton(DrinksFrame,text='Large Seafoam Soda',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var13,
                        command=LargeSeafoamSoda, bg='#7d6536')
LargeSeafoamSoda.grid(row=3,column=0,sticky=W)

# menambahkan fields entri untuk item Drinks
textKelpShake =Entry(DrinksFrame,font=('Krabby Patty','14','bold'),bd=7,width=7,state=DISABLED,textvar=e_KelpShake )
textKelpShake .grid(row=0,column=1)

textSmallSeafoamSoda=Entry(DrinksFrame,font=('Krabby Patty','14','bold'),bd=7,width=7,state=DISABLED,textvar=e_SmallSeafoamSoda)
textSmallSeafoamSoda.grid(row=1,column=1)

textMediumSeafoamSoda=Entry(DrinksFrame,font=('Krabby Patty','14','bold'),bd=7,width=7,state=DISABLED,textvar=e_MediumSeafoamSoda)
textMediumSeafoamSoda.grid(row=2,column=1)

textLargeSeafoamSoda=Entry(DrinksFrame,font=('Krabby Patty','14','bold'),bd=7,width=7,state=DISABLED,textvar=e_LargeSeafoamSoda)
textLargeSeafoamSoda.grid(row=3,column=1)

# membuat tampilan daftar menu SeadSideshargadariSeadSides
CoralBits=Checkbutton(SeadSideshargadariSeadSidesFrame,text='Coral Bits',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var19,
            command=CoralBits, bg='#7d6536')
CoralBits.grid(row=0,column=0,sticky=W)

LargeCoralBits=Checkbutton(SeadSideshargadariSeadSidesFrame,text='Large Coral Bits',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var20,
            command=LargeCoralBits, bg='#7d6536')  
LargeCoralBits.grid(row=1,column=0,sticky=W)

KelpRings=Checkbutton(SeadSideshargadariSeadSidesFrame,text='Kelp Rings',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var21,
            command=KelpRings, bg='#7d6536')
KelpRings.grid(row=2,column=0,sticky=W)

SaltySauce=Checkbutton(SeadSideshargadariSeadSidesFrame,text='Salty Sauce',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var22,
            command=SaltySauce, bg='#7d6536')
SaltySauce.grid(row=3,column=0,sticky=W)

KrabbyFries=Checkbutton(SeadSideshargadariSeadSidesFrame,text='Krabby Fries',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var23,
            command=KrabbyFries, bg='#7d6536')
KrabbyFries.grid(row=4,column=0,sticky=W)

SeaweedSalad=Checkbutton(SeadSideshargadariSeadSidesFrame,text='Seaweed Salad',font=('Krabby Patty',14,'bold'),onvalue=1,offvalue=0,variable=var24,
            command=SeaweedSalad, bg='#7d6536')
SeaweedSalad.grid(row=5,column=0,sticky=W)

# menambahkan fields entri untuk item SeadSideshargadariSeadSides
textCoralBits = Entry(SeadSideshargadariSeadSidesFrame, font=('Krabby Patty','14','bold'),bd=7,width=7, state=DISABLED, textvar=e_CoralBits)
textCoralBits.grid(row=0, column=1)

textLargeCoralBits = Entry(SeadSideshargadariSeadSidesFrame, font=('Krabby Patty','14','bold'),bd=7,width=7, state=DISABLED, textvar=e_LargeCoralBits)
textLargeCoralBits.grid(row=1, column=1)

textKelpRings = Entry(SeadSideshargadariSeadSidesFrame, font=('Krabby Patty','14','bold'),bd=7,width=7, state=DISABLED, textvar=e_KelpRings)
textKelpRings.grid(row=2, column=1)

textSaltySauce = Entry(SeadSideshargadariSeadSidesFrame, font=('Krabby Patty','14','bold'),bd=7,width=7, state=DISABLED, textvar=e_SaltySauce)
textSaltySauce.grid(row=3, column=1)

textKrabbyFries = Entry(SeadSideshargadariSeadSidesFrame, font=('Krabby Patty','14','bold'),bd=7,width=7, state=DISABLED, textvar=e_KrabbyFries)
textKrabbyFries.grid(row=4, column=1)

textSeaweedSalad = Entry(SeadSideshargadariSeadSidesFrame, font=('Krabby Patty','14','bold'),bd=7,width=7, state=DISABLED, textvar=e_SeaweedSalad)
textSeaweedSalad.grid(row=5, column=1)

# FRAME KANAN

# Membuat frame kanan untuk (Struk)
rightFrame=Frame(root,bd=15,relief=RIDGE)
rightFrame.pack(side=RIGHT)

strukFrame=Frame(rightFrame,bd=1,relief=RIDGE, bg='#f0f0f0')
strukFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE)
buttonFrame.pack()
# Batas frame kanan (Struk)


# membuat label harga dan kolom entrinya
LabelHargadariMealsDeals=Label(hargaFrame,text='    MEALS PRICE', font=('Krabby Patty',12,'bold'),bg='#ffeec2',fg='#461912')
LabelHargadariMealsDeals.grid(row=0,column=0)

textHargadariMealsDeals=Entry(hargaFrame,font=('Krabby Patty',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadariMealsDealsvar)
textHargadariMealsDeals.grid(row=0,column=1,padx=41)

LabelHargadariDrinks=Label(hargaFrame,text='    DRINKS PRICE', font=('Krabby Patty',12,'bold'),bg='#ffeec2',fg='#461912')
LabelHargadariDrinks.grid(row=1,column=0)

textHargadariDrinks=Entry(hargaFrame,font=('Krabby Patty',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadariDrinksvar)
textHargadariDrinks.grid(row=1,column=1,padx=41)

LabelHargadariSeaSides=Label(hargaFrame,text='  SEA SIDES PRICE', font=('Krabby Patty',12,'bold'),bg='#ffeec2',fg='#461912')
LabelHargadariSeaSides.grid(row=2,column=0)

textHargadariSeaSides=Entry(hargaFrame,font=('Krabby Patty',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadariSeadSidesvar)
textHargadariSeaSides.grid(row=2,column=1,padx=41)

LabelSubTotal=Label(hargaFrame,text='SUB TOTAL', font=('Krabby Patty',12,'bold'),bg='#ffeec2',fg='#461912')
LabelSubTotal.grid(row=0,column=2)
textSubTotal=Entry(hargaFrame,font=('Krabby Patty',14,'bold'),bd=6,width=16,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

LabelTax=Label(hargaFrame,text='Tax'+' '+str(tax*100)+'%', font=('Krabby Patty',12,'bold'),bg='#ffeec2',fg='#461912')
LabelTax.grid(row=1,column=2)

textTax=Entry(hargaFrame,font=('Krabby Patty',14,'bold'),bd=6,width=16,state='readonly',textvariable=servicetaxvar)
textTax.grid(row=1,column=3,padx=41)

LabelHargaTotal=Label(hargaFrame,text='TOTAL PRICE', font=('Krabby Patty',12,'bold'),bg='#ffeec2',fg='#461912')
LabelHargaTotal.grid(row=2,column=2)

textHargaTotal=Entry(hargaFrame,font=('Krabby Patty',14,'bold'),bd=6,width=16,state='readonly',textvariable=totalcostvar)
textHargaTotal.grid(row=2,column=3,padx=41)


# Membuat tampilan Buttons struk (Tombol-tombol pada frame kanan)
buttonTotal= Button(buttonFrame,text='Total',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonStruk= Button(buttonFrame,text='Receipt',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=struk)
buttonStruk.grid(row=0,column=1)

buttonSimpan= Button(buttonFrame,text='Save',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=save)
buttonSimpan.grid(row=0,column=2)

buttonReset= Button(buttonFrame,text='Reset',font=('arial',12,'bold'),fg='#fefefe',bg='red',bd=3,padx=12,
            command=reset)
buttonReset.grid(row=0,column=4)

# menentukan teks pada frame struk
textStruk=Text(strukFrame,font=('arial',12,'bold'),bd=3,width=36,height=26)
textStruk.grid(row=0,column=0)


root.mainloop()

# Stop the music when the program exits
mixer.music.stop()