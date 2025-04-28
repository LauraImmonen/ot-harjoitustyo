# Käyttöohje

## **Asennus**

Repositorio asennusohjeet:

Avaa ensin terminaalissa tmp kansio komennolla: (muuten SQLite sanoo database locked)

```
cd /tmp
```

Kloonaa repositorio omalle koneellesi komennolla

```
git clone https://github.com/LauraImmonen/ot-harjoitustyo.git
```

siirry sitten vielä repon sisälle komennolla:

```
cd ot-harjoitustyo/
```

Jos tietokoneessasi ei ole Poetry:ä, tulee se asentaa ensin.

Sen jälkeen voit asentaa riippuvuudet komennolla:

```
poetry install
```

## **Ohjelman suorittaminen**

Ohjelman saa käyntiin komennolla:

```
poetry run invoke start
```

## **Tervetuloa sovellukseen**

Sovellus aukeaa tervetuliais-sivulle, jossa valitaan onko jo tili olemassa vai ei.

(kuva)

## **Tilin luonti**

Tili luodaan antamalla käyttäjänimi ja salasana ja painamalla "create user"-nappia. Jos kyseinen käyttäjänimi on jo käytössä, sovellus pyytää valitsemaan toisen nimen.

(kuva)

## **Kirjautuminen**

Lisää tilisi tiedot (käyttäjänimi ja salasana) ja paina "login"-nappia. Jos jompikumpi on kirjoitettu väärin, sovellus ilmoittaa siitä käyttäjälle.

(kuva)

## **Budjetin luominen**

Kotinäkymässä ylhäällä näkyy "create budget"-nappi, paina sitä niin pääset sivulle, jossa voit luoda kiinteän kuukausibudjetin itsellesi.

(kuva)

Kun pääset budjetin luonti sivulle, kirjoita numeraalinen määrä, eli esim 1000 ja paina "Create budget"-nappia. Jolloin kuukausibudjettisi on 1000 euroa.

(kuva)

Nyt näet kotisivulla budjettisi.

(kuva)

## **Kulujen lisääminen**

Voit lisätä kuluja lisäämällä numeerisen euromäärän ja kirjoittaa kuvauksen ostetusta tuotteesta tai palvelusta. Esim. 100 euroa ja kuvaus: groceries

Tämän jälkeen näet kotisivun ala-osassa kuukauden kulut listana, ja näet paljonko rahaa olet säästänyt, tai paljonko yli budjetin olet mennyt tässä kuussa.

(kuva)
