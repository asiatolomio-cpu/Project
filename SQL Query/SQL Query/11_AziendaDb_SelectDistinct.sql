--argomenti da trattare:
--1.SUBQUERY

/*consegna: calcolo gli ordini sopra alla media
prima vado a vedere quale sia la media di tutti gli ordini
poi la inserisco come subquery fra parentesi tonda
lascio i select e introduco il tutto con WHERE
il ";" va alla fine della query totale*/
SELECT 
    AVG(Totale) as Media
FROM Ordini; --925

SELECT *
FROM Ordini
WHERE Totale > (
    SELECT 
    AVG(Totale) as Media
FROM Ordini
);

--ex. Clienti senza ordini

SELECT ClientiID
FROM Ordini;

SELECT ClientiID
FROM Ordini
WHERE ClientiID NOT IN(
    SELECT ClientiID
    FROM Ordini
);--non ho clienti senza ordini

/*ho inserito NOT IN per vedere se ho clienti senza ordini,
quindi se ho ordini senza clienti*/

--Consegna: Ordini sopra la media del cliente
--vedo la media degli ordini
SELECT
    AVG(Totale) as Media
FROM Ordini; --926

--calcolo la media e seleziono solo le righe che hanno una media ordini maggiore della media
SELECT *
FROM Ordini
WHERE Totale >(
    SELECT
    AVG(Totale) as Media
FROM Ordini
);

--faccio combaciare l'id clienti in entrambe le tabelle (anche se sono la stessa)
--siccome Ordini compare 2 volte devo creare 2 alias diversi
--con il WHERE devo farli combaciare mettendo il segno di uguaglianza 
--è come se facessi l'inner join sulla stessa tabella (in questo caso Ordini) 
SELECT *
FROM Ordini as o
WHERE Totale > (
    SELECT 
    AVG(Totale) as Sopra_Media
    FROM Ordini as oo
    WHERE o.ClientiID = oo.ClientiID
);

--la query sopra è uguale alla seguente, ma in sintassi più semplice:
SELECT 
    AVG(o.Totale) AS 'Sopra media'
FROM Ordini as o
INNER JOIN Ordini oo
	ON o.ClienteID = oo.ClienteID;

--consegna: media superiore per cliente
--per visualizzare solo determinati dati devo inserire tutta la lista di ciò che voglio vedere
--inserisco anche la colonna che andrò a creare dopo la join con pertinenza all'alias corretto: quindi tabella.colonna
--la subquery si trasforma in una tabella
--la tabella Ordini ha fatto inner join con se stessa, 
SELECT DISTINCT
    o.OrdineID,
    o.ClientiID,
    o.Totale,
    M.MediaCliente
FROM Ordini as o
INNER JOIN ( 
    SELECT DISTINCT
    AVG(Totale) as MediaCliente
    FROM Ordini
    GROUP BY ClientiID
) AS M on Totale NOT IN (
    SELECT 
    AVG(Totale) AS Media
    FROM Ordini
    WHERE Totale>1500
);

--oppure:
SELECT DISTINCT
    o.OrdineID,
    o.ClientiID,
    o.Totale,
    M.MediaCliente
FROM Ordini as o
INNER JOIN ( 
    SELECT DISTINCT
    AVG(Totale) as MediaCliente
    FROM Ordini
    GROUP BY ClientiID
) AS M on o.Totale > M.MediaCliente
WHERE O.Totale > M.MediaCliente;

--oppure:
SELECT
    ClientiID,
    AVG(Totale) AS Media
FROM Ordini
GROUP BY ClientiID;

SELECT DISTINCT
    o.OrdineID,
    o.ClientiID,
    o.Totale,
    M.MediaCliente
FROM Ordini as o
INNER JOIN ( 
    SELECT DISTINCT
    ClientiID,
    AVG(Totale) as MediaCliente
    FROM Ordini
    GROUP BY ClientiID
) AS M on o.Totale > M.MediaCliente
WHERE O.Totale > M.MediaCliente;
--da modificare


/*modello SINTATTICO:
SELECT
* oppure le colonne selezionate
FROM Tabella
WHERE + condizione con (
    SELECT 
    * oppure colonne selezionate
    FROM Tabella
    );
*/

--2.WHERE e HAVING
--Modello Sintattico
/*SELECT
* oppure le colonne selezionate
FROM Tabella
GROUP BY Colonna
HAVING +condizione
;
*/

SELECT 
    Prodotto,
    SUM (Quantita) as Quantita
FROM DettagliOrdine
GROUP BY Prodotto
HAVING SUM(Quantita) >= 5;

--inseriamo GROUP BY perchè nella SELECT abbiamo una funzione di Aggregazione (SUM)
--nell'HAVING dobbiamo per forza enunciare la funzione di Aggregazione se vogliamo raggruppare per quella colonna
--infatti HAVING tiene conto solo delle colonne esistenti nella tabella prima dell'esecuzione della query

--3.DATA in SQL Server
GET DATE
DATE
DAY
MONTH
YEAR
TIME

--seleziono gli ordini dopo il 2024
SELECT *
FROM Ordini
WHERE DataOrdine>= '2024';

--modifichiamo la tabella Ordini, sottraendo 30gg ad ogni DataOrdine
SELECT *
FROM Ordini
WHERE DataOrdine>= DATEADD (DAY,-30,GETDATE());

--ordini per mese, anno, mese, giorno
--uso CONVERT per estrapolare i vari componenti della data
SELECT 
    CONVERT(NVARCHAR,YEAR(DataOrdine)) AS Anno,
    CONVERT(NVARCHAR,MONTH(DataOrdine)) AS Mese,
    CONVERT(NVARCHAR,DAY(DataOrdine)) AS Giorno
FROM Ordini;

--continua sul file 28_04_26 Create DB

