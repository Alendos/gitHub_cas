# x = 10

# if x > 0:
#     print("x je pozitivan broj")
# else:
#     print("x je negativan broj")

# print("Izvrsava se u svakom slucaju")


#primer 1
# vozilo_u_pokretu = True
# brzina = 50

# if vozilo_u_pokretu:
#     print("Vozilo se krece")
#     print("Proverite i brzinu")
#     if brzina > 50:
#         print("Prekoracili ste brzinu")
#     print("Ovo izvrsavam kolika god da je brzina")
#     if brzina <=  50:
#         print("Niste prekoracili brzinu")

# if vozilo_u_pokretu == False:
#     print("Vozilo se ne krece")


#primer 2
#1 - prikaz; 2 - kupovina; 3 - izlaz

# proizvod = "Duks"
# cena = 3000
# komanda = int(input("Unesite komandu: "))

# if komanda == 1:
#     print("Pirkazi proizvode")
#     print("Proizvod:", proizvod, ", " "Cena:", cena)
# if komanda == 2:
#     stanje = int(input("Unesite stanje na racunu: "))
#     print("Kupovina")
#     if stanje >= cena:
#         print("Mozete kupiti duks")
#     else:
#         print("Nemate dovoljno novca")
# if komanda == 3:
#     print("Izlaz")
#     exit()


#primer3
# broj = 5

# if broj > 0:
#     print("Broje je veci od 0")
# else:
#     print("Broj nije veci od 0")


#primer4
# marija = False
# ksenija = True
# katarina = False
# devojka_na_dejtu = ""

# if marija:
#     devojka_na_dejtu = "Marijom"
# elif ksenija:
#     devojka_na_dejtu = "Ksenijom"
# elif katarina:
#     devojka_na_dejtu  ="Katarinom"
# else:
#     devojka_na_dejtu = "Sofijom"
# print("Izlazis sa", devojka_na_dejtu)


#primer 5
# automobil_polovan = False
# godiste = 2022
# boja = "Crna"

# if automobil_polovan or godiste > 2017 and boja == "Crna":
#     print("Kupujem")
# if not automobil_polovan :
#     print("Automobil je polovan.")


#primer6
import random
# broj = int(input("Unesite jedan broj od 1 do 100: "))
# nasumican_broj = random.randint(1,100)
# print("Nasumicni broj je:", nasumican_broj)
# if broj >100 or broj <1:
#     print("Morate uneti broj od 1 do 100, probaj opet")
# elif broj > nasumican_broj:
#     print("Vas broj je veci od nasumcinog")
# elif broj < nasumican_broj:
#     print("Vas broj je manji od nasumicnog")
# else:
#     print("Vas broj je isti kao i nasumicni broj")



#primer 7
# pol = input("Unesite m ili z:")
# poruka = "Hey mister" if pol == "m" else "Hey miss"

# print(poruka)



#primer8
# jesen = True
# popularan_proizvod = "Ajvar" if not jesen else "Sladoled"
# print(popularan_proizvod)
