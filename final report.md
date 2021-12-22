# Final report

Sami Dinh, Jan Rundt, Pentti Lähdeaho, Iida Vilkkinen

## Sprinttien aikana kohdatut ongelmat

Sprint 1:  
- Ensimmäisen sprintin aikana kului yllättävänkin suuri aika jo pelkkään konfigurointiin ja oppien mieleen palauttamiseen web-sovelluksiin liittyen. Myöskin uuden tehtävän ja ryhmän kanssa työnjaon tekeminen tapahtui muihin sprintteihin verrattuna hieman verkkaisemmin, vaikka onnistuikin kuitenkin lopulta ihan hyvin. Vaikeutta lisäsi kuitenkin se, että jotkin toiminnallisuudet oli helpompi luoda vasta kun oli saatu jokun aikaisempi userstory toteutettua, mikä vaati hyvää organisointia ryhmän työajan ja tehtävien jaon suhteen.
- Herokun käyttöönotto tuotti hieman ongelmia, joita monella tapaa yritettiin ratkaista (esim. Herokussa Docker kontin ajaminen). Heroku ei suoraan tue Poetrya, joten piti kikkailla. 

Sprint 2:  
- Tässä sprintissä piti saada pysyvä tallennus toimimaan, ja yksi haaste oli saada github-actioneihin tietokanta. Github-actioneissä on se hankala puoli, että niitä pystyy vain testaamaan "tuotannossa", eli tekemällä suuren määrän committejä kunnes löytyy toimiva ratkaisu. Tämä jättää ikään kuin ruman jäljen repositoryn historiaan. Ratkaisu tälle oli tehdä testit toista repositorya vastaan, taisi mennä jotain 25 committia ennen kuin toimi kuten pitäisi.

Sprint 3:
- Kahdet sprintin aikana mukana olleet user storyt menivät vähän ristiin, ja kaksi eri ryhmän jäsenet näitä toteuttivat. Huomattiin vasta ihan sprintin loppumetreillä, että toisen storyn toteutus oli mennyt vähän rikki siitä, kun toinen story oli toteutettu sen jälkeen. Tuli kiire korjata sen ennen loppudemoa. 

## Mikä sujui projektissa hyvin, mitä pitäisi parantaa seuraavaa kertaa varten

Sujui hyvin:  
- Yhteistyö  
- "Daily" scrumien pitäminen, tiimi pysyi paremmin kartalla missä mennään ja toisen koodia oli helpompi ymmärtää kun itse koodaaja oli tavoitettavissa
- Työn jakaminen sopivankokoisiin osiin  
- Hyvien ideoiden ja neuvojen jakaminen

Parantamisen varaa:
- Branchien ja/tai pullareiden käyttöönotto, ettei pushata suoraan main-branchiin ja mahdollisesti hajoteta asioita

## Mitä asioita opittiin, mitä asioita olisimme halunneet oppia, mikä tuntui turhalta

- Oppi aina jotain uutta kun katsoo miten muut ratkaisevat jonkun ongelman, tai käyttävät jonkun itselle vieraan teknologian
- Huomasi, että on ihan hauskaa kehittää sovelluksen yhteistyössä, ettei joudu itse ratkaisemaan ihan kaikkia pulmia
