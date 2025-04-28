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

![welcome_page](https://github.com/user-attachments/assets/b4358fdb-0e35-42ed-af26-c649995339ab)


## **Tilin luonti**

Tili luodaan antamalla käyttäjänimi ja salasana ja painamalla "create user"-nappia. Jos kyseinen käyttäjänimi on jo käytössä, sovellus pyytää valitsemaan toisen nimen.

![create_account](https://github.com/user-attachments/assets/6ab38138-1403-4ac5-b636-21a60b26207c)


## **Kirjautuminen**

Lisää tilisi tiedot (käyttäjänimi ja salasana) ja paina "login"-nappia. Jos jompikumpi on kirjoitettu väärin, sovellus ilmoittaa siitä käyttäjälle.

![login_page](https://github.com/user-attachments/assets/d1b4a4fd-5396-49cc-bfa3-a08017ca4266)


## **Budjetin luominen**

Kotinäkymässä ylhäällä näkyy "create monthly budget"-nappi, paina sitä niin pääset sivulle, jossa voit luoda kiinteän kuukausibudjetin itsellesi.

![home_page_before](https://github.com/user-attachments/assets/5d3ef69a-4f82-4f2d-96cf-99fbeb025b99)


Kun pääset budjetin luonti sivulle, kirjoita numeraalinen määrä, eli esim 1000 ja paina "Create budget"-nappia. Jolloin kuukausibudjettisi on 1000 euroa.

![create_budget_page](https://github.com/user-attachments/assets/866c9889-4aaf-44ba-9fc6-ce5207274995)


Nyt näet kotisivulla budjettisi.

![home_page_after](https://github.com/user-attachments/assets/8d908292-4e20-46f1-81a7-2f4b81001939)


## **Kulujen lisääminen**

Voit lisätä kuluja lisäämällä numeerisen euromäärän ja kirjoittaa kuvauksen ostetusta tuotteesta tai palvelusta. Esim. 100 euroa ja kuvaus: groceries

![home_page_add_expense](https://github.com/user-attachments/assets/dd1828a1-710a-4036-8045-b0a9bd2d8eb7)


## **Kulujen tarkastelu ja loppuraportti**
Tämän jälkeen näet kotisivun ala-osassa kuukauden kulut listana, ja näet paljonko rahaa olet säästänyt, tai paljonko yli budjetin olet mennyt tässä kuussa "Final report"-osiosta joka löytyy sivun yläosasta.

![home_page_past_expenses](https://github.com/user-attachments/assets/e51e269d-bb95-425a-a4ad-62a03b268ce0)
