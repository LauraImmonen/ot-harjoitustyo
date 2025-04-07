# Rakenne

Applikaationi rakenne noudattelee kolmitasoista kerrosarkkitehtuuria.
Olen piirtänyt pakkausrakenteen seuravaanlaisesti:

![pakkaus_rakenne](https://github.com/user-attachments/assets/9182d612-3dfb-4403-b825-805f39eede0b)


Pakkaus ui sisältää käyttöliittymästä vastaavan koodin, services sovelluslogiikasta ja database tietokannasta ja tietojen tallennuksesta vastaavan koodin. Services ja database kansioiden sisältämät tiedostot sisältävät funktioita, eivät luokkia.

Ui kansiossa olevat Python-tiedostot sisältävät seuraavat luokat:

![ui_luokat](https://github.com/user-attachments/assets/73ec31a1-c5e4-46b4-807b-e02f6b7e85ee)

