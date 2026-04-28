-- =============================================
-- Author:		--tuo nome
-- Create date: 28/04/2026
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE --
AS
BEGIN
    -- Insert statements for procedure here
	IF EXISTS
	(
		SELECT 1
		FROM Iscrizioni
	)
	BEGIN
		----
	END
	ELSE
		BEGIN
			PRINT 'Nessuna isczizione presente';
		END

END;
GO
