# Ohjelmistotekniikka harjoitustyö

Tämä on harjoitustyöni Helsingin yliopiston kurssille **Aineopintojen harjoitustyö: _Ohjelmistotuotanto_**.
Aikeenani on tehdä desktop-sovellus joka toimii budjetointi-sovelluksena.

Tällä hetkellä sovelluksessa on welcome page jolla käyttäjä voi valita onko hänellä jo tili vai ei.
Hän voi tällä hetkellä myös luoda käyttäjätunnuksen ja sieltä hänet uudelleenohjataan kirjautumissivulle.
Kirjautumissivulla käyttäjä kirjautuu sisään sovellukseen ja hänet uudelleenohjataan kotisivulle, 
jossa hän voi asettaa kuukausibudjetin jos sitä vielä ei ole, ja jos se on jo asetettu, näkyy se sivulla. 
Budjetti asetetaan erillisellä sivulla jonne käyttäjä uudelleenohjataan napin painalluksella.
Käyttäjä pystyy myös kirjautumaan ulos kotisivulta.

Olisi hyvä saada palautetta siitä, tulisiko minun testata vain services kansiossa olevia funktioita, jotka sisältävät sovelluslogiikan.

Linkki vaatimusmäärittelyyn: [vaatimusmäärittely](https://github.com/LauraImmonen/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
Linkki arkkitehtuuri tiedostoon: [arkkitehtuuri.md](https://github.com/LauraImmonen/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
Linkki tuntikirjanpitoon: [tuntikirjanpito](https://github.com/LauraImmonen/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

# Asennus

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
