0. Uso ScuolaDb per capire il funzionamento tra tabelle 

SELECT * FROM Aule;--30 Lezioni
SELECT * FROM Corsi;--30
SELECT * FROM Docenti;--30 DocentiCorsi
SELECT * FROM DocentiCorso;--30 Corsi
SELECT * FROM Iscrizioni;--28 Corsi e Studenti
SELECT * FROM Lezioni;--26 Corsi
SELECT * FROM Studenti;--37 Studenti e Corsi

SELECT *
FROM Aule 
WHERE AulaId = 10;

SELECT NomeAula
FROM Aule 
WHERE Capacita > 30;

SELECT TOP 10 *
FROM Studenti;

SELECT *
FROM Corsi
WHERE Crediti < 7 and Durata >=30;

SELECT DISTINCT *
FROM Studenti
WHERE DataNascita IS NULL;

/*abbiamo convertito i records NULL della colonna DataNascita, in 'Data Nascita Non Trovata (o n/d),
usando il CONVERT dobbiamo specificare Tipo di carattere, Colonna, Formato quando si tratta della data
abbiamo poi delle date che non sono nulle quindi possiamo usare le funzioni MONTH, YEAR sulla colonna
e poi specificare cosa scrivere nel caso NULL e infine definire l'alias */
--105,103,107 sono i formati della Data di Nascita, non sono indispensabili perchè c'è un impostazione di default
SELECT 
    Nome +' '+ Cognome as 'Nome Completo',
   ISNULL(CONVERT(NVARCHAR,DataNascita, 105), 'n/d') as DataNascita,
   ISNULL(CONVERT(NVARCHAR,MONTH(DataNascita),107), 'n/d') AS MeseNascita,
    ISNULL(CONVERT(NVARCHAR,YEAR(DataNascita)), 'n/d') AS AnnoNascita
FROM Studenti;

--1.TUTTI LE JOIN (Left,Right,Inner,Simple)
--Studenti iscritti ad un corso
SELECT 
    s.StudenteId,
    s.Nome +' '+ s.Cognome as 'Nome Completo',
    c.NomeCorso,
    c.Durata
FROM Studenti AS s
LEFT JOIN Iscrizioni AS i
    ON i.StudenteId = s.StudenteId
LEFT JOIN Corsi AS C
    ON c.CorsoId = i.CorsoId;

--se ci fossero Corsi il cui nome fosse NULL allora:
SELECT 
    s.StudenteId,
    s.Nome +' '+ s.Cognome as 'Nome Completo',
    ISNULL(c.NomeCorso, 'n/d') as 'Nome Corso',
    c.Durata
FROM Studenti AS s
LEFT JOIN Iscrizioni AS i
    ON i.StudenteId = s.StudenteId
LEFT JOIN Corsi AS C
    ON c.CorsoId = i.CorsoId;

/*se ci fossero Corsi la cui durata fosse NULL allora:
inserisco ISNULL, fra parentesi inserisco la colonna esistente per restituirmela così com'è
poi la virgola e subito dopo il valore che vogliamo al posto di NULL (se stringa è fra '')
chiudo la parentesi e poi l'alias*/
SELECT 
    s.StudenteId,
    s.Nome +' '+ s.Cognome as 'Nome Completo',
    ISNULL(c.NomeCorso, 'n/d') as 'Nome Corso',
    ISNULL(c.Durata, 0) as 'Durata Corso'
FROM Studenti AS s
LEFT JOIN Iscrizioni AS i
    ON i.StudenteId = s.StudenteId
LEFT JOIN Corsi AS C
    ON c.CorsoId = i.CorsoId;

/*se inseriamo COUNT poi dovremmo inserire per ultimo GROUP BY
inserisco tutti le specifiche che ho inserito sotto SELECT
ricordandoci di specificare la colonna originale (non gli alias)
con la pertinenza della tabella (s.,c.,i. in questo caso)*/ 
SELECT 
    s.StudenteId,
    s.Nome +' '+ s.Cognome as 'Nome Completo',
    ISNULL(c.NomeCorso, 'n/d') as 'Nome Corso',
    ISNULL(c.Durata, 0) as 'Durata Corso',
    COUNT(s.StudenteId) as 'Totale Studenti'
