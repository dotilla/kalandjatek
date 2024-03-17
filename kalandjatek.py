import time


def main():
  print("Üdvözöllek Komorka Kalandjátékában!\n")
  time.sleep(1)
  print(
      "Idén végre eljutottál a Fishing on Orfűre, nézzük, kivel futhatsz össze, miközben hajnali kettőkor gyrost vadászol!\n(Csak a számot írd be, majd üss entert!)\n"
  )
  time.sleep(1)
  print("Induljunk el!\n")
  time.sleep(1)

  while True:
    print("\nVálassz egy frontembert, akivel találkozni szeretnél:")
    print("1. Beck Zoli (30y)")
    print("2. Szendrői Csaba (Elefánt)")
    print("3. Bérczesi Robi (hiperkarma)")
    print("4. Csepella Olivér (Csaknekedkislány)")
    print("5. Krúbi")
    print("q. Kilépés")

    valasz = input("Válasz: ")

    if valasz == '1':
      beck_zoli()
    elif valasz == '2':
      szendroi_csaba()
    elif valasz == '3':
      berczesi_robi()
    elif valasz == '4':
      csepella_oliver()
    elif valasz == '5':
      krubi()
    elif valasz.lower() == 'q':
      print("Viszlát!")
      break
    else:
      print("Nem értem, próbáld újra!")


def beck_zoli():
  print("\nBeck Zolival, a 30y énekesével találkoztál!")
  time.sleep(1)
  print(
      "Beck Zoli: Heló! Ha van egy kis időd, akkor elmesélhetem a házunk történetét, mit szólsz?"
  )
  time.sleep(1)
  print("1. Meghallgatom, Zoli")
  print("2. Ajaj, ennyi időm azért nincs, bocsi")

  valasz = input("Válasz: ")

  if valasz == '1':
    print(
        "\nHát én panel gyerek vagyok, panelbe' nőttem föl, csajom is panel, nem laktunk soha máshol, csak panel lakásba', és állatira akartuk, hogy egyszer legyen egy ilyen házunk. Rátaláltunk Pécsen egy ilyen tök jó kis házra, amit asszem senki más nem akart volna megvenni, mer' videózöld színe volt, és kicsi is volt, meg mittudomén, de nem az volt a lényeg, hanem volt valami jó érzésünk vele kapcsolatban. Emlékszem, mikor megvettük a házat, akkor a Pinyon egyszer csak azt mondta, hogy milyen jó, hogy megvettük a házat, mer' látod mindenkinek kell, hogy legyen egy kis saját ege. Nem arra gondolt, hogy földet vettél, vagy, hogy házat vettél, hanem, hogy állsz valahol és ha fölnézel, akkor az a kihasított darab, az egy picit a tiéd, szóval, hogy van honnan nézned fölfelé. És ez szerintem ilyen szép metaforája annak, hogy asszem a ház legfőbb értelme az valami ilyesmi, hogy figyelj, nem az udvart, vagy a kertet keríted le, vagy mittudomén, hanem van valami ilyen...ilyen helyed. Na, köszi, hogy meghallgattad, most mennem kell, koncertre készülünk."
    )
  elif valasz == '2':
    print("Viszlát, Zoli!")


def szendroi_csaba():
  print("\nSzendrői Csabával, az Elefánt énekesével találkoztál!")
  time.sleep(1)
  print(
      "Szendrői Csaba: Helló! Mit szólnál, ha felolvasnám neked a kedvenc versem a Féyn című kötetemből?"
  )
  time.sleep(1)
  print("1. Olvasd, Csabi")
  print("2. Nem vagyok verses kedvemben")

  valasz = input("Válasz: ")

  if valasz == '1':
    print(
        "\nEzt a verset\nazért írtam,\nmert hallani akartam\nsercegni a ceruzát a papíron.\n\nEnnek a versnek\nnincs mondanivalója.\nEnnek a versnek\nértelme van.\n\nNa, köszi, hogy benéztél, de most megyek, le kell mosnom Babakéket."
    )
  elif valasz == '2':
    print("Viszlát, Csabi!")


def berczesi_robi():
  print("\nBérczesi Robival, a hiperkarma énekesével találkoztál!")
  time.sleep(1)
  print(
      "Bérczesi Robi: Szervusz! Eláruljak magamról valamit, amit valószínűleg még nem tudsz?"
  )
  time.sleep(1)
  print("1. Mondd, Robi")
  print("2. Felejtsd el, nem tudsz olyat mondani, amit ne tudnék")

  valasz = input("Válasz: ")

  if valasz == '1':
    print(
        "\n5 éves koromban megtanultam írni, ugyanis van egyfajta ilyen madár-és tollfóbiám, és hát a szüleim falun libáztak, kétezer libájuk volt, így aztán az udvarra már eleve esélyem sem volt kimenni. Ezzel töltöttem a gyerekkoromat, ötéves koromtól bezárkóztam a szobámba és egy sci-fi regényen dolgoztam. Egyébként a mai napig nem fejeztem be, megyek is, folytatom."
    )
  elif valasz == '2':
    print("Viszlát, Robi!")


def csepella_oliver():
  print("\nCsepella Olivérrel, a Csaknekedkislány énekesével találkoztál!")
  time.sleep(1)
  print(
      "Csepella Olivér: Helló! Gondolom tudod rólam, hogy grafikus vagyok, de nem biztos, hogy ismered a diplomázásom pontos sztoriját, pedig vicces. Elmeséljem?"
  )
  time.sleep(1)
  print("1. Mesélj, Olivér")
  print("2. Tulajdonképpen már hallottam")

  valasz = input("Válasz: ")

  if valasz == '1':
    print(
        "\nSzerettem volna képregénnyel diplomázni, aztán mikor le kellett adni, hogy ugye akkor mivel diplomázunk, konkrétan mit vállalunk, stb., akkor így elbizonytalanodtam, hogy biztos, hogy így meg tudom-e csinálni, meg ilyenek. Igazából jogosan bizonytalanodtam el, merhogy' így a védés reggelén nyolc órakor lett kész a cucc, de úgy, hogy segítettek a színezéssel azok, akiknek mittomén' év közben nyomtattam, vagy csak simán jófejek voltak. A mai napig lassan dolgozom, úgyhogy ha tovább folytatom a sztorizást, gondolom megint nem fogok aludni."
    )
  elif valasz == '2':
    print("Viszlát, Olivér!")


def krubi():
  print(
      "\nÖsszefutottál Krúbival, aki éppen egy vödörrel a fején próbál beleolvadni a környezetébe"
  )
  time.sleep(1)
  print("Krúbi: Szia, figyelj, most annyira nem tudok beszélni")
  time.sleep(1)
  print("1. Miért bujkálsz, Krúbi?")
  print("2. Elbúcsúzás")

  valasz = input("Válasz: ")

  if valasz == '1':
    print(
        "Már megint egy Fonogramot akarnak rám sózni, nem értik, hogy nem kell. Légyszi, segíts elrejtőzni!"
    )
  elif valasz == '2':
    print("Viszlát, Krúbi, jó bujkálást!")


if __name__ == "__main__":
  main()
