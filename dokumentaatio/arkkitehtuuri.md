# Rakenne

Applikaatiossani on rakenteena kolmitasoinen kerrosarkkitehtuuri.
Olen piirtänyt pakkausrakenteen seuravaanlaisesti:

![pakkaus_rakenne](https://github.com/user-attachments/assets/9182d612-3dfb-4403-b825-805f39eede0b)

Pakkaus ui sisältää käyttöliittymästä vastaavan koodin, services sovelluslogiikasta ja database tietokannasta ja tietojen tallennuksesta vastaavan koodin. Services ja database kansioiden sisältämät tiedostot sisältävät funktioita, eivät luokkia.

Ui kansiossa olevat Python-tiedostot sisältävät seuraavat luokat:

![ui_luokat](https://github.com/user-attachments/assets/73ec31a1-c5e4-46b4-807b-e02f6b7e85ee)

# Käyttöliittymä

Käyttöliittymäni sisältää 5 eri näkymää

- Etusivu
- Käyttäjätilin luonti
- Kirjautuminen
- Kotisivu
- Budjetin luonti

Jokainen näkymä on erillinen luokka. Käyttöliittymä eristetty sovelluslogiikasta ja on UI-kandion sisällä. Käyttöliittymän luokat kutsuvat erilaisia services-funktioita, esim. käyttäjää luodessa kutsutaan from services.account_service import create_user joka tarkastaa onko kyseinen käyttäjänimi jo olemassa.

# Tietojen pysyväistallennus

Sovellukseni käyttää SQLite tietokantaa jossa on 2 taulua users ja expenses. Kaikki tietokantojani koskeva koodi löytyy kansioista "database". "create_database.py"-tiedostosta. Tiedosto sisältää koodin, joka luo tietokannan ja yhteyden tietokantaan sekä luo taulut. "queries.py" -tiedosto sisältää kaikki SQLite kyselyt, joilla muokataan tietokannan tauluja tai haetaan dataa niistä.

# Sovelluksen päätoiminallisuudet

## **Tilin luominen:**

![create account](https://github.com/user-attachments/assets/c70577f0-704a-4c53-8ad9-2c0b9d1a50e6)

Käyttäjä painaa "Create Account"-nappia käyttäjätilin luonti sivulla ja syöttää kenttiin käyttäjänimen ja salasanan. Jos käyttäjänimi on jo käytössä, nousee esille virheviesti: "username already exists! Please choose another username." Jos nimeä ei ole vielä käytössä, tulee esiin viesti: "Account created successfully", ja näkymä vaihtuu sisäänkirjautumisnäkymäksi.

## **Sisäänkirjautuminen:**

![Login](https://github.com/user-attachments/assets/3611e9e9-7389-4d21-8f54-fc23ff16b239)

Sisäänkirjautumissivulla käyttäjä syöttää käyttäjänimensä ja salasanansa ja painaa lopusi "Login"-nappia. Sovellus tarkastaa ovatko salasana ja käyttäjänimi oikein. Jos eivät, tulee esiin niille suunnatut virheviestit. Jos kaikki on syötetty kenttiin oikein, tulee esiin viesti: "Logged in sucessfully! ja näkymä vaihtuu kotisivun näkymäksi.

## **Budjetin luominen:**

![create budget](https://github.com/user-attachments/assets/65bb06b0-3b5f-41aa-92b9-9210e9cdcf94)

Kotisivulla käyttäjä painaa nappia "Create your monthly budget", joka ohjaa näkymän create account sivulle. Sitten käyttäjä täyttää kuukausibudjetin määrän numerona kenttään. Jos input ei ole numero, tulee virheviesti joka ilmoittaa asiasta. Muuten ohjelma avaa näkymän takasin kotisivulle ja antaa viestin "Budget created successfully!".

## **Menojen lisääminen:**

![add expense](https://github.com/user-attachments/assets/22eaa88a-66f7-4e7f-ad50-8d1c4405c7e4)

Kotisivun alalaidassa voi lisätä kuluja syöttämällä kulun hinnan numerona ja halutessaan voi lisätä myös kuvauksen ja painaa "Add expense"-nappia. Sovellus tarkastaa nykyisen käyttäjän id:n, jotta se voi lisätä kulut oikealle henkilölle. Jos kulun hinta ei ole numero, syntyy virheilmoitus joka ilmoittaa asiasta. Jos kaikki on ok, ilmoittaa sovellus "Expense added successfully!" Sitten sovellus tyhjentää kentät, jotta käyttäjä voi lisätä uuden kulun.
