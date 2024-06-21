"""Napisati regex za provjeru validnsti unosa e-maila. E-mail mora biti formata ime.prezime@fpmoz.sum.ba.
Nakon toga napisati regex za provjeru eduId koji mora biti formata iprezime@sum.ba, gdje je prvo slovo imena
+prezime. X predstavlja bilo moji broj(moze ici u beskonacnost), a taj broj ne mora postijati (moze biti samo iprezime@sum.ba)
Od korisnika zatražiti unos maila i eduId te ispisati uspjesnost. """

import re

email = input("Unesite email: ")
eduId = input("Unesite email za eduId: ")

fpmoz = r'^[a-z]+\.[a-z]+@fpmoz\.sum\.ba$'
edu = r'^[a-z][a-z]+[0-9]*@sum\.ba$'

if re.match(fpmoz, email):
    print("E-mail je dobar.")

else:
    print("E-mai nije dobar")

if re.match(edu, eduId):
    print("E-mail je dobar.")

else:
    print("E-mai nije dobar")
