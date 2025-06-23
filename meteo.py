import requests
import os
import matplotlib.pyplot as grafico
import sqlite3 as db

# lancio il pulisci schermo
os.system("cls")

def SalvaDB(voci):
    dbcon = db.connect("meteo.sqlite")
    dbexe = dbcon.cursor()
    dbexe.execute("CREATE TABLE IF NOT EXISTS previsioni(" +
                  "idPrevisioni INTEGER PRIMARy KEY AUTOINCREMENT," +
                  "giorno DATETIME," +
                  "vento DOUBLE," +
                  "umido DOUBLE," +
                  "temperatura DOUBLE"
                  ")")
    record = len(voci["time"])
    for i in range(record):
        quando = voci["time"][i]
        vento = voci["wind_speed_10m"][i]
        umido = voci["relative_humidity_2m"][i]
        temperatura = voci["temperature_2m"][i]
        sql = f"INSERT INTO previsioni (giorno, vento, umido, temperatura) VALUES ('{quando}', {vento}, {umido}, {temperatura})"
        dbexe.execute(sql)
    dbcon.commit()
    dbcon.close()

# recupera le coordinate da nominatim di un luogo
def DammiLocalizzazione(luogo):
    risposta = requests.get("https://nominatim.openstreetmap.org/search",
                            params= {
                                "q"      : luogo,
                                "format" : "json",
                                "limit"  : 1
                            },
                            headers= {
                                "User-Agent": "mio meteo"
                            }
    )
    if risposta.status_code == 200:
        print("luogo recuperato...")
        return risposta.json()[0]
    else:
        print("errore sul luogo...")
        return None

# recuperare il forecast direttamente da open-meteo
def DammiMeteo(lat, lon):
    risposta = requests.get("https://api.open-meteo.com/v1/forecast", params={
                    "latitude"  : lat,
                    "longitude" : lon,
                    "current"   : ["temperature_2m", "wind_speed_10m", "relative_humidity_2m"],
                    "hourly"    : ["temperature_2m", "wind_speed_10m", "relative_humidity_2m"]
                })
    if risposta.status_code == 200:
        print("dati ricevuti...")
        return risposta.json()
    else:
        print("internet is gone away...")
        return None
    

# recupero dove
print("-" * 10)
print("MIO METEO!!!")
print("-" * 10)
print("mi dici dove?\t", end="")
nome = input()
luogo = DammiLocalizzazione(nome)
if luogo is not None:
    # recupero le previsioni
    previsioni = DammiMeteo(luogo["lat"], luogo["lon"])
    if previsioni is not None:
        # stampo il meteo
        print( previsioni["current"]["temperature_2m"] )
        print( previsioni["current"]["relative_humidity_2m"] )
        futuro = previsioni["hourly"]
        SalvaDB(futuro)
        grafico.scatter(futuro["time"], futuro["temperature_2m"])
        grafico.show()