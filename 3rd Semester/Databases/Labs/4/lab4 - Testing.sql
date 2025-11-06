Use VideoGamesStore
go

INSERT INTO Tables(Name) VALUES ('Departament'),('Produs'),('Achizitie');
GO

CREATE VIEW VDepartament AS
	SELECT D.NumeD
	From Departament D
GO

CREATE VIEW VProdus AS
	SELECT P.NumePr, D.NumeD, P.Pret
	FROM Produs P INNER JOIN Departament D ON P.CodD = D.CodD
	WHERE P.Pret > 100
GO

CREATE VIEW VAchizitie AS
	SELECT P.NumePr,Ac.DataAchizitie,Ac.cantitate AS CantitateAchizitionata,P.Pret AS PretPerBuc,C.Nume,sum(P.pret *Ac.cantitate) as PretTotal
	FROM Produs P
	INNER JOIN Achizitie Ac ON P.CodPr = Ac.CodPr
	INNER JOIN Client C ON Ac.CodCl = C.CodCl
	GROUP BY P.NumePr,Ac.DataAchizitie,Ac.cantitate,P.Pret,C.Nume
GO

INSERT INTO Views(Name) VALUES ('VDepartament'),('VProdus'),('VAchizitie');
GO

INSERT INTO Tests(Name) VALUES
('Insert_10'),('Insert_100'),('Insert_1000'),
('Delete_10'),('Delete_100'),('Delete_1000'),
('Select_all');
GO

INSERT INTO TestViews VALUES 
(7,1),
(7,2),
(7,3);
GO

INSERT INTO TestTables VALUES
(1,1,10,1),
(2,1,100,1),
(3,1,1000,1),
(1,2,10,2),
(2,2,100,2),
(3,2,1000,2),
(1,3,10,3),
(2,3,100,3),
(3,3,1000,3),

(4,1,10,3),
(5,1,100,3),
(6,1,1000,3),
(4,2,10,2),
(5,2,100,2),
(6,2,1000,2),
(4,3,10,1),
(5,3,100,1),
(6,3,1000,1)
GO

-- Proceduri insert
CREATE OR ALTER PROCEDURE InsertDepartament		@rows int
AS
BEGIN
    DECLARE @id INT
    DECLARE @NumeD NVARCHAR(100)
    DECLARE @NrAngajati INT

    DECLARE @index INT
    DECLARE @lastId INT

    SET @NumeD = 'Jocuri Video'
    SET @NrAngajati = 10

    SET @index = 1
    SET @id = 1000

    WHILE @index <= @rows
    BEGIN
        SELECT TOP 1 @lastId = D.CodD FROM Departament D ORDER BY D.CodD DESC
        IF @lastId IS NULL
            SET @lastId = 1000
        SET @id = @lastId + 1

        SET IDENTITY_INSERT Departament ON
        INSERT INTO Departament(CodD, NumeD, NrAngajati)
        VALUES (@id, @NumeD + CAST(@index AS NVARCHAR), @NrAngajati + @index)
        SET IDENTITY_INSERT Departament OFF

        SET @index = @index + 1
    END
END
GO

CREATE OR ALTER PROCEDURE InsertProdus(@rows INT)
AS
BEGIN
    DECLARE @id INT
    DECLARE @NumePr NVARCHAR(100)
    DECLARE @Pret INT
    DECLARE @Cantitate INT
    DECLARE @CodD INT

    DECLARE @index INT
    DECLARE @lastId INT

    SET @NumePr = 'Joc video Adulti'
    SET @Pret = 100
    SET @Cantitate = 50
    SET @CodD = 1

    SET @index = 1
    SET @id = 2000

    WHILE @index <= @rows
    BEGIN
        SELECT TOP 1 @lastId = P.CodPr FROM Produs P ORDER BY P.CodPr DESC
        IF @lastId IS NULL
            SET @lastId = 2000
        SET @id = @lastId + 1

        SET IDENTITY_INSERT Produs ON
        INSERT INTO Produs(CodPr, NumePr, Pret, Cantitate, CodD)
        VALUES (@id, @NumePr + CAST(@index AS NVARCHAR), @Pret + (@index * 10), @Cantitate + @index, @CodD)
        SET IDENTITY_INSERT Produs OFF

        SET @index = @index + 1
    END
