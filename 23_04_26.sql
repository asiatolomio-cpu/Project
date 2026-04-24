--SUM, MAX,MIN, AVG, COUNT permettono calcoli su gruppi di dati
USE AziendaDB;

--consegna: contare quante righe esistono nella tabella Assegnazioni
/*ho inserito l'asterisco nel COUNT e non nel SELECT
non mi permette di visualizzare prima tutte le colonne (SELECT *), 
perchè andiamo a contare le righe prima dobbiamo concentrarci sulla funzione e poi sulle colonne, 
restituisce una sola riga con scritto il numero di righe della tabella*/
Select 
     COUNT(*) as NumeroAssegnazioni
FROM Assegnazioni;

--consegna: contare quante righe di ruoli abbiamo nella tabella Assegnazioni
/*per selezionare la colonna che vogliamo visualizzare andiamo a 
specificarla subito dopo il COUNT posto fra le parentesi*/
Select 
Count (Ruolo) as NumeroRuoli
FROM Assegnazioni;
--oppure
SELECT
count (a.Ruolo) as 'Tot Ruoli'
FROM Assegnazioni a;

--consegna: contare quante email dei clienti sono presenti nella tabella Clienti
Select 
count (Cl.Email) as NumeroEmailClienti
From Clienti Cl;

--consegna: calcolare la media dei salari dei dipendenti e contare quanti dipendenti abbiamo
/*stessa logica del COUNT, sempre specificando la colonna 
fra parentesi dopo AVG*/
select 
count(*) as NumeroDipendenti,
avg (Stipendio) as MediaStipendiDipendenti
From Dipendenti;

--consegna: somma  di tutti i salari dei dipendenti
/*stessa logica del COUNT, sempre specificando la colonna 
fra parentesi dopo SUM*/
SELECT
SUM(Stipendio) as BudgetDipendenti
from Dipendenti;

--consegna: calcolare somma, media, massimo, minimo e numero dipendenti
/*queste funzioni hanno tutti la stessa logica di sintassi*/
select 
count(*) as NumeroDipendenti,
SUM (Stipendio) as BudgetDipendenti,
avg (Stipendio) as MediaStipendiDipendenti,
min (Stipendio) as StipendioMinimo,
max (stipendio) as StipendioMassimo
from Dipendenti;

--GROUP BY: raggruppare colonne, righe secondo un criterio, va inserito come ultima riga di query
--consegna: stipendio per reparto
/* Deve restituirci:
Nome completo dipendente (unendo nome e cognome del dipendente)
Stipendio
Media stipendio
Nome del reparto
Sede del reparto*/
/*se non specifico nel GROUP BY gli elementi specificati nel SELECT, la query non funziona*/
SELECT
	d.Nome + ' ' + d.Cognome AS 'Nome completo del dipendente',
	d.Stipendio,
	AVG(d.Stipendio) AS 'Stipendio medio',
	r.NomeReparto AS 'Nome del Reparto',
	r.SedeReparto
	FROM Dipendenti AS d
	INNER JOIN Reparti AS r ON d.RepartoID = r.RepartoID
	GROUP BY d.Nome, d.Cognome, d.Stipendio, r.NomeReparto, r.SedeReparto
	ORDER BY r.NomeReparto DESC

