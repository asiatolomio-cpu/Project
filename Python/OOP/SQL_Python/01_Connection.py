# chiedere nome del server, nome del database, username e password per ciascuno

# Obiettivo, recuperare automaticamente tutte le tabelle da SQL Server con Pyhton
# come collegarsi a un database SQL Server
       # eseguire query di sistema
       # recuperare automaticamente tutte le tabelle
       # gestire errori e connessioni in modo professionale
       # capire come un Data Analyst esplora un database sconosciuto

        

import pymssql 


try:
    # collegamento al database
    conn = pymssql.connect(
        server='localhost',
        user='sa',
        password='DataAnalyst14$',
        database='ScuolaDb'
    )
    print("✅ Connesso al server")
    conn.close()
except Exception as e:
    print("❌ Errore di connessione:")
    print(e)


try:
    print("⏳ Connessione al server...")
    
    conn = pymssql.connect(
        server='localhost',
        user='sa',
        password='DataAnalyst14$',
        database='ScuolaDb'
    )

    # creo un cursore
    # ossia una mano che esegue query SQL
    cursor = conn.cursor()
    
    # esegue la query fra parentesi 
    # introduco una variabile in modo da verificare la connessione
    # in questo caso 'values'
    values = cursor.execute('SELECT @@SERVERNAME').fetchone()[0]
    # la dicitura 'fetchone/fetchall()? legge i risultati
    # con 'fetchall()' ho bisogno di inserire un'altra variabile 

    print(f"✅ Connesso al server {values}\n")
    
    print("\n Recupera automaticamente tutte le tabelle ")
    
    # VERSIONE 1 -- QUERY STANDARD (da compilare a mano)
    # va inserito tutto fra triple virgolette
    cursor.execute("""
        SELECT TABLE_NAME 
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_TYPE='BASE TABLE'
        ORDER BY TABLE_NAME ASC
        """
    )
    # VERSIONE 2 -- QUERY di SISTEMA (Stored Procedure)
    cursor.execute("EXEC sp_ListaTabelle")

    # VERSIONE 3 -- QUERY con PANDAS 
    df = pd.read_sql("EXEC sp_ListaTabelle", conn)
    print(df) 

    # VERSIONE 4 --QUERY con PANDAS e PARAMETRI
    
    print("📌 Tabella Trovate\n")
    
    for row in cursor.fetchall():
        print(f" -> {row[0]}")
        
except Exception as e:
    # gestisce gli errori
    # segnala che ci sono 
    # mi riporta quali sono
    print("❌ Errore di connessione:")
    print(e)

finally:
    try:
        print("Chiusura connessione...\n")
        conn.close()
        print("\n🔐 Connessione Chiusa")
    except:
        print("Riprova")
        pass
        