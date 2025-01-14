from random import choice


female_names = [
    "Aava", "Ahoo", "Aida", "Anahita", "Ariana", "Arina", "Armita", "Arnika", "Arshin", "Arta",
    "Atessa", "Azadeh", "Azar", "Azarin", "Azita", "Behnaz", "Behrokh", "Behshad", "Behzadi", "Berna",
    "Darya", "Delaram", "Delnavaz", "Dena", "Diba", "Dilara", "Donya", "Elnaz", "Elina", "Elira",
    "Ermia", "Esmehan", "Farangis", "Fariba", "Farnaz", "Farrokh", "Farzaneh", "Fereshteh", "Firouzeh", "Ghazaleh",
    "Golara", "Golbanou", "Goleen", "Golestan", "Golnaz", "Golrokh", "Golshan", "Golzar", "Hanieh", "Hasti",
    "Hedieh", "Helia", "Helnaz", "Helya", "Hengameh", "Homa", "Hooria", "Iris", "Kimia", "Kiana",
    "Ladan", "Laleh", "Lamia", "Leila", "Leyla", "Liana", "Mahdieh", "Mahgol", "Mahtab", "Mahvash",
    "Mana", "Mandana", "Marjan", "Mehrnaz", "Mehrnoosh", "Mehry", "Melina", "Melisa", "Melodi", "Melorin",
    "Mina", "Minou", "Mitra", "Mona", "Monir", "Morsal", "Nafiseh", "Nahal", "Narges", "Nasim",
    "Nasrin", "Nazanin", "Negin", "Nerina", "Niloufar", "Nina", "Nioosha", "Nushin", "Parastoo", "Parinaz",
    "Parisa", "Parnaz", "Parya", "Parvin", "Pegah", "Pooneh", "Poupak", "Raha", "Rana", "Rasa",
    "Roya", "Rozhan", "Rozhin", "Roxana", "Sadaf", "Sahar", "Sana", "Sanaz", "Sarina", "Shabnam",
    "Shadi", "Shahla", "Shakiba", "Sharareh", "Shirin", "Shiva", "Shokouh", "Sima", "Simin", "Soma",
    "Sonia", "Soraya", "Soudabeh", "Souzan", "Suzan", "Tara", "Tarlan", "Tina", "Tirgan", "Vanda",
    "Vida", "Yasaman", "Yasmin", "Zahra", "Zalal", "Zarrin", "Ziba", "Zohreh", "Zoya", "Zyra",
     "Aariana", "Afarin", "Afra", "Aidaan", "Ainoosh", "Aiza", "Alara", "Alida", "Alineh", "Amira",
    "Anisa", "Aralia", "Ariaa", "Arisha", "Aryani", "Asal", "Ashena", "Asoo", "Atieh", "Ayla",
    "Azana", "Azarrah", "Azin", "Barana", "Bebin", "Belira", "Beneh", "Bennisa", "Berah", "Beza",
    "Bita", "Bonnisa", "Carmia", "Dahira", "Delana", "Delba", "Delisa", "Delsa", "Deria", "Dorna",
    "Dorsa", "Doryan", "Edila", "Ela", "Elaria", "Elasha", "Elma", "Elvara", "Eman", "Emirah",
    "Eriana", "Eshra", "Esmira", "Esna", "Eveena", "Fadwa", "Fahrah", "Farimah", "Farina", "Farrah",
    "Farris", "Farya", "Fayzah", "Feriel", "Firuzeh", "Fiza", "Fouzia", "Freha", "Freyra", "Ghadir",
    "Ghariba", "Ghasar", "Ghazana", "Gila", "Golaneh", "Golaria", "Golshan", "Golzhan", "Hadeh", "Hadiss",
    "Haili", "Haleh", "Hamia", "Hanifa", "Hanina", "Hanita", "Hanya", "Havah", "Havira", "Hazara",
    "Helya", "Hesara", "Hiara", "Hira", "Honaira", "Hosna", "Ibaa", "Ibira", "Ila", "Ilana",
    "Ilara", "Imaneh", "Imara", "Ina", "Ishana", "Ishrana", "Itan", "Iva", "Iyana", "Izna",
    "Jahida", "Jahana", "Jalina", "Jasra", "Javena", "Javiera", "Jaza", "Jemira", "Jenina", "Jihana",
    "Jilza", "Joana", "Jumana", "Kaamilah", "Kaarina", "Kahina", "Kaira", "Kalira", "Kalista", "Kamira",
    "Karama", "Karida", "Kavina", "Keena", "Khansa", "Kheira", "Kiana", "Kira", "Kyra", "Laira",
    
]


