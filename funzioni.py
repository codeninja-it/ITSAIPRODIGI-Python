import sqlite3 as db

def CreaTabella(nome, campi):
    buffer = []
    for nomec, tipo in campi.items():
        match(tipo):
            case "key":
                buffer.append(f"{nomec} INTEGER PRIMARY KEY AUTOINCREMENT")
            case "int":
                buffer.append(f"{nomec} INTEGER")
            case "dbl":
                buffer.append(f"{nomec} DOUBLE")
            case "txt":
                buffer.append(f"{nomec} TEXT")
            case "date":
                buffer.append(f"{nomec} DATETIME")
            case _:
                buffer.append(f"{nomec} {tipo}")
    sql = f"CREATE TABLE IF NOT EXISTS {nome}(\n"
    sql += f",\n".join(buffer)
    sql += ")"
    return sql

if(__name__ == "__main__"):
    letture = {
        "idLettura" : "key",
        "idLuogo" : "int",
        "temp" : "dbl",
        "vento" : "dbl",
        "umido" : "dbl",
        "quando" : "date"    
    }

    luoghi = {
        "nome" : "text",
        "idLuogo" : "key"
    }

    dbcon = db.connect("esperimento.sqlite")
    dbexe = dbcon.cursor()
    dbexe.execute( CreaTabella("letture", letture) )
    dbexe.execute( CreaTabella("luoghi", luoghi) )
    dbcon.close()
