# Vaatimuusmärittely

---

**Sovelluksen tarkoitus**

- Sovellukseni on budjetointi-sovellus, jonne käyttäjä voi tehdä tilin ja kirjautua. (Tehty)
- Sovelluksessa käyttäjä voi asettaa kiinteän kuukausibudjetin ja lisätä menoja. (Tehty)
- Sovelluksessa näkee tämän kuun menot listana, missä näkyy menon kuvaus ja määrä euroina.
- Sovellus näyttää loppuraportin, jossa se ilmoittaa montako euroa käyttäjä on ylittänyt budjetin tai montako euroa käytäjä on säästänyt tässä kuussa. (Tehty)
- Sovellukseni kieli on englanti.

---

**Käyttöliittymäsuunnitelma sekä sovelluksen toiminnallisuus**

Sovellus koostuu viidestä eri näkymästä: Front page, login, create account, home page and create budget.
Eli etusivu, sisäänkirjautuminen, käyttäjätilin luominen, kotisivu ja budjetin luonti.

![budget_app_kayttoliittyma1](https://github.com/user-attachments/assets/e5faee6d-2d09-480a-9018-6a7f349578a4)

![home_page](https://github.com/user-attachments/assets/eb6f7144-ec95-48c9-8e54-eec41e2f240c)

![budget_app_kayttoliittyma3](https://github.com/user-attachments/assets/59314819-6b21-4cae-919a-0d59a69aee2c)

Sovellus aukeaa etusivulle jossa toivotetaan käyttäjä tervetulleeksi sovellukseen ja kysytään onko hänellä jo tiliä, jos on, hän voi kirjautua sisään, jos ei hän voi luoda tilin ja sen luotua hänet uudelleenohjataan sisäänkirjautumissivulle.

Sisäänkirjauduttuaan käyttäjälle avautuu kotisivu jossa voi kirjautua ulos, luoda kiinteän kuukausibudjetin tai nähdä jo olemassa olevan budjetin, sekä nykyisen kuukauden loppuraportin ja tarkastella ja lisätä tämän kuukauden menoja.
Tältä sivulta voi myös kirjautua ulos "logout" napin painalluksella, joka uudelleenhjaa käyttäjän takaisin etusivulle.

Jos käyttäjällä ei vielä ole budjettia, hän painaa make a budjet/create a budget näppäintä joka uudelleenohjaa hänet sivulle, jossa hän voi luoda kiinteän kuukausibudjetin itselleen. Kun se on luotu, hänet uudelleenohjataan takaisin kotisivulle.

---

**Jatkokehitysideoita**

- Sovellukseen voisi lisätä että voi luoda joka kuulle oman budjetin jos haluaa tai muokata vanhaa budjettia
- Tulot ja menot voisi laittaa kategorioihin
- Loppuraportissa voisi esim. näkyä piirakkamallina menot kategorioittain ja prosenteittain
- Voisi selata edeltävien kuukausien raportteja ja menoja. Nykyisessä versiossa näkyy vain sen kuukauden raportti jota eletään. Esim. Nyt on Maaliskuu joten käyttäjä näkee vain maaliskuun datan
