import random

#definisco il mio record
class meteo:
    # equivalente di costrunct, init, constructor, etc...
    def __init__(self, temp, vento, umidita):
        self.temp = temp
        self.vento = vento
        self.umidita = umidita

    # esempio di funzioni per generare valori derivati
    def Celsius(self):
        return self.temp
    
    def Farenheit(self):
        return ((self.temp * 9) / 5) + 32
    
    def Kelvin(self):
        return self.temp + 273.15
    
    # equivalente di ToString()
    def __str__(self):
        return f"{self.temp}°\t{self.vento}kmh\t{self.umidita}%"

# definisco il "recordset"
letture = []

numeroRecord = 100

#inizializzo il seme randomico
random.seed(1.1)

#carico 10 record in array
for i in range(numeroRecord):
    numero = 10 + (random.random() * 30)
    letture.append( meteo(numero, 12, 25) )

#rivedo quanto caricato
for i in range(numeroRecord):
    print(letture[i])