-- Author : Asia Tolomio
-- Create date : 15/05/2026
-- Description : Questa query restituisce la lista di tutte le tabelle presenti in un database SQL Server.

CREATE PROCEDURE sp_ListaTabelle 
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT TABLE_NAME 
	FROM INFORMATION_SCHEMA.TABLES
	WHERE TABLE_TYPE='BASE TABLE'
	ORDER BY TABLE_NAME ASC
END
GO

---Esecuzione della stored procedure
EXEC sp_ListaTabelle;