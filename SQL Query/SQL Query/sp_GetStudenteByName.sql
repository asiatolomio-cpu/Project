=========================================================================
-- Author : Asia Tolomio
-- Create date : 28/04/2026
-- Description : Questa query restituisce la lista di tutti gli studenti
=========================================================================
CREATE PROCEDURE sp_GetStudenteByName --nome della procedura
    @Nome NVARCHAR(100)  --definiamo  i parametri 
AS
BEGIN 
    SET NOCOUNT ON;
    --inseriamo qui la nostra query
    SELECT 
    StudenteId,
    Nome + ' ' + Cognome AS 'Nome Completo',
    ISNULL(CONVERT(NVARCHAR, DataNascita, 103), 'N/D') AS DataNascita,
    ISNULL(CONVERT(NVARCHAR, Email), 'N/E') AS Email,
    ISNULL(CONVERT(NVARCHAR, Telefono), 'N/D') AS Telefono,
    ISNULL(CONVERT(CHAR(16), CodiceFiscale), 'CF-NULL') AS CodiceFiscale
    FROM Studenti
    WHERE Nome = @Nome
END
GO

EXEC sp_GetStudenteByName 'Anna'