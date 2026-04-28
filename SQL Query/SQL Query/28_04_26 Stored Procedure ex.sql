--3.Stored Procedure
/*sono query o blocchi di query salvati nel database per esecuzioni ripetute e automatizzate
rende il lavoro più veloce e sicuro
Seleziono il db 
Vado su "Programmability"
poi su "Stored Procedure"
tasto destro e poi di nuovo "Stored Procedure"
in automatico si apriranno righe di codice per la documentazione
in realtà la base sarebbe la seguente */
=========================================================================
-- Author : Asia Tolomio
-- Create date : 28/04/2026
-- Description : Questa query restituisce la lista di tutti gli studenti
=========================================================================
CREATE PROCEDURE sp_GetAllStudenti --nome della procedura
AS
BEGIN --inseriamo qui la nostra query
    SELECT *
    FROM Studenti;
END
GO

---Esecuzione della stored procedure
EXEC sp_GetAllStudenti;

/*per alcune query devo definire un parametro, con nome, tipo di dato ed eventualmente lunghezza*/




/*se ci fosse un parametro e devo cercare un dato o più dati in particolare,
lo inserisco dopo EXEC sp_NomeStoredProcedure
e in automatico mi da il risultato desiderato*/








--4.View come viste
--5.Back up standard e automatizzata del database