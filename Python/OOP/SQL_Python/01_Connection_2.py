# =========================================
# IMPORT LIBRERIA
# =========================================

# pymssql serve per collegarsi a SQL Server
import pymssql


# =========================================
# VARIABILE CONNESSIONE
# =========================================

# Inizialmente la connessione è vuota
conn = None


# =========================================
# BLOCCO TRY
# =========================================

try:

    print("⏳ Connessione al server...\n")

    # =========================================
    # CONNESSIONE DATABASE
    # =========================================

    conn = pymssql.connect(

        # nome server SQL
        server='localhost',

        # utente SQL Server
        user='sa',

        # password SQL Server
        password='DataAnalyst14$',

        # database da usare
        database='ScuolaDb'
    )

    print("✅ Connessione riuscita\n")

    # =========================================
    # CREAZIONE CURSORE
    # =========================================

    # Il cursore serve per eseguire query SQL
    cursor = conn.cursor()

    # =========================================
    # RECUPERO NOME SERVER
    # =========================================

    cursor.execute("SELECT @@SERVERNAME")

    # Legge la prima riga del risultato
    values = cursor.fetchone()[0]

    print(f"✅ Connesso al server: {values}\n")

    # =========================================
    # RECUPERO TABELLE DATABASE
    # =========================================

    print("📌 Recupero automatico tabelle...\n")

    cursor.execute("""

        SELECT TABLE_NAME

        FROM INFORMATION_SCHEMA.TABLES

        WHERE TABLE_TYPE='BASE TABLE'

        ORDER BY TABLE_NAME ASC

    """)

    # =========================================
    # LETTURA RISULTATI
    # =========================================

    tables = cursor.fetchall()

    print("📋 Tabelle trovate:\n")

    for row in tables:

        print(f" -> {row[0]}")


# =========================================
# GESTIONE ERRORI
# =========================================

except Exception as e:

    print("❌ Errore di connessione:\n")

    print(e)


# =========================================
# FINALLY
# =========================================

finally:

    # Controlla che la connessione esista
    if conn:

        print("\n⏳ Chiusura connessione...")

        conn.close()

        print("🔐 Connessione chiusa")