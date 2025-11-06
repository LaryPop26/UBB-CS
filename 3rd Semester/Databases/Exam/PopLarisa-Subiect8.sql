CREATE DATABASE Biblioteca
GO

USE Biblioteca
GO

-- Creare tabele
CREATE TABLE Carte(
	IdCarte INT PRIMARY KEY IDENTITY,
	Titlu VARCHAR(100) NOT NULL,
	Editura VARCHAR(100),
	AnAparitie INT NOT NULL
);

CREATE TABLE Poveste(
	IdPoveste INT PRIMARY KEY IDENTITY,
	Denumire VARCHAR(100) NOT NULL,
	Autor VARCHAR(100) NOT NULL,
	AnScriere INT NOT NULL,
	NrPagini INT,
	IdCarte INT FOREIGN KEY REFERENCES Carte(IdCarte)
);

CREATE TABLE BibliotecaT(
	IdBibliotecaT INT PRIMARY KEY IDENTITY,
	Denumire VARCHAR(100) NOT NULL,
	AnInfiintare INT,
	Oras VARCHAR(100),
	Strada VARCHAR(100),
	Numar INT
	);

CREATE TABLE Copil(
	IdCopil INT PRIMARY KEY IDENTITY,
	Nume VARCHAR(100) NOT NULL,
	Prenume VARCHAR(100) NOT NULL,
	Gen CHAR(1) CHECK (Gen IN ('M', 'F')) NOT NULL,
	DataNastere DATE,
	IdBibliotecaT INT FOREIGN KEY REFERENCES BibliotecaT(IdBibliotecaT)
);

CREATE TABLE CopilPoveste(
	IdCopil INT FOREIGN KEY REFERENCES Copil(IdCopil),
	IdPoveste INT FOREIGN KEY REFERENCES Poveste(IdPoveste),
	Durata TIME ,
	NrPuncte INT CHECK (NrPuncte>=0 AND NrPuncte<=5),
	CONSTRAINT pk_CopilPoveste PRIMARY KEY (IdCopil,IdPoveste)
	);

-- Insert valori
INSERT INTO Carte(Titlu,Editura,AnAparitie) VALUES
('Narnia','Litera',2019),
('Povesti din popor','Art',2015);

INSERT INTO Poveste(Denumire,Autor,AnScriere,NrPagini,IdCarte) VALUES
('Capitolul 1','Nae Ion',2018,15,1),
('Pe ulita','Anonim',2013,20,2),
('In sat','Grigore Avram',2017,10,2)

INSERT INTO BibliotecaT(Denumire,AnInfiintare,Oras,Strada,Numar) VALUES
('Biblioteca Municipala',2000,'Cluj-Napoca','Universitatii',2),
('Biblioteca Universala',1985,'Baia Mare','Unirii',3);

INSERT INTO Copil(Nume,Prenume,Gen,DataNastere,IdBibliotecaT) VALUES
('Popescu','Ion','M','2010-03-05',1),
('Iacob','Diana','F','2011-05-06',2)

INSERT INTO CopilPoveste(IdCopil,IdPoveste,Durata,NrPuncte) VALUES
(1,1,'03:00',3),
(2,2,'04:00',5),
(1,3,'01:00',4),
(2,3,'01:30',2)

SELECT * FROM Carte
SELECT * FROM Poveste
SELECT * FROM BibliotecaT
SELECT * FROM Copil
SELECT * FROM CopilPoveste


-- Validare NrPuncte
CREATE FUNCTION VerificareNrPuncte(@NrPuncte int)
RETURNS INT
AS
BEGIN
	IF @NrPuncte >=0 AND @NrPuncte<=5
		RETURN 1;
	RETURN 0
END

-- Procedura
CREATE OR ALTER PROCEDURE AdaugaPoveste
	@IdCopil INT,
	@IdPoveste INT,
	@Durata TIME,
	@NrPuncte INT
AS
BEGIN
	IF dbo.VerificareNrPuncte(@NrPuncte) = 0
	BEGIN
		RAISERROR ('Nr puncte invalid',16,1)
		RETURN;
	END

	IF NOT EXISTS(SELECT 1 FROM Copil WHERE IdCopil = @IdCopil)
	BEGIN
		RAISERROR ('IdCopil neexistent',16,1)
		RETURN;
	END

	IF NOT EXISTS(SELECT 1 FROM Poveste WHERE IdPoveste = @IdPoveste)
	BEGIN
		RAISERROR ('IdPoveste neexistent',16,1)
		RETURN;
	END
		
	IF EXISTS(SELECT 1 FROM CopilPoveste
			  WHERE IdCopil=@IdCopil AND IdPoveste=@IdPoveste)
	BEGIN
		UPDATE CopilPoveste
		SET Durata=@Durata, NrPuncte=@NrPuncte
		WHERE IdCopil=@IdCopil AND IdPoveste=@IdPoveste
	END
	ELSE
	BEGIN
		INSERT INTO CopilPoveste(IdCopil,IdPoveste,Durata,NrPuncte)
		VALUES (@IdCopil,@IdPoveste,@Durata,@NrPuncte)
	END
END
GO


SELECT * FROM CopilPoveste
EXEC AdaugaPoveste 2,1,'02:00',3


EXEC AdaugaPoveste 1,2,'05:00',8
EXEC AdaugaPoveste 5,1,'05:00',4
EXEC AdaugaPoveste 1,5,'05:00',4

-- View
CREATE OR ALTER VIEW TopPovesti
AS
	SELECT P.Denumire as Denumire_Poveste,COUNT(CP.IdCopil) AS NrCopii
	FROM Poveste P
	INNER JOIN CopilPoveste CP ON P.IdPoveste = CP.IdPoveste
	GROUP BY P.Denumire
	HAVING COUNT(CP.IdCopil) = (SELECT MAX(NrCititori) 
								FROM (SELECT COUNT(IdCopil) AS NrCititori
									FROM CopilPoveste
									GROUP BY IdPoveste
									) AS Subquery
    );

SELECT * FROM TopPovesti
SELECT * FROM CopilPoveste