END
GO

CREATE OR ALTER PROCEDURE InsertAchizitie(@rows INT)
AS
BEGIN
    DECLARE @id INT
    DECLARE @DataAchizitie DATE
    DECLARE @MetodaPlata NVARCHAR(20)
    DECLARE @Cantitate INT
    DECLARE @CodPr INT
    DECLARE @CodCl INT

    DECLARE @index INT

    SET @DataAchizitie = GETDATE()
    SET @MetodaPlata = 'Cash'
    SET @Cantitate = 1
    SET @index = 1

    WHILE @index <= @rows
    BEGIN
        -- Alege un CodPr existent din Produs
        SELECT TOP 1 @CodPr = CodPr FROM Produs ORDER BY NEWID()

        -- Alege un CodCl existent din Client
        SELECT TOP 1 @CodCl = CodCl FROM Client ORDER BY NEWID()

        -- Verifică dacă perechea (CodPr, CodCl) există deja
        IF NOT EXISTS (
            SELECT 1
            FROM Achizitie
            WHERE CodPr = @CodPr AND CodCl = @CodCl
        )
        BEGIN
            -- Inserează o achiziție nouă
            INSERT INTO Achizitie (DataAchizitie, MetodaPlata, cantitate, CodPr, CodCl)
            VALUES (@DataAchizitie, @MetodaPlata, @Cantitate + @index, @CodPr, @CodCl)
        END
        ELSE
        BEGIN
            PRINT 'Perechea (' + CAST(@CodPr AS NVARCHAR) + ', ' + CAST(@CodCl AS NVARCHAR) + ') există deja. Se sare peste această inserare.'
        END

        SET @index = @index + 1
    END
END
GO

-- Proceduri delete
CREATE OR ALTER PROCEDURE DeleteDepartament(@rows INT)
AS
BEGIN
    DECLARE @id INT
    DECLARE @index INT
    DECLARE @lastId INT

    SET @index = @rows

    WHILE @index > 0
    BEGIN
        SELECT TOP 1 @lastId = D.CodD FROM Departament D ORDER BY D.CodD DESC

        IF @lastId IS NULL
            BREAK

        DELETE FROM Departament WHERE CodD = @lastId

        SET @index = @index - 1
    END
END
GO

CREATE OR ALTER PROCEDURE DeleteProdus(@rows INT)
AS
BEGIN
    DECLARE @id INT
    DECLARE @index INT
    DECLARE @lastId INT

    SET @index = @rows

    WHILE @index > 0
    BEGIN
        SELECT TOP 1 @lastId = P.CodPr FROM Produs P ORDER BY P.CodPr DESC

        IF @lastId IS NULL
            BREAK
		
		DELETE FROM Produs WHERE CodPr = @lastId

        SET @index = @index - 1
    END
END
GO

CREATE OR ALTER PROCEDURE DeleteAchizitie(@rows INT)
AS
BEGIN
    DECLARE @index INT
    DECLARE @lastCodPr INT
    DECLARE @lastCodCl INT

    SET @index = @rows

    WHILE @index > 0
    BEGIN
        SELECT TOP 1 @lastCodPr = A.CodPr, @lastCodCl = A.CodCl
        FROM Achizitie A
        ORDER BY A.DataAchizitie DESC, A.CodPr DESC, A.CodCl DESC

        IF @lastCodPr IS NULL OR @lastCodCl IS NULL
            BREAK

        DELETE FROM Achizitie WHERE CodPr = @lastCodPr AND CodCl = @lastCodCl

        SET @index = @index - 1
    END
END
GO


CREATE OR ALTER PROCEDURE Insert_10 	@Table varchar(30)
AS
BEGIN
	IF @Table = 'Departament'
		EXEC InsertDepartament 10
	IF @Table = 'Produs'
		EXEC InsertProdus 10
	IF @Table = 'Achizitie'
		EXEC InsertAchizitie 10
END
GO

CREATE OR ALTER PROCEDURE Insert_100	@Table varchar(30)
AS
BEGIN
	IF @Table = 'Departament'
		EXEC InsertDepartament 100
	IF @Table = 'Produs'
		EXEC InsertProdus 100
	IF @Table = 'Achizitie'
		EXEC InsertAchizitie 100
END
GO

