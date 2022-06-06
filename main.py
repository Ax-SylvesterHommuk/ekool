from classes import *

# Loon uue kooli
Kool = Kool()
Kool.adding_nimi()

# Loon listid
all_õpetajas_list = []
all_õpilased_list = []

# Loon 5 uut õpetajat
print("Loon õpetajad...")

for i in range(5):
    õpetaja = õpetaja()
    õpetaja.naming_õpetajas()
    Kool.adding_õpetaja(õpetaja)
    all_õpetajas_list.append(õpetaja)
    
# Loon 10 uut õpilast
print("Loon õpilased...")

for i in range(10):
    õpilane = õpilane()
    õpilane.naming_õpilane()
    all_õpilased_list.append(õpilane)
    
# Loon teise kooli
Kool2 = Kool()
Kool2.adding_nimi()

# Kõigi õpilaste lisamine esimesse kooli ja teisse kooli
for i in all_õpilased_list:
    Kool.registering_õpilane_2kool(i)
    
for i in all_õpilased_list:
    Kool2.registering_õpilane_2kool(i)
    
# Vea vaatlus
if Kool2.õpilased.__len__() == 0:
    print(f"!!! Viga ei õnnestunud registreerida teise kooli õpilasi !!!")
    
pe = Teema()
pe.naming_teema("PE")
Kool.adding_teema(pe)
pe.adding_õpetaja(Kool.õpetaja[0])
pe.adding_õpetaja(Kool.õpetaja[1])
pe.adding_õpetaja(Kool.õpetaja[2])

it = Teema()
it.naming_teema("IT")
Kool.adding_teema(it)
it.adding_õpetaja(Kool.õpetaja[3])

ehitus_klass = Teema()
ehitus_klass.naming_teema("Ehituse klass")
Kool.adding_teema(ehitus_klass)
ehitus_klass.adding_õpetaja(Kool.õpetaja[4])

itdeveloper = Hinded()
itdeveloper.naming_grade("IT Arendaja")
Kool.adding_grades(itdeveloper)

chef = Hinded()
chef.naming_grade("Ehitaja")
Kool.adding_grades(chef)

pe.add_grade_to_teema(itdeveloper)
pe.add_grade_to_teema(chef)
it.add_grade_to_teema(itdeveloper)
ehitus_klass.add_grade_to_teema(chef)

# Hinnete vaatlus
b = 0
for i in Kool.õpilased:
    if b < 5:
        i.adding_grade(itdeveloper)
    if b >= 5:
        i.adding_grade(chef)
    b = b + 1
    
for i in itdeveloper.õpilased:
    i.registering_to_teema(it)
    i.registering_to_teema(pe)
for i in chef.õpilased:
    i.registering_to_teema(ehitus_klass)
    i.registering_to_teema(pe)
    
c = 0
for i in itdeveloper.õpilased:
    if c == 0:
        i.add_a_mark(1, it)
        i.add_a_mark(2, pe)
    if c == 1:
        i.add_a_mark(3, it)
        i.add_a_mark(4, pe)
    if c == 5:
        i.add_a_mark(5, it)
        i.add_a_mark(5, pe)
    elif c > 1:
        i.add_a_mark(3, it)
        i.add_a_mark(3, pe)
    c = c + 1
d = 0
for i in chef.õpilased:
    if d == 0:
        i.add_a_mark(1, ehitus_klass)
        i.add_a_mark(2,pe)
    if d == 1:
        i.add_a_mark(3, ehitus_klass)
        i.add_a_mark(4,pe)
    if d == 5:
        i.add_a_mark(5, ehitus_klass)
        i.add_a_mark(5, pe)
    elif d > 1:
        i.add_a_mark(3, ehitus_klass)
        i.add_a_mark(3, pe)
    d = d + 1
    
    
for i in itdeveloper.õpilased:
    i.show_teema_stats()
for i in chef.õpilased:
    i.show_teema_stats()
    
Kool.show_grades()
Kool.show_õpetaja()
Kool.show_Teema()
Kool.show_õpilased()

for i in Kool.õpetaja:
    i.show_teemas()
Kool.show_Kool_ranking(Kool, Kool.õpilased)