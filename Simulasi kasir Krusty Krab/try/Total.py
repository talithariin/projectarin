
# FUNGSI
# Awal fungsi perhitungan harga total
def totalcost():
    # mengglobalkan beberapa variable terlebih dahulu
    global hargadariMealsDeals,hargadariDrinks,hargadariSeadSides,subtotalItems,totaltax
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or\
        var26.get() != 0 or var27.get() != 0:

        item1=int(e_KrabbyPatty.get())
        item2=int(e_KrabbyPattySeaCheese.get())
        item3=int(e_DoubleKrabbyPatty.get())
        item4=int(e_TripleKrabbyPatty.get())
        item5=int(e_KrabbyMeal.get())
        item6=int(e_DoubleKrabbyMeal.get())
        item7=int(e_SailorsSurprise.get())
        item8=int(e_SaltySeaDog.get())
        item9=int(e_FootLong.get())

        item10=int(e_KelpShake .get())
        item11=int(e_SmallSeafoamSoda.get())
        item12=int(e_MediumSeafoamSoda.get())
        item13=int(e_LargeSeafoamSoda.get())

        item19=int(e_CoralBits.get())
        item20=int(e_LargeCoralBits.get())
        item21=int(e_KelpRings.get())
        item22=int(e_SaltySauce.get())
        item23=int(e_KrabbyFries.get())
        item24=int(e_SeaweedSalad.get())

        hargadariMealsDeals=(item1*28000) + (item2*32000) + (item3*29000) + (item4*28000) + (item5*31000) + (item6*26000) + (item7*38000) \
        + (item8*27000) + (item9*29000)
        hargadariDrinks=(item10*20000) + (item11*15000) + (item12*15000) + (item13*22000)
        hargadariSeadSides=(item19*18000) + (item20*25000) + (item21*25000) + (item22*28000) + (item23*16000) + (item24*21000) \

        hargadariMealsDealsvar.set(str(hargadariMealsDeals))
        hargadariDrinksvar.set(str(hargadariDrinks))
        hargadariSeadSidesvar.set(str(hargadariSeadSides))

        subtotalItems=hargadariMealsDeals+hargadariDrinks+hargadariSeadSides
        subtotalvar.set(str(subtotalItems))
       #tax=(11/100)
        taxvaluevar.set(str(tax))
        totaltax= subtotalItems*tax
        
        servicetaxvar.set(totaltax)
        
        totalcost=subtotalItems+totaltax
        totalcostvar.set(str(totalcost))

    else:
        messagebox.showerror('Error','Tidak ada item yang dipilih')
# Batas fungsi perhitungan harga total