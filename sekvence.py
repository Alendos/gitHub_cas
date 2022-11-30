# brojevi = [9, 1, 3, 2, 5, 8, 7]
# brojevi.sort()
# brojevi.reverse()
# print(brojevi)


# brojevi = [9, 1, 3, 2, 5, 8, 7]

# while True:
#     izvrsena_zamena = False
#     for i in range(1,len(brojevi)):
#         print(brojevi[i], "poredim sa", brojevi[i-1])
#         if brojevi[i] < brojevi [i-1]:
#             privremena = brojevi[i]
#             brojevi[i] = brojevi[i-1]
#             brojevi[i-1] = privremena
#             izvrsena_zamena = True
#     if izvrsena_zamena == False:
#             break
# print(brojevi)


# proizvod = ["Phone", "TV", "Computer"]
# cene = [155.95, 180.35, 199.99]
# for i in range(len(proizvod)):
#     print(proizvod[i],cene[i])


# automobili = ["Audi","BMW","Yugo","Citroen","Kia","Peugeot"]
# for i in range(len(automobili)):
#     if i == 2:
#         print("Ovo je Aleksandrin automobil:", automobili[i])


proizvodi = [
    ["iphone 11","samsung s22","xiaomi x3" ], 
    ["acer", "macbook","dell"], 
    ["ipad","samsung galaxy tab","xiaomi tablet"]
            ]
# print(proizvodi[0][0])

# telefoni = ["iphone 11","samsung s22","xiaomi x3" ]
# laptopovi = ["acer", "macbook","dell"]
# tableti = ["ipad","samsung galaxy tab","xiaomi tablet"]

# proizvodi = [telefoni, laptopovi, tableti]

# for kategorija in proizvodi:
#     for i in kategorija:
#         print(i)

# for i in range(len(proizvodi)):
#     # print(proizvodi[i])
#     for j in range(len(proizvodi[i])):
#         print(proizvodi[i][j])


# hrana = [["Cokolada", "Bombone", "Palacinke"], ["Sarma", "Musaka", "Kiseli kupus"], ["Pecena paprika", "Ajvar", "Sopska"]]

# for kategorija in hrana:
#     for jelo in kategorija:
#         print(jelo)

# ime = "Sofija"

# poruka = f"Cao {ime} !!!"
# print(poruka)


biblioteka = []
while True:
    print("Odaberi komandu: 1-unos, 2-prikaz, 3-brisanje, > 3 izlaz")
    komanda = int(input("Unesite komandu: "))

    if komanda == 1:
        naslov = input("Unesite naslov: ")
        autor = input("Unesite autora: ")
        isbn = int(input("Unesite isbn: "))
        biblioteka.append([naslov, autor, isbn])
        print("Dodata knjiga")
    if komanda == 2:
        for i in biblioteka:
            for x in i:
                print(x)
    if komanda == 3:
        kljucna_rec = input("Unesite naziv knjige koje zelite da obrisem:")
        for i in biblioteka:
            for x in i:
                if x == kljucna_rec:
                    biblioteka.remove(i)
                    print("Knjiga je obrisana")
    if komanda > 3:
        quit()