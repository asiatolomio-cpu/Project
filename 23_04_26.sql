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
Nome completo dipendente
Stipendio
Media stipendio
Nome del reparto*/

select 
D.Nome + ' '+ D.Cognome as 'Nome Completo Dipendente',
D.Stipendio,
AVG (D.Stipendio) as 'Media Stipendio',
R.Nome as 'Nome Reparto',
R.Sede
from Dipendenti as D
inner join Reparti as R 
    on R.RepartoID=D.RepartoID
GROUP BY D.Nome, D.Cognome, AVG(D.Stipendio),D.Stipendio, R.Nome, R.Sede 
ORDER BY R.Nome DESC
---non funziona, da correggere



