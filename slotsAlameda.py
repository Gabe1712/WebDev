import requests
import json

r=requests.get("https://fenix.tecnico.ulisboa.pt/api/fenix/v1/parking")

if(r.ok):
    x=(json.loads(r.content)).get("Alameda").get("total")
    y=(json.loads(r.content)).get("Alameda").get("freeSlots")
    z=x-y
    print("O nº de lugares ocupados é :", z)