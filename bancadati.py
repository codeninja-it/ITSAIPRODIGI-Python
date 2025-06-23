import sqlite3
from tkinter import simpledialog

testo = simpledialog.askstring("nome del db", "dove vuoi salvare il db?")

# mi connetto alla banca dati
dbcon = sqlite3.connect("miodb.sqlite")

# ottengo un telefono
dbexe = dbcon.cursor()

dbexe.execute(
    "CREATE TABLE IF NOT EXISTS letture("+ 
        "idLettura INTEGER PRIMARY KEY AUTOINCREMENT," +
        "vento NUMBER," + 
        "temperatura NUMBER," +
        "umidita NUMBER,"  +
        "quando DATETIME" +
    ")"
)

# per dieci volte
for n in range(10):
    # eseguo una richiesta di inserimento
    dbexe.execute("INSERT INTO letture (vento, temperatura, umidita) VALUES (0, 0, 0)")

# chiudo la transazione rendendo le mi richieste
# accessibili anche ad altri
dbcon.commit()

# chiudo la connessione
# per risparmiare risorse
dbcon.close()