# Testausdokumentti

Olen testannut sovellustani automatisoiduilla yksikkö- ja integraatiotesteillä unittestilla. Olen myös testannut sovellukseni toimivuutta manuaalisesti eri käyttäjillä.

# Yksikkö- ja integraatiotestaus

Olen testannut sovelluslogiikkaa tekemällä testit account_service.py ja budget_service.py sisältäville funktioille. En käyttänyt valetietokantaa, vaan käytin oikeaa, mutta poistin kaikki testattavat asiat aina ennen seuraavaa testiä.

SetUp metodini sisältää kaikki testeissä käytettävät inputit esim. käyttäjänimen ja salasanan, sekä luo yhteyden tietokantaan.

# Testikattavuus

Testikattavuus on 78%.

![coverage_report_78_procent](https://github.com/user-attachments/assets/e7a35520-bc9b-4a92-909b-0d1dfb7e0b70)


Testaamatta jäi virheilmoitukset, joita tulee kun käyttäjä lisää vääränlaisen tai tyhjän inputin.

# Jäjestelmätestaus

Tehty manuaalisesti.

# Asennus ja konfigurointi

Olen asentanut sovelluksen käyttöohjeideni mukaan ja testannut sitä eri käyttäjillä ja inputeilla. Olen käyttänyt testeissäni Linux-ympäristöä (omalla Linux tietokoneellani sekä virtuaaliympäristössä).

# Toiminnallisuudet

Olen testannut kaikki määrittelydokumenttini ja käyttöohjeissa olevat toiminnallisuudet läpi. Olen kokeillut täyttää myös virheellisiä ja tyhjiä arvoja kaikkiin syötekenttiin nähdäkseni, ettei sovellus kaadu ja että virheviestit näkyvät oikein.