male_names = [
    "Adrin", "Aiden", "Amin", "Amir", "Anoush", "Arad", "Aram", "Arian", "Arman", "Armin",
    "Arsham", "Aryan", "Ashkan", "Babak", "Bardia", "Behnam", "Behrooz", "Behzad", "Borhan", "Cyrus",
    "Danial", "Darab", "Dariush", "Dena", "Dior", "Ebrahim", "Emad", "Erfan", "Eshagh", "Farhad",
    "Fariborz", "Faramarz", "Faraz", "Farrokh", "Feryad", "Firooz", "Foad", "Ghasem", "Ghobad", "Hamid",
    "Hamed", "Hami", "Haroon", "Hashem", "Hassan", "Hedayat", "Hesam", "Hooshang", "Hooshyar", "Hossein",
    "Iraj", "Isa", "Kamran", "Karim", "Kaveh", "Kian", "Kiarash", "Keyan", "Khosrow", "Kianoush",
    "Koosha", "Kourosh", "Mahdi", "Mahyar", "Mani", "Mansour", "Masoud", "Matin", "Mehrab", "Mehrdad",
    "Mehran", "Mehryar", "Milad", "Mirza", "Mohammad", "Mokhtar", "Mostafa", "Morteza", "Mousa", "Nader",
    "Nima", "Omid", "Parsa", "Parviz", "Pejman", "Pouria", "Rahim", "Rahman", "Ramin", "Ramtin",
    "Reza", "Roham", "Roshan", "Saeed", "Saman", "Sasan", "Sattar", "Shahab", "Shahin", "Shahrokh",
    "Siavash", "Soheil", "Sorush", "Taher", "Taha", "Tirdad", "Touraj", "Vahed", "Varoosh", "Yahya",
    "Aadin", "Aadran", "Aalar", "Aarash", "Aban", "Abeel", "Abeir", "Adeel", "Adrian", "Afam",
    "Afnan", "Aghil", "Ahvaz", "Aidan", "Ailaan", "Airaj", "Akbar", "Aliyan", "Aliz", "Amal",
    "Amar", "Amel", "Amirali", "Ammad", "Amnaz", "Amza", "Andar", "Andi", "Andira", "Anushir",
    "Arbah", "Ardin", "Areef", "Arsalan", "Artaban", "Arveen", "Aryon", "Ashay", "Ashfaque", "Asif",
    "Asiyaan", "Aswan", "Asyaar", "Azaan", "Azhan", "Azin", "Azmat", "Baba", "Bahram", "Balazir",
    "Balur", "Bamdad", "Banafsheh", "Baraz", "Barham", "Barkhar", "Basil", "Bazir", "Behan", "Behnoud",
    "Benzir", "Berdan", "Bert", "Bija", "Bilal", "Bora", "Borhan", "Bouzar", "Brahim", "Brem",
    
]


