from countries import countries 
import random


odabrani = random.sample(countries, 26)
finalisti = []
for drzava, izvodjac, pjesma in odabrani:
    rodabrani = {
        "drzava": drzava,
        "izvodjac": izvodjac,
        "pjesma": pjesma,
        }
    finalisti.append(rodabrani)
bodovi = [12, 10, 8,7,6,5,4,3,2,1]
for drzava, izvodjac, pjesma in countries:
    bez_drzave = []
    for item in finalisti:
        if item["drzava"] != drzava:
            bez_drzave.append(item)
    za_bodovanje = random.sample(bez_drzave, 10)
brojac = 0
for bod in bodovi:
    naziv_drzave = za_bodovanje[brojac]["drzava"]
    for finalist in finalisti:
        if finalist["drzava"] == naziv_drzave:
            finalist["bodovi"] = finalist.get("bodovi", 0) + bod
            break
    brojac += 1

            
print(finalisti)
    
