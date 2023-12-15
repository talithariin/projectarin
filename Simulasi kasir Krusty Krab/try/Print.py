# awal fungsi cetak struk
def struk():
    global billnumber, date
    if hargadariMealsDealsvar.get() != '' or hargadariSeadSidesvar.get() != '' or hargadariDrinksvar.get() != '':
        textStruk.delete(1.0, END)
        x = random.randint(100, 10000)
        billnumber = 'BILL' + str(x)
        
        # Get the current date and time
        current_datetime = datetime.now()
        date = current_datetime.strftime('%d/%m/%Y %H:%M:%S')
        
        textStruk.insert(END, 'Receipt Ref:\t        ' + billnumber + '\t         ' + date + '\n')
        textStruk.insert(END, '************************************\n')
        textStruk.insert(END, 'Items:\t\t\tQty\t\tTotal Price (Rp)\n')
        textStruk.insert(END, '************************************\n')
    
        # Krabby Patty
        if e_KrabbyPatty.get() != '0':
            quantity_KrabbyPatty = int(e_KrabbyPatty.get())
            total_price_KrabbyPatty = quantity_KrabbyPatty * 27000
            textStruk.insert(END, f'KrabbyPatty\t\t\t{quantity_KrabbyPatty}\t\tRp. {total_price_KrabbyPatty}\n\n')
        
        # Krabby Patty with Sea Cheese
        if e_KrabbyPattySeaCheese.get() != '0':
            quantity_KrabbyPattySeaCheese = int(e_KrabbyPattySeaCheese.get())
            total_price_KrabbyPattySeaCheese = quantity_KrabbyPattySeaCheese * 33000
            textStruk.insert(END, f'KrabbyPattySeaCheese\t\t\t{quantity_KrabbyPattySeaCheese}\t\tRp. {total_price_KrabbyPattySeaCheese}\n\n')

        # Double Krabby Patty
        if e_DoubleKrabbyPatty.get() != '0':
            quantity_DoubleKrabbyPatty = int(e_DoubleKrabbyPatty.get())
            total_price_DoubleKrabbyPatty = quantity_DoubleKrabbyPatty * 25000
            textStruk.insert(END, f'DoubleKrabbyPatty\t\t\t{quantity_DoubleKrabbyPatty}\t\tRp. {total_price_DoubleKrabbyPatty}\n\n')

        # Cinnamon Roll
        if e_TripleKrabbyPatty.get() != '0':
            quantity_TripleKrabbyPatty = int(e_TripleKrabbyPatty.get())
            total_price_TripleKrabbyPatty = quantity_TripleKrabbyPatty * 22000
            textStruk.insert(END, f'TripleKrabbyPatty\t\t\t{quantity_TripleKrabbyPatty}\t\tRp. {total_price_TripleKrabbyPatty}\n\n')

        # Krabby Meal
        if e_KrabbyMeal.get() != '0':
            quantity_KrabbyMeal = int(e_KrabbyMeal.get())
            total_price_KrabbyMeal = quantity_KrabbyMeal * 33000
            textStruk.insert(END, f'KrabbyMeal\t\t\t{quantity_KrabbyMeal}\t\tRp. {total_price_KrabbyMeal}\n\n')

        # Double Krabby Meal
        if e_DoubleKrabbyMeal.get() != '0':
            quantity_DoubleKrabbyMeal = int(e_DoubleKrabbyMeal.get())
            total_price_DoubleKrabbyMeal = quantity_DoubleKrabbyMeal * 46000
            textStruk.insert(END, f'DoubleKrabbyMeal\t\t\t{quantity_DoubleKrabbyMeal}\t\tRp. {total_price_DoubleKrabbyMeal}\n\n')

        # Sailors Surprise
        if e_SailorsSurprise.get() != '0':
            quantity_SailorsSurprise = int(e_SailorsSurprise.get())
            total_price_SailorsSurprise = quantity_SailorsSurprise * 38000
            textStruk.insert(END, f'SailorsSurprise\t\t\t{quantity_SailorsSurprise}\t\tRp. {total_price_SailorsSurprise}\n\n')

        # Salty Sea Dog
        if e_SaltySeaDog.get() != '0':
            quantity_SaltySeaDog = int(e_SaltySeaDog.get())
            total_price_SaltySeaDog = quantity_SaltySeaDog * 27000
            textStruk.insert(END, f'avocado toast\t\t\t{quantity_SaltySeaDog}\t\tRp. {total_price_SaltySeaDog}\n\n')

        # Foot Long
        if e_FootLong.get() != '0':
            quantity_FootLong = int(e_FootLong.get())
            total_price_FootLong = quantity_FootLong * 22000
            textStruk.insert(END, f'tomato soup\t\t\t{quantity_FootLong}\t\tRp. {total_price_FootLong}\n\n')

        # Kelp Shake
        if e_KelpShake .get() != '0':
            quantity_KelpShake  = int(e_KelpShake .get())
            total_price_KelpShake  = quantity_KelpShake  * 20000
            textStruk.insert(END, f'apple juice\t\t\t{quantity_KelpShake }\t\tRp. {total_price_KelpShake }\n\n')

        # Small Seafoam Soda
        if e_SmallSeafoamSoda.get() != '0':
            quantity_SmallSeafoamSoda = int(e_SmallSeafoamSoda.get())
            total_price_SmallSeafoamSoda = quantity_SmallSeafoamSoda * 15000
            textStruk.insert(END, f'lemon tea\t\t\t{quantity_SmallSeafoamSoda}\t\tRp. {total_price_SmallSeafoamSoda}\n\n')

        # Medium Seafoam Soda
        if e_MediumSeafoamSoda.get() != '0':
            quantity_MediumSeafoamSoda = int(e_MediumSeafoamSoda.get())
            total_price_MediumSeafoamSoda = quantity_MediumSeafoamSoda * 15000
            textStruk.insert(END, f'MediumSeafoamSoda\t\t\t{quantity_MediumSeafoamSoda}\t\tRp. {total_price_MediumSeafoamSoda}\n\n')

        # Large Seafoam Soda
        if e_LargeSeafoamSoda.get() != '0':
            quantity_LargeSeafoamSoda = int(e_LargeSeafoamSoda.get())
            total_price_LargeSeafoamSoda = quantity_LargeSeafoamSoda * 22000
            textStruk.insert(END, f'LargeSeafoamSoda\t\t\t{quantity_LargeSeafoamSoda}\t\tRp. {total_price_LargeSeafoamSoda}\n\n')

         # Large Coral Bits
        if e_LargeCoralBits.get() != '0':
            quantity_LargeCoralBits = int(e_LargeCoralBits.get())
            total_price_LargeCoralBits = quantity_LargeCoralBits * 36000
            textStruk.insert(END, f'french fries\t\t\t{quantity_LargeCoralBits}\t\tRp. {total_price_LargeCoralBits}\n\n')

        # Kelp Rings
        if e_KelpRings.get() != '0':
            quantity_KelpRings = int(e_KelpRings.get())
            total_price_KelpRings = quantity_KelpRings * 15000
            textStruk.insert(END, f'fried ice cream\t\t\t{quantity_KelpRings}\t\tRp. {total_price_KelpRings}\n\n')

        # Salty Sauce
        if e_SaltySauce.get() != '0':
            quantity_SaltySauce = int(e_SaltySauce.get())
            total_price_SaltySauce = quantity_SaltySauce * 1500
            textStruk.insert(END, f'cheese cake\t\t\t{quantity_SaltySauce}\t\tRp. {total_price_SaltySauce}\n\n')

        # Krabby Fries
        if e_KrabbyFries.get() != '0':
            quantity_KrabbyFries = int(e_KrabbyFries.get())
            total_price_KrabbyFries = quantity_KrabbyFries * 16000
            textStruk.insert(END, f'ice cream\t\t\t{quantity_KrabbyFries}\t\tRp. {total_price_KrabbyFries}\n\n')

        # Seaweed Salad
        if e_SeaweedSalad.get() != '0':
            quantity_SeaweedSalad = int(e_SeaweedSalad.get())
            total_price_SeaweedSalad = quantity_SeaweedSalad * 21000
            textStruk.insert(END, f'SeaweedSalad\t\t\t{quantity_SeaweedSalad}\t\tRp. {total_price_SeaweedSalad}\n\n')

        textStruk.insert(END,'******************\n')
        if hargadariMealsDealsvar.get()!='Rp 0':
            textStruk.insert(END,f'Meals price\t\t\tRp. {hargadariMealsDeals}\n\n')
        if hargadariDrinksvar.get() != 'Rp 0':
            textStruk.insert(END,f'Drinks price\t\t\tRp. {hargadariDrinks}\n\n')
        if hargadariSeadSidesvar.get() != 'Rp 0':
            textStruk.insert(END,f'Sea sides price \t\t\tRp. {hargadariSeadSides}\n\n')

        textStruk.insert(END, f'Sub Total\t\t\tRp. {subtotalItems}\n\n')
        textStruk.insert(END, f'Service Tax\t\t\tRp. {totaltax}\n\n')
        textStruk.insert(END, f'Total price\t\t\tRP. {subtotalItems+totaltax}\n\n')
        textStruk.insert(END,'******************\n')

    else:
        messagebox.showerror('Error','No items selected')
# batas fungsi cetak struk
