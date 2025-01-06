use VideoGamesStore
go

-- Modificare tip coloana
CREATE PROCEDURE ChangeNumePr_ToNVarChar
AS
BEGIN
	ALTER TABLE Produs
	ALTER COLUMN NumePr NVARCHAR(100) NOT NULL 
	PRINT 'Tipul coloanei NumePr s-a modificat la NVARCHAR'
END

-- Undo modificare tip coloana
CREATE PROCEDURE ChangeNumePr_Back
AS
BEGIN
	ALTER TABLE Produs
	ALTER COLUMN NumePr VARCHAR(100) NOT NULL 
	PRINT 'Tipul Coloanei NumePr a revenit la VARCHAR'
END

-- Adaugare constrangere default
CREATE PROCEDURE AddDefaultPLataPeOra
AS
BEGIN
	ALTER TABLE Angajat
	ADD CONSTRAINT df_PlataPeOra DEFAULT 10 FOR PlataPeOra
	PRINT 'S-a adaugat constrangere default la coloana PlataPeOra'
END

-- Undo adaugare constrangere default
CREATE PROCEDURE RemoveDefaultPLataPeOra
AS
BEGIN
	ALTER TABLE Angajat
	DROP CONSTRAINT df_PlataPeOra 
	PRINT 'S-a sters constrangerea default la coloana PlataPeOra'
END

-- Creare tabela noua
CREATE PROCEDURE AddTable
AS
BEGIN
	CREATE TABLE Periferice
	(	
		CodPrf INT NOT NULL PRIMARY KEY,
		NumePrf VARCHAR(50) NOT NULL
	)
	PRINT 'S-a adaugat tabela Periferice'
END

-- Stergere tabela noua
CREATE PROCEDURE DeleteTable
AS
BEGIN
	DROP TABLE Periferice
	PRINT 'S-a sters tabela Periferice'
END

-- Adaugare camp nou
CREATE PROCEDURE AddColumn
AS
BEGIN
	ALTER TABLE Periferice
	ADD Producator VARCHAR(50)
	PRINT 'S-a adaugat coloana Producator in tabela Periferice'
END

-- Stergere camp adaugat
CREATE PROCEDURE RemoveColumn
AS
BEGIN
	ALTER TABLE Periferice
	DROP COLUMN Producator
	PRINT 'S-a sters coloana Producator din tabela Periferice'
END

-- Creare constrangere fk
CREATE PROCEDURE AddForeignKey
AS
BEGIN
	ALTER TABLE Periferice
	ADD CONSTRAINT FK_CodPrf
	FOREIGN KEY (CodPrf) REFERENCES Produs(CodP)
	PRINT 'S-a adaugat constrangere de cheie straina'
END

-- Stergere constrangere fk
CREATE PROCEDURE RemoveForeignKey
AS
BEGIN
	ALTER TABLE Periferice
	DROP CONSTRAINT FK_CodPrf
	PRINT 'S-a sters constrangere de cheie straina'
END

-- Ajutor pt Procedura Principala

CREATE TABLE VersionTable
(	VersionNumber INT DEFAULT 0 NOT NULL
);

CREATE TABLE DirectProcedures
(	IdDir INT PRIMARY KEY,
	NumePr varchar(100));

CREATE TABLE ReverseProcedures
(	IdRev INT PRIMARY KEY,
	NumePr varchar(100));

INSERT INTO DirectProcedures VALUES
(0,'ChangeNumePr_ToNVarChar'),
(1,'AddDefaultPlataPeOra'),
(2,'AddTable'),
(3,'AddColumn'),
(4,'AddForeignKey')

INSERT INTO ReverseProcedures VALUES
(1,'ChangeNumePr_Back'),
(2,'RemoveDefaultPlataPeOra'),
(3,'DeleteTable'),
(4,'RemoveColumn'),
(5,'RemoveForeignKey')

SELECT * FROM DirectProcedures
SELECT * FROM ReverseProcedures

EXEC ChangeNumePr_ToNVarChar
EXEC AddDefaultPlataPeOra

EXEC AddTable

EXEC AddColumn

EXEC AddForeignKey

EXEC RemoveForeignKey
EXEC RemoveColumn
EXEC DeleteTable
EXEC RemoveDefaultPLataPeOra
EXEC ChangeNumePr_Back


-- Procedura Principala

CREATE PROCEDURE MAIN
@Versiune int
AS
BEGIN
	 IF @Versiune>5
	 BEGIN
		 RAISERROR('Versiune invalida', 16, 1);
		RETURN;
	 END

	 DECLARE @Versiune_actuala AS INT
	 SELECT @Versiune_actuala = Number
	 FROM Versiune;

	 PRINT 'versiunea actuala este :'; 
	 PRINT @Versiune_actuala;
	 PRINT 'Schimbam la veriunea :'; 
	 PRINT @Versiune;

	 IF @Versiune=@Versiune_actuala
	 BEGIN
		PRINT 'Suntem deja in aceasta versiune!';
		RETURN;
	 END

	 DECLARE @Functie AS varchar(100);


	 IF @Versiune>@Versiune_actuala
	 BEGIN
		WHILE @Versiune!=@Versiune_actuala
		BEGIN

			SELECT @Functie = NumePr
			FROM DirectProcedures
			where @Versiune_actuala=IdDir;

			EXECUTE @Functie;

			SET @Versiune_actuala=@Versiune_actuala+1;

		END

		UPDATE Versiune
		SET Number = @Versiune;

		RETURN;
	 END
	 
	 -- altfel daca  @Versiune < @Versiune_actuala

	 WHILE @Versiune!=@Versiune_actuala
		BEGIN

			set @Versiune_actuala=@Versiune_actuala-1;

			SELECT @Functie = NumePr
			FROM ReverseProcedures
			where @Versiune_actuala=IdRev;

			EXECUTE @Functie;
		END
	 
	 UPDATE Versiune
	 SET Number = @Versiune;
	 RETURN;
END

exec main 0;