#!/bin/bash

# käynnistetään Flask-palvelin taustalle (huomaa & komennon lopussa)
cd src
poetry run flask run &

# odotetaan, että palvelin on valmiina ottamaan vastaan pyyntöjä,
# jolloin localhost:5000/ping antaa vastauksen statuskoodilla 200
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5000/ping)" != "200" ]];
  do sleep 1; 
done

# pysäytetään Flask-palvelin portissa 5000
function clean_up {
  kill $(jobs -p)
}

# suoritetaan clean_up-funktio, kun prosessi lopettaa suorituksen
trap clean_up EXIT

# suoritetaan testit
poetry run robot tests
