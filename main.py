print('''
++++++++++++++++++++++++++++++++++++++++++++++++++++++
||               Degvielas kalkulators              ||
||                  Anna Minno 10.b                 ||
++++++++++++++++++++++++++++++++++++++++++++++++++++++
''')
print('''
Sveiki! 
Lūdzu, ievadiet degvielas daudzumu, kuru Jūs vēlāties pārvēst citā mērvienībā. Ja Jūs lietojat decimdaļas, tad lietojiet punktu.
''')
while True:  #skaitla parbaude
    print('Ievadiet daudzumu,kuru Jūs vēlāties pārvēst citā mērvienībā:')
    daudzums = input()
    try:
        daudzums = float(daudzums)
    except:
        print('Lietojiet tikai skaitļus!')
        continue
    if daudzums < 0:
        print('Kluda! Skaitlim jabut vairak par 0!')
        continue
    break
print(f'Degvielas daudzums ir {daudzums}.')
mervieniba = input("Uz kuru mervienibu parverst litriem(l) vai galoniem (g)?")
#mervienibas parversana
print(mervieniba)
if mervieniba == "l":
    resultats_litri = daudzums * 3.79
    print(f"Litros tas bus:{resultats_litri:.{3}f}")
else:
    resultats_galoni = daudzums / 3.79
    print(f"Galonos tas bus:{resultats_galoni:.{3}f}")
#degvielas daudzums uz S
print("Tagad paskaitisim uz cik lielu attalumu jums pietiks degvielas")
izvele = input( "Izveleties degvielas paterinu: litri/100km (k) vai galons/judze (j)")
if izvele == "k":
    paterina_km = float(input("Ievadiet litru paterinu uz 100 kilometriem: "))
    cels = resultats_litri * (100 / paterina_km)
    print(f'Pietiks uz {cels:.{3}f} kilometriem.')
else:
    paterina_judze = float(input("Ievadiet galonu pateriņu uz judzem : "))
    attalums = resultats_galoni * (1 / paterina_judze)
    print(f'Pietiks uz {attalums:.{3}f} judzēm.')
#Beigas
print("Paldies, ka lietojat musu programmu ")
print('''
++++++++++++++++++++++++++++++++++++++++++++++++++++++
''')