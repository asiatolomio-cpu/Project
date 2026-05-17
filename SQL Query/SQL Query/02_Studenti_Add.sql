use ScuolaDb;

select *
from Studenti;

select Nome,
    Cognome,
    Genere 
from Studenti;

/*per evitare di vedere i valori doppi uso SELECT DISTINCT
--devo specificare le colonne di cui non voglio visualizzare i duplicati
--l'ordine in cui li scrivo sarà quello in cui compaiono i risultati*/

select distinct Nome,
    Cognome 
from Studenti;

select distinct StudenteId,
    Nome, 
    Cognome,
    Genere
from Studenti;

/* con WHERE (definisce una condizione) quindi vado a a prendere solo i dati per un singolo criterio
sto cercando lo studente con ID 3, quindi specifico la colonna e il valore che mi interessa*/ 

select * from Studenti
where StudenteId=3;

select Nome,
    Cognome
    from Studenti
    where StudenteId=3;

/*posso anche rinominare le colonne, usando AS seguito dal nuovo nome che voglio dare alla colonna
la vedo solo io, non va a modificare la struttura della tabella*/
select Nome as 'Nome Studente',
    Cognome as 'Cognome Studente',
    Genere as 'Genere Studente',
    Email as 'Email Studente'
    from Studenti
where StudenteId=3;

--ritorna solo i nomi e i cognomi degli studenti di genere maschile, senza visualizzare i duplicati 
SELECT Distinct Nome,
Cognome
from Studenti
Where Genere='M';

/*ritorna tutti gli studenti che hanno il nome che inizia con la lettera indicata 
il simbolo % è un carattere jolly che indica che dopo la L può esserci qualsiasi cosa*/
--il significato di LIKE in soldoni è "ci sta" ossia quello che specifico è contenuto all'interno dei dati apparteneneti alla colonna
/*ammette solo stringhe di testo, quindi non posso usarlo per i numeri*/

select distinct Nome,
    Cognome,
    genere 
    from Studenti
where Nome like 'L%';  

/*operatori aritmetici sono simboli/parole che permettono di 
.confrontare valori
.fare calcoli
.filtrare risultati*/

/* operatori di confronto
usati con WHERE:
.operatore                         | significato       |
__________________________________________________________
=                                  | uguale            |
>                                  | maggiore          |
<                                  | minore            |
>=                                 | maggiore o uguale |
<=                                 | minore o uguale   |
<>  /  !=                          | diverso           |

a sx dell'operatore andrà il nome della colonna di cui voglio confrontare il valore
a dx dell'operatore andrà il valore con cui voglio confrontarlo
*/
select * from Studenti
where StudenteId=3;

/*operatori logici sono simboli/parole che permettono di
.combinare più condizioni
.operatore                          | significato                                         |
___________________________________________________________________________________________
AND                                 | e  ossia tutte le condizioni sono VERE              |
OR                                  | o  ossia almeno una condizione è VERA               |
NOT                                 | non  ossia nessuna condizione è VERA, nega          |   
*/
--inserisco più voci all'interno della tabella, in modo da lavorare su più dati

INSERT INTO Studenti (Nome, Cognome, Email, Genere)
VALUES
('Mario','Rossi','mario1@email.com','M'),
('Luca','Bianchi','luca2@email.com','M'),
('Giulia','Verdi','giulia3@email.com','F'),
('Anna','Ferrari','anna4@email.com','F'),
('Marco','Romano','marco5@email.com','M'),
('Paolo','Ricci','paolo6@email.com','M'),
('Sara','Gallo','sara7@email.com','F'),
('Davide','Costa','davide8@email.com','M'),
('Elena','Fontana','elena9@email.com','F'),
('Simone','Greco','simone10@email.com','M'),
('Francesca','Conti','francesca11@email.com','F'),
('Andrea','DeLuca','andrea12@email.com','M'),
('Chiara','Marino','chiara13@email.com','F'),
('Alessio','Riva','alessio14@email.com','M'),
('Valentina','Lombardi','valentina15@email.com','F'),
('Giorgio','Barbieri','giorgio16@email.com','M'),
('Martina','Moretti','martina17@email.com','F'),
('Stefano','Ferraro','stefano18@email.com','M'),
('Roberta','Caruso','roberta19@email.com','F'),
('Alberto','Giordano','alberto20@email.com','M'),
('Federica','Colombo','federica21@email.com','F'),
('Claudio','Silvestri','claudio22@email.com','M'),
('Marta','Testa','marta23@email.com','M'),
('Daniele','Villa','daniele24@email.com','M'),
('Silvia','Serra','silvia25@email.com','F'),
('Emanuele','Leone','emanuele26@email.com','M'),
('Ilaria','Santoro','ilaria27@email.com','F'),
('Matteo','Fiore','matteo28@email.com','M'),
('Noemi','Ruggiero','noemi29@email.com','F'),
('Fabio','Pellegrini','fabio30@email.com','M');

--se inserisco il % dopo le lettere vuol dire che le lettere indicate sono le iniziali (non c'è differenza tra maiuscole e minuscole)
-- S% o s% significa S.... o s...., quindi qualsiasi nome che inizia con S o s
select *
from Studenti
where Nome like 'S%' and Genere='F';

-- se inserisco il % prima delle lettere vuol dire che le lettere indicate sono le finali (non c'è differenza tra maiuscole e minuscole)
-- %o o %O significa ....o o ....O, quindi qualsiasi nome che finisce con o o O
select *
from Studenti 
where Nome like '%o' and Genere='M';

select *
from Studenti
where Nome='Mario' or Nome='Paolo';

select *
from Studenti
where Nome='Alice' or Nome='Mario';

/*si può decidere l'ordine di apparizione dei risultati, usando ORDER BY seguito dal nome della colonna e dalla direzione 
ASC per crescente, 
DESC per decrescente*/

select *
from Studenti
order by Nome Desc;

select *
from Studenti
order by Cognome ASC;

/*usiamo TOP per limitare il numero di risultati restituiti, 
seguito da un numero che indica quanti risultati vogliamo vedere*/
select top 5 *
from Studenti;

/*is not null si usa per escludere tutti i valori nulli in una determinata colonna
NON esistendo la funzione LAST, dobbiamo usare ORDER BY e TOP*/
select top 15 *
from Studenti 
where Email is not null and Genere='F'
order by Nome Desc;

--posso anche combinare più condizioni usando gli operatori logici
select top 5*
from Studenti where Email is not null and Genere='F' or Nome like 'S%';

/*se uso le parentesi, do la precedenza a quelle condizioni, 
quindi prima valuto se il nome inizia con S e il cognome finisce con o, e poi valuto se l'email è null e il genere è F*/
select top 5*
from Studenti where Email is not null and Genere='F' or (Nome like 'S%' and Cognome like '%o');

/*possiamo usare IN come sostituzione di AND/OR nei casi in cui io abbia più valori da confrontare
con questa sintassi indico una lista di valori che mi devono essere restituiti (se all'interno della tabella)*/
select*
from Studenti
where Nome in ('Mario', 'Alice', 'Simone');
--infatti è uguale a scrivere:
select *
from Studenti
where Nome='Mario' or Nome='Alice' or Nome='Simone';


--esercitazioni
select *
from Studenti
where Nome in ('Mario','Alice','Simone','Giulia') 
and Email is not null;

select *
from Studenti
where Nome in ('Mario','Alice','Simone','Giulia') 
and Email is not null;

select *
from Studenti
where Email is null;
