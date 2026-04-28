USE AziendaDb;
GO

-- 1. SUBQUERY (SOTTORAQUERY)
/*
	SELECT 
		---*---
	FROM ------
	WHERE CONDIZIONE CON (
		SELECT 
			---*---
		FROM --
	)
*/
SELECT 
	AVG(Totale) AS Media
FROM Ordini; -- 920.833333

-- Ordini sopra la media
SELECT 
	* 
FROM Ordini
where Totale > (
	SELECT 
		AVG(Totale) AS Media
	FROM Ordini
);


-- Ordini sotto la media
SELECT 
	* 
FROM Ordini
where Totale > (
	SELECT 
		AVG(Totale) AS Media
	FROM Ordini
);


-- Clienti senza ordini CON (NOT IN)
SELECT ClienteID FROM Ordini;

SELECT *
FROM Clienti
WHERE ClienteID NOT IN(
	SELECT ClienteID FROM Ordini	
);


-- Ordini sopra la media del cliente
SELECT 
	AVG(Totale) as Media
FROM Ordini
WHERE Totale > (
	SELECT 
		AVG(Totale) as Media
	FROM Ordini
);

SELECT AVG(o.Totale) AS 'Sopra media'
FROM Ordini o
INNER JOIN Ordini oo
	ON o.ClienteID = oo.ClienteID
	


SELECT 
	*
FROM Ordini AS o
WHERE Totale > (
	SELECT 
		AVG(Totale) AS 'Sopra media'
	FROM Ordini oo
	WHERE o.ClienteID = oo.ClienteID
);

-- Ordini sopra la media del cliente
SELECT 
	o.OrdineID,
	o.ClienteID,
	o.Totale,
	M.MediaCliente
FROM Ordini AS o
INNER JOIN (
	SELECT
		ClienteID,
		AVG(Totale) AS MediaCliente
	FROM Ordini 
	GROUP BY ClienteID
) AS M ON o.ClienteID = M.ClienteID
WHERE 
	o.Totale > M.MediaCliente


UPDATE Ordini
SET Totale = 10000
WHERE OrdineID = 36;

SELECT * FROM Ordini WHERE OrdineID = 36;

SELECT 
	ClienteID,
	AVG(Totale) AS Media
FROM Ordini
GROUP BY ClienteID

-- 2. WHERE E HAVING
/*
	SELECT 
		---*---
	FROM ------
	GROUP BY --
	HAVING ----
*/
SELECT 
	Prodotto,
	SUM(Quantita) AS Quantita
FROM DettagliOrdine
GROUP BY Prodotto
HAVING SUM(Quantita) > 5


-- 3. DATA IN SQL SERVER
SELECT 
	*
FROM Ordini 
where DataOrdine >= DATEADD(DAY, -30, GETDATE());
	 
-- Ordini per mese 
SELECT 
	CONVERT(NVARCHAR, YEAR(DataOrdine)) AS Anno,
	CONVERT(NVARCHAR, MONTH (DataOrdine)) AS Mese,
	CONVERT(NVARCHAR, DAY(DataOrdine)) AS Giorno
FROM Ordini

-- 4. TUTTI I JOIN {Left join, Right join, inner join, join}
-- 5. CONDIZIONI IF/ELSE (CASE THEN ) == se / ALTRIMENTI
-- 6. STORE PROCEDURE 
-- 7. VIEW = VISTE
-- 8. BACK-UP STANDARD E AUTOMATIZZATA DEL DB