last_names = [
    "Abadi", "Afshar", "Ahangar", "Ahmadi", "Akhavan", "Amini", "Ardalan", "Aria", "Asadi", "Ashouri",
    "Azad", "Bagheri", "Bahar", "Bakhshi", "Barzegar", "Behnam", "Boroumand", "Chaman", "Danesh", "Dehghan",
    "Doust", "Ebrahimi", "Eftekhar", "Fakhri", "Farahani", "Farrokhi", "Fazeli", "Firouz", "Forough", "Ghaffari",
    "Ghasemi", "Golzar", "Haddad", "Hakimi", "Hamidi", "Hashemi", "Hedayati", "Hosseini", "Jamali", "Javan",
    "Kamal", "Kamali", "Karimi", "Kazemi", "Khosravi", "Kiani", "Mahdavi", "Mansouri", "Marandi", "Mazaheri",
    "Mehraban", "Mehrjou", "Mirzadeh", "Mohammadi", "Moradi", "Mousavi", "Nabavi", "Nazari", "Nouri", "Oskouei",
    "Parsa", "Parvaneh", "Rahimi", "Ramin", "Rastegar", "Ravanshad", "Rezvani", "Rohani", "Rostami", "Saadat",
    "Sadat", "Salehi", "Sattari", "Shahbaz", "Shahrokh", "Shokouhi", "Soltani", "Tabesh", "Tabrizi", "Tavakoli",
    "Afshar", "Ahangaran", "Ahmadpour", "Alavi", "Amini", "Anousheh", "Ardalan", "Asadi", "Ashkanian", "Bagherzadeh",
    "Bahadori", "Bakhshandeh", "Baradaran", "Bardiya", "Bazargan", "Behdani", "Behrouzian", "Borhani", "Chakameh", "Daryabi",
    "Dehghanian", "Dolatabadi", "Ebrahimi", "Eftekhar", "Esfahani", "Farhangi", "Fard", "Farhadpour", "Fathian", "Firouzi",
    "Foroughian", "Ghaffar", "Ghaffari", "Ghasemi", "Golpar", "Golshan", "Hamidi", "Hashemi", "Hedayati", "Jamshidian",
    "Javadian", "Kamalpour", "Karimian", "Kazemi", "Khanlari", "Khosrowshahi", "Mahdavi", "Mansoorian", "Mazaheri", "Mehrabi",
    "Abarian", "Aftabi", "Ahang", "Ahmadi", "Akbari", "Alinia", "Amiri", "Anvari", "Aram", "Arasteh",
    "Arbab", "Arefian", "Ariafar", "Armanian", "Aryan", "Ashouri", "Atash", "Atefi", "Avazian", "Azadeh",
    "Azimi", "Baghban", "Baghdadi", "Bahrani", "Bakhshi", "Balouchi", "Baran", "Barazandeh", "Bazrafkan", "Behnam",
    "Boroumand", "Chavoshi", "Chogan", "Dabiri", "Dadian", "Danesh", "Danial", "Davarpanah", "Deljoo", "Derakhshan",
    "Doosti", "Dousti", "Eghtesadi", "Ehsani", "Elahi", "Esbati", "Esmaeili", "Etemadi", "Fallahi", "Fanaei",
    "Farahmand", "Fardad", "Farhadian", "Farhadi", "Farhang", "Farrokh", "Farsi", "Fathollahi", "Fazeli", "Firouzan",
    "Fotouhi", "Fozouni", "Ganjali", "Ghadiri", "Gharavi", "Gharibi", "Ghassemi", "Ghassemloo", "Golestan", "Golmohammadi",
    "Golpayegani", "Hadian", "Hamayeli", "Hamidi", "Hanaei", "Hashemian", "Heshmatian", "Hosseinian", "Hosseinzadeh", "Jahangiri",
    "Jalali", "Jamali", "Jami", "Jandaghi", "Javadi", "Javaheri", "Jomeh", "Kadivar", "Kamalvandi", "Karami",
    "Karimi", "Katib", "Kazemian", "Khanjani", "Khatami", "Khodayari", "Khorshidi", "Khorrami", "Khoushdel", "Kiaei",
    "Kiani", "Kordestani", "Kousari", "Lahouti", "Lari", "Mahdian", "Mahmoudian", "Majd", "Malekian", "Maleki",
    "Malekan", "Mashhadi", "Mazandarani", "Maziar", "Mazloumi", "Mehraban", "Mehrabi", "Mehrjoo", "Mehrnia", "Minaei",
    "Mir", "Mirafzali", "Miran", "Mirfakhraei", "Mirhosseini", "Mirzaei", "Modarresi", "Mohajer", "Mohammadi", "Mokhtari",
    "Monajemi", "Moosavi", "Mozaffari", "Naderi", "Namazi", "Naseri", "Nasseri", "Nazemi", "Neshat", "Nikdel",
    "Nikjoo", "Nikouei", "Noorani", "Noroozi", "Nourbakhsh", "Omidi", "Orouji", "Ostad", "Pahlavan", "Pakdel",
    "Panahi", "Parastoo", "Parsa", "Parvin", "Pashaei", "Pourali", "Pourmand", "Pourshabanan", "Rahimi", "Rahmati",
    "Rajabi", "Ramezani", "Ranjbar", "Ravandi", "Razavi", "Riahi", "Roohani", "Rostami", "Roudaki", "Roudbar",
    "Ruhollah", "Saberi", "Sadatian", "Safaei", "Safaian", "Sahebi", "Sahraeian", "Samadi", "Sanayei", "Sarafi",
    "Sarhang", "Sarmadi", "Sepehri", "Shafiei", "Shahidi", "Shahmoradi", "Shahraki", "Shahsavari", "Shakouri", "Sharifi",
    "Sheibani", "Shirazi", "Shokoohi", "Soroush", "Sohrabi", "Tabari", "Tafazoli", "Taheri", "Tajbakhsh", "Talebian",
    "Tavakkoli", "Tehrani", "Torabi", "Vahdat", "Vahidi", "Vakili", "Varasteh", "Yaghoubi", "Yazdani", "Zamani",
    "Zare", "Zarrabi", "Zavarei", "Zoghi", "Zomorrodi", "Zorratab", "Abadian", "Afarian", "Aghayan", "Ahourian", "Akhtarian", "Alavian", "Amirian", "Ananian", "Ardalanian", "Ardaniyan",
    "Ardalanian", "Arefian", "Arianian", "Armanian", "Ashkanian", "Atashian", "Azinian", "Azizian", "Badian", "Baghiyan",
    "Baghouyan", "Baharian", "Bakhshiyan", "Balayan", "Bamiyan", "Banafshian", "Baradian", "Bazrafshanian", "Behnamian", "Boroumandian",
    "Chakarian", "Chavoshian", "Dabirian", "Daneshian", "Danialian", "Daryan", "Davarpanian", "Delarian", "Derakhshian", "Doostian",
    "Ebrahimpouryan", "Eftekharian", "Elahian", "Esfahaniyan", "Etemadian", "Fallahian", "Farahmandian", "Farhangian", "Farhadian", "Faridiyan",
    "Farsiyan", "Fathian", "Fazelian", "Firouzian", "Fotouhian", "Ghadirian", "Ghafourian", "Ghasemian", "Golestanian", "Golparian",
    "Golshanian", "Hamidian", "Hashemian", "Hedayatian", "Jamshidian", "Javadian", "Javaherian", "Jomhourian", "Kadivarian", "Kamalvadian",
    "Karimian", "Kazemian", "Khademian", "Khalilian", "Khodayarian", "Khorshidian", "Khorramian", "Khosravian", "Kiani", "Lahoutian",
    "Mahdavian", "Mahmoudian", "Majidian", "Malekian", "Mashadian", "Mazaherian", "Mehrabanian", "Mehrabi", "Mehrjooian", "Mehrvarzian",
    "Mirafzalian", "Mirian", "Mirjahanian", "Mirrahimian", "Mirzaian", "Modarresian", "Mohajerian", "Mohammadian", "Mokhtarrian", "Moosavian",
    "Mozaffarian", "Naderian", "Nassirian", "Nazarian", "Nikdelian", "Nikjouyan", "Nikouian", "Norouzian", "Nourian", "Ostadian",
    "Pakdamanian", "Pakdelian", "Panahian", "Parsaian", "Parvizian", "Pashaeian", "Pourarian", "Pourfarzadian", "Pourmandian", "Rahimian",
    "Rahmanian", "Rahnamaian", "Rajabian", "Ramezanian", "Ranjbarian", "Razavian", "Roohanian", "Rostamian", "Roudbarian", "Sabzian",
    "Sadeghian", "Safavian", "Sahabian", "Sahraian", "Samaian", "Sarmadian", "Sarrafian", "Shafian", "Shahbaziian", "Shahedian",
    "Shahsavarian", "Shakibian", "Sharafian", "Sharifian", "Sheibanian", "Shirazian", "Shokoohian", "Soroushian", "Sohrabian", "Tabarian",
    "Taherian", "Tajbakhshian", "Talebian", "Tavakolian", "Tehranian", "Torabian", "Toranjian", "Vahdatian", "Vahidyan", "Vakilian",
    "Varastehian", "Yaghoubian", "Yazdanian", "Zamaniyan", "Zandian", "Zareian", "Zarrabian", "Zavareian", "Zoghiyan", "Zomorrodian"

    
]



while True:
    gender = input('enter the gender: ')
    last_name = choice(last_names)
    if gender == 'f':
        first_name = choice(female_names)
    elif gender == 'm':
        first_name = choice(male_names)
    else:
        print('invalid input')
        continue

    print(('-' * 33) + f'\n\n{first_name} - {last_name}\n\n' + ('-' * 33))