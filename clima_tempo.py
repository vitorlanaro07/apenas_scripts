
from unittest import result
import requests
import json

#token: 5d9f6f9e
#https://api.hgbrasil.com/weather?key=5d9f6f9e&city_name=Japurá,PR (Cidade e Estado)
#

def get_cidade(city_name, state_abbr):
    url = f"https://api.hgbrasil.com/weather?key=5d9f6f9e&city_name={city_name},{state_abbr}"
    var_request = requests.get(url).text
    var_request = json.loads(var_request)
    #print(var_request)

    result = var_request['results']
    temp = result['temp']
    time_now = result['time']
    description = result['description']
    city_na = result['city_name']
    currently = result['currently']
    #print(temp)
    print("###################################################")
    print(f"Cidade: {city_na}\nHorário da consulta: {time_now} da {currently} \n{description}. {temp}°C")
    print("###################################################")
    


get_cidade(str(input("Que cidade deseja saber o tempo: ")),str(input("De qual estado: ")))