CREATE OR ALTER PROCEDURE Insert_1000 	@Table varchar(30)
AS
BEGIN
	IF @Table = 'Departament'
		EXEC InsertDepartament 1000
	IF @Table = 'Produs'
		EXEC InsertProdus 1000
	IF @Table = 'Achizitie'
		EXEC InsertAchizitie 1000
END
GO

CREATE OR ALTER PROCEDURE Delete_10 	@Table varchar(30)
AS
BEGIN
	IF @Table = 'Departament'
		EXEC DeleteDepartament 10
	IF @Table = 'Produs'
		EXEC DeleteProdus 10
	IF @Table = 'Achizitie'
		EXEC DeleteAchizitie 10
END
GO

CREATE OR ALTER PROCEDURE Delete_100 	@Table varchar(30)
AS
BEGIN
	IF @Table = 'Departament'
		EXEC DeleteDepartament 100
	IF @Table = 'Produs'
		EXEC DeleteProdus 100
	IF @Table = 'Achizitie'
		EXEC DeleteAchizitie 100
END
GO

CREATE OR ALTER PROCEDURE Delete_1000 	@Table varchar(30)
AS
BEGIN
	IF @Table = 'Departament'
		EXEC DeleteDepartament 1000
	IF @Table = 'Produs'
		EXEC DeleteProdus 1000
	IF @Table = 'Achizitie'
		EXEC DeleteAchizitie 1000
END
GO

CREATE OR ALTER PROCEDURE Select_all @View varchar(30)
AS
BEGIN
	IF @View = 'Departament'
		SELECT * FROM VDepartament
	IF @View = 'Produs'
		SELECT * FROM VProdus
	IF @View = 'Achizitie'
		SELECT * FROM VAchizitie
END
GO

CREATE or ALTER PROCEDURE rulare (@Table VARCHAR(30))
AS
BEGIN
    DECLARE @date1 DATETIME, @date2 DATETIME, @date3 DATETIME
    DECLARE @descriere NVARCHAR(2000)

    DECLARE @testInsert VARCHAR(40)
    DECLARE @testDelete VARCHAR(40)
    DECLARE @nrRows int
    DECLARE @idTest int

    DECLARE @id_table int
    DECLARE @id_view int

    SELECT @id_table = TableID FROM Tables WHERE Name = @Table
    SELECT @id_view = ViewID FROM Views WHERE Name = 'V' + @Table

    SET @nrRows = 1000
    SET @testInsert = 'Insert_' + CONVERT(VARCHAR(5), @nrRows)
    SET @testDelete = 'Delete_' + CONVERT(VARCHAR(5), @nrRows)

    SET @date1 = GETDATE()
    exec @testInsert @Table
    exec @testDelete @Table

    SET @date2 = GETDATE()
    exec Select_all @Table

    SET @date3 = GETDATE()
    SET @descriere = N'Testele: ' + @testInsert + ', ' + @testDelete + ', si view-urile pe' + @Table

    INSERT INTO TestRuns VALUES (@descriere, @date1, @date3)
    SELECT TOP 1 @idTest = T.TestRunID FROM dbo.TestRuns T ORDER BY T.TestRunID DESC
    INSERT INTO TestRunTables VALUES (@idTest, @id_table, @date1, @date2)
    INSERT INTO TestRunViews VALUES (@idTest, @id_view, @date2, @date3)

END
GO

CREATE or ALTER PROCEDURE run
AS
BEGIN
    DECLARE @index int
    SELECT @index = COUNT(*) FROM Tables
    DECLARE @tableName VARCHAR(20)

    DECLARE cursorTable CURSOR SCROLL FOR
        SELECT name FROM Tables;

    OPEN cursorTable;
        FETCH LAST FROM cursorTable INTO @tableName

    WHILE @index > 0 AND @@FETCH_STATUS = 0
    BEGIN
        EXEC rulare @tableName
        print @tableName
        FETCH PRIOR FROM cursorTable INTO @tableName;
        SET @index = @index - 1
    END

    CLOSE cursorTable;
    DEALLOCATE cursorTable;
END
GO

exec run
select * from TestRuns
select * from TestRunTables
select * from TestRunViews


delete from Achizitie

select * from Departament
select * from Produs
select * from Achizitie

select * from Views
select * from Tables
select * from Tests
select * from TestTables
select * from TestViews