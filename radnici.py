"""
Potrebno je kreirati evidenciju odrađenih sati i isplata radnika tvrtke koja se bavi dostavljanjem.
Generirati 15 radnika random imena i prezimena iz ponuđene liste, te njegovu satnicu slučajnim odabirom floata između 4 i 6 zaokruženu na 2 decimale.
Sve radnike spremiti u listu radnika, a jedan radnik je rječnik oblika 
{“ime”: “John”, “prezime”: “Doe”, “satnica”: 5.20}
Iterirati kroz sve radnike i dodati im novo svojstvo “tjedni_sati” koji generira cijeli broj odrađenih sati u 1 tjednu od 20 do 30.
Nakon toga napraviti obračun množenjem satnice sa tjednim satima i rezultate spremiti u listu tuple-a (trojki) oblika (ime, prezime, isplata).
Iteriranjem ispisati podatke, a zatim izračunati ukupnu i prosječnu isplatu za taj tjedan.
Ispisati Imena svih radnika koji imaju isplatu iznad prosječne.


imena = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John', 'Roseanna', 'Gerald', 'George',
'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan', 'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']

prezimena = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez', 'Cleary', 'Hoyman', 'Hall',
'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith', 'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']
"""
import random
imena = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John', 'Roseanna', 'Gerald', 'George',
'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan', 'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']

prezimena = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez', 'Cleary', 'Hoyman', 'Hall',
'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith', 'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']

#kreiranje liste radnika sa imenom prezimenom i satnicom
radnici = []
print("-----------------------------------")
while len(radnici) <= 15:
    rijecnik = {}
    ime = random.choice(imena)
    prezime =random.choice(prezimena)    
    satnica =round(random.uniform(4, 6), 2)
    if ime not in rijecnik and prezime not in rijecnik:
        rijecnik["Ime"] = ime
        rijecnik["Prezime"] = prezime
        rijecnik["Satnica"] = satnica
    radnici.append(rijecnik)
print(f"Radnici su: {radnici}\n")
print("-----------------------------------")
#dodavanje tjednih sati
tjedni_Sati = []
for i in radnici:
    sat = random.randint(20,30)
    i.update({"tjedni_sati":sat})
    tjedni_Sati.append(i)

#ispisivanje radnika jedan ispod drugog
for radnik in radnici:
    print(f"Radnik: {radnik}")
print("-----------------------------------")
#obracun i svi radnici koji imaju plcau iznad prosjecne
obracuni = []
suma = 0
brojac = 0
iznad_prosjeka= []
for radnik in tjedni_Sati:
    ime = radnik.get("Ime")
    prezime =radnik.get("Prezime")
    sat = radnik.get("Satnica")
    tjedni_sat = radnik.get("tjedni_sati")
    obracun = round(sat * tjedni_sat, 2)
    obracuni.append((ime, prezime, obracun))
    suma += obracun
    brojac += 1
    prosjek = suma /brojac
    if obracun > prosjek:
        iznad_prosjeka.append(ime)
print(f"Obracun za radnike {obracuni}\n")
print("-----------------------------------")
print(f"Prosjek je: {prosjek}\n")
print("-----------------------------------")
print(f"Osobe sa placom iznad prosjeka: {iznad_prosjeka}")
