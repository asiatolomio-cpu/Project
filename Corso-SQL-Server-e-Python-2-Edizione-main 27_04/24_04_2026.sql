USE AziendaDb;

select * from Ordini
-- Aggiunta della colonna 
/*
	ALTER TABLE NOME DELLA TABELLA 
	ADD NOME DELLA COLONNA CON IL TIPO
*/

ALTER TABLE Ordini
ADD DetaglioId INT;


-- Modifica del nome della colonna
EXEC sp_rename 'Ordini.DetaglioId', 'DettaglioId';

-- Modifica del nome della tabella 
EXEC sp_rename 'Ordine', 'Ordini';

-- Update per la modifica
/*
	UPDATE nome della tabella
	SET nome della colonna = il nuovo valole
	WHERE condizione (es. OrdineId = 1)
*/

UPDATE Ordini
SET DettaglioId = 36
WHERE OrdineId = 36


/*
	DELETE FROM Nome della tabella
      WHERE colonna = valore 
*/

-- Esempio: 

INSERT INTO Ordini (ClienteID, DataOrdine, Totale, DettaglioId) VALUES
(30,'2026-01-01',100, 22);


DELETE FROM Ordini
      WHERE Totale = 100

/*
	ALTER TABLE NOME DELLA TABELLA 
	ADD CONSTRAINT NOME DELLA CHIAVE ESTERNA
	FOREIGN KEY NOME DELLA COLONNA (DetaglioId)
	REFERENCES RIFERIMENTO ALLA TABELLA ESTERNA CON IL NOME DELLA COLONNA (DetaglioId)
*/
ALTER TABLE Ordini
ADD CONSTRAINT FK_Ordini_Dettagli
FOREIGN KEY (DettaglioId) REFERENCES DettagliOrdine(DettaglioId)


-- count
SELECT 
	COUNT(*) AS 'TOTALE RIGHE'
FROM Clienti;


-- SUM ()
SELECT
	SUM(Totale) AS 'Somma totale degli ordini'
FROM Ordini

-- COUNT il numero totale degli ordini
SELECT 
	COUNT(*) AS 'Totale degli ordini'
FROM Ordini

-- Ordine media AVG
SELECT 
	AVG(Totale) AS 'La media degli ordini'
FROM Ordini

-- ANALISI DEI DATI 
SELECT
	COUNT(*) AS 'Totale degli ordini',
	AVG(Totale) AS 'La media degli ordini',
	MIN(Totale) AS 'Ordine minimo',
	MAX(Totale) AS 'Ordine massimo',
	SUM(Totale) AS 'Somma totale degli ordini'
FROM Ordini

select * from Ordini