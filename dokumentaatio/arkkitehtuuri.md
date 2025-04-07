# Rakenne

Applikaationi rakenne noudattelee kolmitasoista kerrosarkkitehtuuria.
Olen piirtänyt pakkausrakenteen seuravaanlaisesti:

(kuva)

Pakkaus ui sisältää käyttöliittymästä vastaavan koodin, services sovelluslogiikasta ja database tietokannasta ja tietojen tallennuksesta vastaavan koodin. Services ja database kansioiden sisältämät tiedostot sisältävät funktioita, eivät luokkia.

Ui kansiossa olevat Python-tiedostot sisältävät seuraavat luokat:

(kuva)
