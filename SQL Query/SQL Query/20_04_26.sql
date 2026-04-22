/*vado a controllare le informazioni sulla colonna Email nella tabella Clienti */
SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Clienti'
AND COLUMN_NAME = 'Email';

/*per modificare un campo della tabella, dal contenuto, all'intestazione delle colonne
devo inserire il nome della tabella (ex MyTable), poi il nome della colonna e il nuovo tipo per la colonna,
o la modifica richiesta */
--ex. ALTER TABLE MyTable
--   ALTER COLUMN NullCOl NVARCHAR (20) NOT NULL;

/*Devo aumentare la dimensione della colonna Nome nella tabella Progetti,
inoltre passo dal null a not null*/
ALTER TABLE Progetti
ALTER COLUMN Nome NVARCHAR(150) NULL;
/*cerco di fare la stessa cosa con altre colonne, in altre tabelle */

ALTER TABLE Dipendenti
ALTER COLUMN Email NVARCHAR(150) NOT NULL;--non funziona

ALTER TABLE Clienti
ALTER COLUMN Email NVARCHAR(150) NOT NULL;--non funziona

ALTER TABLE Dipendenti
ADD Telefono NVARCHAR (50);

INSERT INTO Dipendenti (Nome, Cognome, Email, Stipendio, DataAssunzione, RepartoId, Telefono)
VALUES ('Asia', 'Tolomio', 'asia.tolomio@example.com', 100000, '2023-01-01', 1, '1234567890');

/*Unique non funziona con alter column*/
--ALTER TABLE Clienti
--ALTER COLUMN Email NVARCHAR(150) UNIQUE;-- non funziona

--ESERCIZIO DA FARE DAL PDF

select *
from Dipendenti;

select *
from Clienti;

ALTER TABLE NomeTabella 
ADD NomeColonna TipoDato;