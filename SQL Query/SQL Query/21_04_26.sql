ALTER TABLE Dipendenti
ADD Telefono NVARCHAR (50);

Alter table Clienti
Add Indirizzo NVARCHAR(100);

--cambio nome alla colonna
/*exec, per trovare le store procedure corretta, sp_rename, poi nome della tabella 
a cui la colonna fa riferimento, poi punto e il nome attuale della colonna, (questi 2 nomi 
fra singola virgola), successivamente virgola e fra virgole singole il nuovo nome*/
exec sp_rename 'Dipendenti.RepartoId', 'RepartoID';
--provo con un altra colonna
exec sp_rename 'Dipendenti.Stipendio', 'Salario';
/*faccio tornare come prima, uso la specifica 'COLUMN' alla fine, 
per specificare che si tratta di una colonna;
non è obbligatorio, ma è buona pratica inserirlo, per evitare errori*/
exec sp_rename 'Dipendenti.Salario', 'Stipendio', 'COLUMN';

--vado a modificare la riga
/*con UPDATE posso sostituire tutti i valori nulli in una determinata colonna
'SET' è il nuovo dato da inserire, nome colonna seguito da uguale e il nuovo dato 
poi vado a definire dove questo nuovo dato andrà inserito usando WHERE*/

UPDATE Clienti 
SET Indirizzo ='via Torino 654'
WHERE ClientiID=5;

UPDATE Dipendenti
SET DataAssunzione = '2023-01-01'
WHERE DataAssunzione is null;

UPDATE Dipendenti
SET Telefono = '1234567890'
WHERE Telefono is null;

/*posso anche aggiungere/togliere e non solo sostituire i dati
usando gli operatori aritmetici*/
UPDATE Dipendenti
SET Stipendio = Stipendio+1000
WHERE Stipendio <= 2000;

/*voglio cancellare una colonna*/
ALter Table Dipendenti
DROP COLUMN Telefono;

UPDATE Dipendenti
SET Stipendio = Stipendio +200
Where DipendenteID=12;

UPDATE Dipendenti
SET Stipendio = Stipendio*1.10;

UPDATE Dipendenti
SET RepartoID= 2
WHERE DIpendenteID=1002;

/*voglio unire 2 o più tabelle, (tramite una query, usando tutti gli strumenti già imparati)
le tabelle devono avere colonne in comune per unirle*/
/*ex
SELECT Colonne da visualizzare
FROM Tabella1 
INNER JOIN Tabella2
ON + condizione */ 

--introduciamo AS per rinominare le colonne, per semplificare la query (come ALIAS)
SELECT 
    D.Nome AS 'Nome Dipendente',
    D.Cognome AS 'Cognome Dipendente'
FROM Dipendenti as D;

--Consegna: voglio visualizzare solo i dipendenti con reparto valido
--Voglio che ritornino solo nome completo del dipendente, email, nome e sede del reparto a cui appartiene
--Se l'alias contiene spazi bisogna mettere il nome fra virgolette singole, altrimenti non è necessario
/*uso gli alias per accorciare le query della seconda parte, in modo da essere veloce ed evitare ripetizioni 
ed errori
inserisco nel select tutte colonne che voglio visualizzare anche se non fanno parte della tabella principale*/
SELECT 
    D.Nome AS 'Nome Dipendente',
    D.Cognome AS 'Cognome Dipendente',
    D.Email,
    R.NomeReparto AS 'Nome Reparto',
    R.SedeReparto

FROM Dipendenti as D
INNER JOIN Reparti as R
ON D.RepartoID = R.RepartoID;

--Consegna: voglio Clienti, Ordini e Dettaglio dell'ordine con 
--Cliente (Nome e telefono), 
--Ordini (Data ordine e totale ordine)
--Dettaglio ordine (prodotto,quantità e prezzo unitario) 

SELECT 
    cl.Nome AS 'Nome del cliente',
    cl.Telefono AS Contatto,
    o.DataOrdine AS 'Data dell''ordine',
    d.Prodotto AS 'Nome del prodotto',
    d.Quantita AS 'Quantità del prodotto',
    d.PrezzoUnitario AS 'Prezzo Unitario',
    o.Totale AS 'Totale ordine'
FROM Clienti AS cl 
JOIN Ordini AS o ON o.ClienteID=cl.ClientiID --non ho lo stesso nome in entrambe le tabelle, però posso farle combaciare. 
JOIN DettagliOrdine AS d ON d.OrdineID=o.OrdineID;

exec sp_rename 'Ordini.ClienteID', 'ClientiID', 'COLUMN';
--ora ho cambiato il nome della colonna ClienteID in ClientiID, 
--quindi devo modificare anche la query precedente, altrimenti non funziona più 
/*per la compilazione conviene fare in sequenza
1. select (senza quanto scritto in indentazione)
2. From + alias
3. Join+ alias
4. la condizione con ON (con le colonne che combaciano)
   (in questo caso, a condizione che il ClienteID della tabella Ordini è uguale al ClienteID della tabella Clienti, 
   e che l'OrdineID della tabella DettagliOrdine è uguale all'OrdineID della tabella Ordini)
5. ripetiamo i punti 3 e 4 se abbiamo più tabelle a cui unirsi
6. tutti gli alias dell'indentazione di select*/
SELECT 
    cl.Nome AS 'Nome del cliente',
    cl.Telefono AS Contatto,
    o.DataOrdine AS 'Data dell''ordine',
    d.Prodotto AS 'Nome del prodotto',
    d.Quantita AS 'Quantità del prodotto',
    d.PrezzoUnitario AS 'Prezzo Unitario',
    o.Totale AS 'Totale ordine'
FROM Clienti AS cl 
JOIN Ordini AS o ON o.ClientiID=cl.ClientiID 
JOIN DettagliOrdine AS d ON d.OrdineID=o.OrdineID;

--CONCATENAZIONE usiamo il + per unire più stringhe in una sola, (non è uguale all'addizione) 
SELECT 
    D.Nome +' '+ D.Cognome 'Nome Completo del Dipendente',
    D.Email,
    R.NomeReparto AS 'Nome Reparto',
    R.SedeReparto

FROM Dipendenti as D
INNER JOIN Reparti as R
ON D.RepartoID = R.RepartoID;

SELECT 
    D.Nome +' '+ D.Cognome 'Nome Completo del Dipendente',
    D.Email,
    R.NomeReparto+','+' '+R.SedeReparto AS 'Reparto'
    
FROM Dipendenti as D
INNER JOIN Reparti as R
ON D.RepartoID = R.RepartoID;


SELECT *FROM Assegnazioni;
SELECT *FROM Clienti;
SELECT *FROM DettagliOrdine;
SELECT *FROM Dipendenti;
SELECT *FROM Ordini;
SELECT *FROM Progetti;
SELECT *FROM Reparti;
