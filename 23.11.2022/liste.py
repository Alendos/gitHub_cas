# osoba = ["Sofija", 25, "plava", False]
# for x in range(len(osoba)):
#     print(osoba[x])

# for x in osoba:
# #     print(x)

# voce_i_povrce = ['jabuka', 'belu luk', 'crni luk', 'banana', 'mandarina', 'lubenica', 'krastavac']
# # for x in voce_i_povrce:
# #     print(x)

# # for x in range(len(voce_i_povrce)):
# #     print(voce_i_povrce[x])

    
# for indeks, vrednost in enumerate(voce_i_povrce):
#     print ("Indeks:", indeks, "Stavka:", vrednost)

# automobili = ["Citroen", "BMW", "Opel", "Kia","Jugo"]
# for i,v in enumerate(automobili):
#     if len(v) == 3:
#         print (v)
#     # print("Pozicija:",i,"Auto:", v)
        
# automobili.append("Mercedes")

# automobili[2] = "Opel Corsa"
# print(automobili)
# automobili[3] = "Kia Sportage"

# del automobili[3]
# print(automobili)
# automobili.remove ("BMW")
# car  = automobili.pop(0)
# print(car)

# automobili.clear()
# print(automobili)


# automobili = ["Citroen", "BMW", "Opel", "Kia","Jugo","Peugeot", "Audi"]
# autombili_akcija = automobili[1:4]
# print(autombili_akcija)


a = [3,7,1,9,2,4,5,12]
odd = []
even = []

for x in a:
    even.append(x) if x % 2 == 0 else odd.append(x)
print(odd,even)