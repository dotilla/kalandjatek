import time

def main():
    print("Üdvözöllek a Magyar Alternatív Rockzenekarok Kalandjátékban!\n")
    time.sleep(1)
    print("Találkozz a legnagyobb frontemberekkel és hozz döntéseket velük való interakciók során!\n")
    time.sleep(1)
    print("Induljunk el!\n")
    time.sleep(1)
    
    while True:
        print("\nVálassz egy frontembert, akivel találkozni szeretnél:")
        print("1. Beck Zoli (30y)")
        print("2. Szendrői Csaba (Elefánt)")
        print("3. Bérczesi Robi (hiperkarma)")
        print("4. Lovasi András (Kispál és a Borz, Kiscsillag)")
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
            lovasi_andras()
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
    print("Beck Zoli: Szia! Mit szeretnél tőlem kérdezni?")
    time.sleep(1)
    print("1. Beszélgetés")
    print("2. Elbúcsúzás")

    valasz = input("Válasz: ")

    if valasz == '1':
        print("Beszélgetés Beck Zolival...")
    elif valasz == '2':
        print("Viszlát, Beck Zoli!")

def szendroi_csaba():
    print("\nSzendrői Csabával, az Elefánt énekesével találkoztál!")
    time.sleep(1)
    print("Szendrői Csaba: Helló! Mit szeretnél tőlem kérdezni?")
    time.sleep(1)
    print("1. Beszélgetés")
    print("2. Elbúcsúzás")

    valasz = input("Válasz: ")

    if valasz == '1':
        print("Beszélgetés Szendrői Csabával...")
    elif valasz == '2':
        print("Viszlát, Szendrői Csaba!")

def berczesi_robi():
    print("\nBérczesi Robival, a hiperkarma énekesével találkoztál!")
    time.sleep(1)
    print("Bérczesi Robi: Szervusz! Mit szeretnél tőlem kérdezni?")
    time.sleep(1)
    print("1. Beszélgetés")
    print("2. Elbúcsúzás")

    valasz = input("Válasz: ")

    if valasz == '1':
        print("Beszélgetés Bérczesi Robival...")
    elif valasz == '2':
        print("Viszlát, Bérczesi Robi!")

def lovasi_andras():
    print("\nLovasi Andrással, a Kispál és a Borz/Kiscsillag énekessel találkoztál!")
    time.sleep(1)
    print("Lovasi András: Helló! Mit szeretnél tőlem kérdezni?")
    time.sleep(1)
    print("1. Beszélgetés")
    print("2. Elbúcsúzás")

    valasz = input("Válasz: ")

    if valasz == '1':
        print("Beszélgetés Lovasi Andrással...")
    elif valasz == '2':
        print("Viszlát, Lovasi András!")

def krubi():
    print("\nKrúbi!")
    time.sleep(1)
    print("Krúbi: Hello! Mi a helyzet?")
    time.sleep(1)
    print("1. Beszélgetés")
    print("2. Elbúcsúzás")

    valasz = input("Válasz: ")

    if valasz == '1':
        print("Beszélgetés Krúbival...")
    elif valasz == '2':
        print("Viszlát, Krúbi!")

if __name__ == "__main__":
    main()