FROM Studenti AS s
LEFT JOIN Iscrizioni AS i
    ON i.StudenteId = s.StudenteId
LEFT JOIN Corsi AS C
    ON c.CorsoId = i.CorsoId
GROUP BY s.StudenteId, s.Nome, s.Cognome, c.NomeCorso, c.Durata;

--posso decidere di ordinarli secondo un criterio, ex. Nome Completo
SELECT 
    s.StudenteId,
    s.Nome +' '+ s.Cognome as 'Nome Completo',
    ISNULL(c.NomeCorso, 'n/d') as 'Nome Corso',
    ISNULL(c.Durata, 0) as 'Durata Corso',
    COUNT(s.StudenteId) as 'Totale Studenti'
FROM Studenti AS s
LEFT JOIN Iscrizioni AS i
    ON i.StudenteId = s.StudenteId
LEFT JOIN Corsi AS C
    ON c.CorsoId = i.CorsoId
GROUP BY s.StudenteId, s.Nome, s.Cognome, c.NomeCorso, c.Durata
ORDER BY c.NomeCorso ASC;

--notiamo che abbiamo un solo studente per corso, normale per l'inserimento che abbiamo fatto
--faccio quindi un UPDATE:
UPDATE Iscrizioni
SET CorsoID = 1
WHERE StudenteId < 10;

--2.CONDIZIONI IF/ELSE (CASE THEN )
-- 1=c'è qualcosa, 0=non c'e nulla
--parentesi graffe all'inizio=BEGIN, alla fine=END, sono infatti intercambiabili (simboli e dicitura)
/*se esiste una riga degli studenti (select 1) allora 
(begin-select *...-end) verifichiamo tutti gli studenti
altrimenti (else) vado a stampare un msg (begin-print-end)*/
IF EXISTS (SELECT 1 FROM Studenti)
BEGIN 
    SELECT *
    FROM Studenti
END
ELSE
BEGIN
  PRINT 'Studente non trovato'
END;

--IF ANNODATO (ho l'1 ma prima della parentesi ho il NOT), mi darà 'Studente non trovato'
/*se inserisco IF NOT e 0 o 1 mi stampa la frase
se invece inserisco IF e 0 o 1 mi fa vedere lo studente 
a cosa mi serve questa modalità di Select??????????????????????????????????*/
IF EXISTS (SELECT 1 FROM Studenti)
BEGIN 
    SELECT *
    FROM Studenti
    WHERE StudenteId = 15
END
ELSE
BEGIN
  PRINT 'Studente non trovato'
END;

--voglio 2 stampe diverse per i casi che emergono
/*se tutti avessero la data di nascita allora verrebbe stampato il secondo BEGIN 
visto che invece ci sono delle date mancanti allora si crea la colonna 'Stato' dove viene indicato
la presenza o la mancanza della data di nascita*/
IF EXISTS (
    SELECT 1 
    FROM Studenti 
    WHERE DataNascita IS NULL
)
    BEGIN 
        SELECT 
        Nome,
        Cognome,
        CASE --condizione IF, verifica se è presente la data di nascita
            WHEN DataNascita IS NULL THEN 'Data Mancante'
            ELSE 'Data Presente'
        END AS Stato 
    FROM Studenti;
END
ELSE
BEGIN
  PRINT 'Tutti gli studenti hanno la data di nascita'
END;

-----da errore sintattico vicino il ; da ricontrollare
IF EXISTS(
    SELECT 1
    FROM Studenti
    WHERE DataNascita IS NULL
)
BEGIN    
    SELECT 
        Nome,
        Cognome,
        ISNULL(CONVERT(NVARCHAR, DataNascita, 107), 'DD/MM/YYYY') AS DataNascita,
        CASE 
            WHEN DataNascita IS NULL THEN 'Data Mancante'
            ELSE 'Data Presente'
END AS Stato 
FROM Studenti;



