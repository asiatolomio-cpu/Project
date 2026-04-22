-- esercizio 
/* commento 
a righe
molteplici
*/
--DROP DATABASE nomedatabase; elimina il database se esistente

--CREATE DATABASE nomedatabase; crea un database con il nome specificato

--USE DATABASE nomedatabase; lo metto in uso

USE ScuolaDb;
/*| Tipo             | Quando usarlo                    |
| ---------------- | -------------------------------- |
| INT (integer)    | numeri interi (ID, età)          |
| DECIMAL(10,2)    | soldi (precisione!)              |
| NVARCHAR, VARCHAR| testo (sempre meglio di VARCHAR, poichè il suo massimo è 16) |
| CHAR             | testo di lunghezza fissa (solitamente una sola parola/lettera)    |
 DATE             | solo data                        |
| DATETIME         | data + ora                       |
| BIT              | booleano (0/1)     V/F              |
| UNIQUEIDENTIFIER | GUID ex Codice Fiscale, numero 
                     identificativo in generazione                        |
*/
/*creazione tabella*/
/*per il StudentID devo identificare la chiave primaria,
quale tipo di dati ammetterà,
che non può essere nulla,
e soprattutto che sarà il nostro identificatore,
un nuovo studente corrisponde a un nuovo record nella tabella, incrementando di 1 l'ultimo numero identificativo usato*/ 
/*inserisco NOT NULL ogni volta in cui il dato è indispensabile*/
/*inserisco dopo il tipo di dati, la lunghezza massima consentita per il numero di caratteri*/

CREATE TABLE Studenti(
    StudenteId INT NOT NULL PRIMARY KEY IDENTITY (1,1),
    Nome NVARCHAR(150) NOT NULL,
    Cognome NVARCHAR(150) NOT NULL,
    Email NVARCHAR(150) NULL,
    Genere CHAR(1) NOT NULL,
    );

--visualizza la lista degli studenti
--from invece identifica da quale tabella dobbiamo prendere i dati

--Select, seguito da * per visualizzare tutte le colonne
select *
from Studenti;

--select, seguito da i nomi delle colonne fra parentesi, fa vedere solo quelle specificate (non necessitano di parentesi ma di virgole e a capo)
select Nome,
    Cognome,
    Genere
    
from Studenti;

--Inserisco i dati all'interno delle righe, in una tabella
--Seleziona ed esegui la query, pur non avendo subito risultato è stato inserito correttamente un nuovo record nella tabella, con un nuovo ID
--per vedere il risultato dovrò eseguire il select all(*) from Studenti
INSERT INTO Studenti
    (Nome, Cognome, Genere)
VALUES
    ('Daisy', 'Duck', 'F'),
    ('Minnie', 'Mouse', 'F'),
    ('Mickey', 'Mouse', 'M');
