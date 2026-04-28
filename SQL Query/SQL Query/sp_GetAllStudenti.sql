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