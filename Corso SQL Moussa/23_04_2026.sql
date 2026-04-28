Use AziendaDb;

/*
	SUM, AVG, COUNT, MIN e MAX 
	permettono calcoli su gruppi di dati in SQL Server.
*/

-- Contare le righe della tabella (Count)
SELECT
	COUNT(*) AS 'Totale righe'
FROM Assegnazioni;


SELECT 
	COUNT(a.Ruolo) as 'Tot righe'
FROM Assegnazioni a;

SELECT COUNT(Email) 
FROM Clienti;

-- AVG = Per la media
SELECT 
	AVG(Salario) AS 'Stipendio media'
FROM Dipendenti;

-- Sum => SOMMA
SELECT 
	SUM(Salario) AS 'Totale stipendio'
FROM Dipendenti;


-- MIN => Minimo
SELECT 
	MIN(Salario) AS 'Stipendio minimo'
FROM Dipendenti;

-- MAX => Valore più grande
SELECT 
	MAX(Salario) AS 'Stipendio massimo'
FROM Dipendenti;

-- Analisi dei Dati
SELECT 
	COUNT(*) AS NumRighe,
	MIN(Salario) AS 'Stipendio minimo',
	AVG(Salario) AS 'Stipendio media',
	MAX(Salario) AS 'Stipendio massimo',
	SUM(Salario) AS 'Totale stipendio'
FROM Dipendenti;

-- Esempio: stipendio per reparto
/*
	Nome completo del dipendente
	Salario
	Stipendio media
	Nome del reparto
	Sede
*/
SELECT 
	d.Nome + ' - ' + d.Cognome AS 'Nome completo del dipendente',
	d.Salario,
	AVG(d.Salario) AS 'Stipendio media', 
	r.Nome AS 'Nome del reparto',
	r.Sede
FROM Dipendenti As d
INNER JOIN Reparti AS r ON r.RepartoID = d.RepartoID 
GROUP BY  d.Nome, d.Cognome, d.Salario, r.Nome, r.Sede
ORDER BY r.Nome Desc

--Sto modificando da vs code

SELECT 
	d.Nome + ' - ' + d.Cognome AS 'Nome completo del dipendente',
	d.Salario,
	AVG(d.Salario) AS 'Stipendio media', 
	r.Nome AS 'Nome del reparto',
	r.Sede
FROM Dipendenti As d
INNER JOIN Reparti AS r ON r.RepartoID = d.RepartoID 
GROUP BY  d.Nome, d.Cognome, d.Salario, r.Nome, r.Sede
ORDER BY r.Nome Desc