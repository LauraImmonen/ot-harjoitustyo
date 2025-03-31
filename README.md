# Ohjelmistotekniikka harjoitustyö

Tämä on harjoitustyöni Helsingin yliopiston kurssille **Aineopintojen harjoitustyö: _Ohjelmistotuotanto_**.
Aikeenani on tehdä desktop-sovellus joka toimii budjetointi-sovelluksena.

Tällä hetkellä sovelluksessa on welcome page jolla käyttäjä voi valita onko hänellä jo tili vai ei.
Hän voi tällä hetkellä myös luoda käyttäjätunnuksen ja sieltä hänet uudelleenohjataan kirjautumissivulle.
Kirjautumissivulta ei toistaiseksi pääse pidemmälle.

Olisi hyvä saada palautetta siitä mitä kaikkea tulisi testata, esim tuleeko ui kansiossa olevia tiedostoja testata myös vai pelkästään sovelluslogiikkaa joka on kansiossa services, jota ui-tiedostot käyttävät. En ole ennen tehnyt sovellukseen testejä joten tämä on kaikki minulle aivan uutta.

# Asennus

Repositorio asennusohjeet:

Luo hakemisto tälle repolle esim:

```
mkdir testi
```

ja luo reitti sille:

```
cd testi
```

Kloonaa repositorio omalle koneellesi komennolla

```
git clone https://github.com/LauraImmonen/ot-harjoitustyo.git

```

Tämän jälkeen avaa reitti hakemistoon:

```
cd testi/

```

(näet komennolla ls, oletko repositiossa, pitäisi näkyä kaikki sovelluksen osat esim READ.ME, tasks.py, src. Jos ei näy, niin sinun pitää mennä ns syvemmälle, avaa siis tiedosto koneella ja katso reitti, se voi olla esim. Documents/testi/repon_nimi/ ja yritä sitten: cd Documents/testi/repon_nimi/)

Jos tietokoneessasi ei ole Poetry:ä, tulee se asentaa ensin.

Asenna riippuvuudet komennolla:

```
poetry install
```

# Ohjelman suorittaminen

Ohjelman saa käyntiin komennolla:

```
poetry run invoke start
```

# Testaus

Testit suoritetaan komennolla:

```
poetry run invoke test
```

# Testit

Testikattavuusraportin saa tehtyä komennolla:

```
poetry run invoke coverage-report
```

Raportti generoituu htmlcov-hakemistoon
