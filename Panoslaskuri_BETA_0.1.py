import random

def proportionaalinen_panostus_yksikoilla():
    print("""
    Tervetuloa vedonlyönnin panoslaskuriin! (BETA 1.1)

    Tämä on ensimmäinen kokeiluversio ohjelmastani, ja se on käytettävissä rajatulle joukolle käyttäjiä.
    Arvostan palautettasi, sillä se auttaa parantamaan laskurin toimivuutta ja käyttökokemusta.

    Huom: Tämä versio saattaa sisältää puutteita tai kokeellisia toimintoja.
    """)

    # Riskitason nimet ja kuvaukset
    riskitasojen_nimet = {
        1: {
            "nimi": "Vähäriskinen (Konservatiivinen)",
            "kuvaus": "Panokset: Pienet (1–5 % pelikassasta). Vakaa ja hidas kasvu, mutta tappioriski on minimaalinen."
        },
        2: {
            "nimi": "Keskiriskinen (Tasapainoinen)",
            "kuvaus": "Panokset: Kohtuulliset (5–10 % pelikassasta). Tasapaino kasvun ja riskin välillä."
        },
        3: {
            "nimi": "Korkeariskinen (Aggressiivinen)",
            "kuvaus": "Panokset: Suuret (10–15 % pelikassasta). Nopea kasvu mahdollinen, mutta tappioriski on merkittävä."
        }
    }
    # Kysytään riskitaso vedonlyöntiin
    while True:
        try:
            
            print("""
            Valitse riskitaso, jolla haluat sijoittaa vedonlyöntiin:

            1 = Vähäriskinen (Konservatiivinen)
                - Panokset: Pienet panokset (1–5 % pelikassasta).
                - Vaikutus pelikassaan: Vakaa ja hidas kasvu, mutta tappioriski on minimaalinen.
                - Suositus: Sopii pitkäjänteiseen käyttöön, jossa pelikassan suojeleminen on ensisijaista.
                - Kenelle: Erinomainen valinta aloittelijoille ja niille, jotka arvostavat tasaista kehitystä.

            2 = Keskiriskinen (Tasapainoinen)
                - Panokset: Kohtuulliset panokset (5–10 % pelikassasta).
                - Vaikutus pelikassaan: Kasvupotentiaali ja riskit ovat tasapainossa. Pelikassa voi heilahdella, mutta hallitusti.
                - Suositus: Sopii niille, jotka haluavat yhdistää tuoton tavoittelun ja riskien hallinnan.
                - Kenelle: Suositellaan kokeneemmille vedonlyöjille tai niille, jotka haluavat ottaa hieman enemmän riskiä.
        
            3 = Korkeariskinen (Aggressiivinen)
                - Panokset: Suuret panokset (10–15 % pelikassasta).
                - Vaikutus pelikassaan: Nopea kasvu mahdollinen, mutta samalla tappioriski on merkittävä. 
                - Suositus: Käytä harkiten ja vain kohteisiin, joissa olet erityisen luottavainen.
                - Kenelle: Sopii vain kokeneille vedonlyöjille, jotka hyväksyvät suuren riskin ja pelikassan nopean heilahtelun.
            """)
            riskitaso = int(input("Valitse riskitaso (1-3): "))
            if riskitaso in [1, 2, 3]:
                print(f"\nValitsit riskitason: {riskitasojen_nimet[riskitaso]['nimi']}")
                print(f"{riskitasojen_nimet[riskitaso]['kuvaus']}\n")
                break
            else:
                print("Virheellinen valinta. Valitse riskitaso: 1, 2 tai 3.")
                
        except ValueError:
            print("Anna riskitaso numerona, esimerkiksi 1.")
                
    # Kysytään pelikassa
    while True:
        try:
            print("""
            Suositus pelikassan kooksi:
                - Vähimmäispelikassa: 100 €
                - Optimaalinen pelikassa: Esimerkiksi 500, 1000 € tai enemmän.
                - Huom! Pienellä pelikassalla:
                  * Korkean riskin panostus voi johtaa pelikassan nopeaan hupenemiseen.
            """)

            pelikassa = float(input("Syötä pelikassan koko: ").replace(",", "."))  # Pilkku -> Piste
            if pelikassa <= 0:
                print("Pelikassan tulee olla positiivinen luku.")
            else:
                if pelikassa < 100:
                    print("Huomio: Pienellä pelikassalla (alle 100 €) panokset voivat jäädä liian pieniksi tarkkaan riskienhallintaan ja vedonlyönnin mielekkyys voi kärsiä.")
                break
        except ValueError:
            print("Anna pelikassa numerona, esimerkiksi 1000 tai 1000,50.")

    # Kysytään todennäköisyysarvio yksikköinä
    while True:
        try:
            print("""
            Valitse todennäköisyysarviosi yksikköinä seuraavan ohjeen mukaan:

            1 = Rohkea kokeilu (veto, jossa uskot omaan intuitioosi – tilastot eivät tue valintaa, mutta pieni mahdollisuus on olemassa)
            2 = Potentiaalia näkyvissä (tilastot vihjaavat pelikohteen puolesta, mutta varmuus puuttuu - tämä voi osua)
            3 = Tilastollisesti järkevä (tutkit kohdetta ja tilastot tukevat valintaasi – turvallinen vaihtoehto)
            4 = Lähes varma nakki (ennakkoasetelmat, tilastot ja analyysit puhuvat vahvasti valinnan puolesta - vahva luotto kohteeseen)
            5 = Unelmaveto (kaikki tekijät ovat linjassa: tämä kohde on kuin painaisi "easy money" -nappia)
            """)
            yksikot = int(input("Anna todennäköisyysarviosi yksikköinä (1-5): "))
            if 1 <= yksikot <= 5:
                break
            else:
                print("Valitse luku 1 ja 5 välillä.")
        except ValueError:
            print("Anna luku 1 ja 5 välillä.")

    # Kysytään kohteen kerroin
    while True:
        try:
            kerroin = float(input("Syötä kohteen kerroin (esim. 2.5): ").replace(",", "."))  # Pilkku -> Piste
            if kerroin > 1:
                break
            else:
                print("Kertoimen tulee olla suurempi kuin 1.")
        except ValueError:
            print("Anna kerroin numerona, esimerkiksi 2.5.")

    # Lasketaan implied probability
    implied_probability = 1 / kerroin

    # Käyttäjän arvioitu todennäköisyys (lisätään ylimääräinen odotusarvo yksiköiden perusteella)
    todennakoisyys = implied_probability + (yksikot * 0.05)

    # Varmistetaan, että todennäköisyys ei ylitä 100 %
    #todennakoisyys = min(todennakoisyys, 1.0) // Alkuperäinen, kokeillaan hieman edistyneempää, joka informoi käyttäjää

    # Varmistetaan, ettei todennäköisyys ylitä 100 %
    if todennakoisyys > 1.0:
        print(f"Huomio: Yksikköarvioiden ja kertoimen perusteella laskettu todennäköisyys ylitti 100 % ({todennakoisyys * 100:.1f} %).")
        print("Todennäköisyys rajoitetaan 100 %:iin.")
        todennakoisyys = 1.0

    # Lisätään tarkistus käyttäjän näkökulmasta
    print(f"Laskettiin todennäköisyys (implied): {implied_probability * 100:.1f} %")
    print(f"Lopullinen todennäköisyys käyttäjän arvion perusteella: {todennakoisyys * 100:.1f} %")

    # Skaalauskertoimen laskenta yksikköjen ja riskitason perusteella
    def laske_skaalauskerroin(yksikot, riskitaso):
        if riskitaso == 1:  # Konservatiivinen
            skaalaus = {1: 0.03, 2: 0.05, 3: 0.07, 4: 0.08, 5: 0.09}
        elif riskitaso == 2:  # Tasapainoinen
            skaalaus = {1: 0.08, 2: 0.10, 3: 0.13, 4: 0.14, 5: 0.15}
        elif riskitaso == 3:  # Aggressiivinen
            skaalaus = {1: 0.12, 2: 0.15, 3: 0.18, 4: 0.20, 5: 0.25}
        return skaalaus[yksikot]
    
    # Lasketaan skaalauskerroin
    skaalauskerroin = laske_skaalauskerroin(yksikot, riskitaso)
    panos = skaalauskerroin * (todennakoisyys * pelikassa / kerroin)
    
    # Minimi- ja maksimipanos
    minimiprosentti = 0.01  # 1 % pelikassasta
    kiintea_minimipanos = max(1, pelikassa * minimiprosentti)
    panos = max(kiintea_minimipanos, panos)
    
    # Maksimiprosentti riskitason mukaan
    if riskitaso == 1:
        maksimi_prosentti = 0.05
    elif riskitaso == 2:
        maksimi_prosentti = 0.10
    elif riskitaso == 3:
        maksimi_prosentti = 0.15
    
    panos = min(pelikassa * maksimi_prosentti, panos)

    # Pyöristetään panos pelikassan koon mukaan
    if pelikassa <= 500:
        panos = round(panos / 0.05) * 0.05  # Lähimpään 5 senttiin
        panos = round(panos, 2)  # Varmistetaan, että panos on kahden desimaalin tarkkuudella
    elif pelikassa <= 1000:
        panos = round(panos / 5) * 5  # Lähimpään 5 euroon
    elif pelikassa <= 3000:
        panos = round(panos / 10) * 10  # Lähimpään 10 euroon
    elif pelikassa <= 5000:
        panos = round(panos / 20) * 20  # Lähimpään 20 euroon
    elif pelikassa <= 10000:
        panos = round(panos / 50) * 50  # Lähimpään 50 euroon
    else:
        panos = round(panos / 100) * 100  # Lähimpään 100 euroon
    
    # Tulostetaan tulokset
    print(f"\nPelikassa: {pelikassa:.2f} €")
    print(f"Riskitaso: {riskitasojen_nimet[riskitaso]['nimi']}")
    print(f"Kuvaus: {riskitasojen_nimet[riskitaso]['kuvaus']}")
    print(f"Todennäköisyysarvio pelikohteelle yksikköinä: {yksikot}/5 (käyttäjän laskettu todennäköisyys: {todennakoisyys * 100:.1f} %)")
    print(f"Kerroin: {kerroin}")
    print(f"Panos tähän kohteeseen: {panos} €")


# Kutsutaan funktiota
proportionaalinen_panostus_yksikoilla()

