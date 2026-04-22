-- Creazione del Database
CREATE DATABASE ScuolaDb1;

-- Elimina il Database esistente
-- DROP DATABASE Demo;


-- Uso del Database
use ScuolaDb;



/*
| Tipo             | Quando usarlo                    |
| ---------------- | -------------------------------- |
| INT  = INTERGER  | numeri interi (ID, età) = 100 000 000          |
| DECIMAL(10,2)    | soldi (precisione!)              |
| NVARCHAR, VARCHAR| testo (sempre meglio di VARCHAR) |
| DATE             | solo data                        |
| DATETIME         | data + ora                       |
| BIT              | booleano (0/1)   Vero o Falso    |
*/

-- Creazione della tabella Studenti
CREATE TABLE Studenti(
	-- Nome della colonna di tipo Intero Chiave primaria Identifica univocamente  una riga che si incrementa automaticamente da 1 a 1 
	StudenteId INT NOT NULL PRIMARY KEY IDENTITY(1,1), 
	Nome NVARCHAR(150) NOT NULL,
	Cognome NVARCHAR(150) NOT NULL,
	Email NVARCHAR(150) NULL,
	Genere CHAR(1) NOT NULL
);

-- VISUALIZZA LA LISTA DEGLI STUDENTI
SELECT Nome, Cognome, Email, Genere FROM Studenti;

-- inserimento dei dati nella tabella studenti
SELECT * FROM Studenti


INSERT INTO Studenti
	(Nome, Cognome, Genere)
Values
	('Melania', 'Todaro', 'F'),
	('', '', ''),
	('', '', ''),
	('', '', ''),
	('', '', ''),
	('', '', '');