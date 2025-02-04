use VideoGamesStore
go

CREATE OR ALTER FUNCTION ValidareStringNenulMic (@sir varchar(10))
RETURNS INT
AS 
BEGIN
	IF @sir IS NOT NULL and @sir <> ''
	BEGIN 
		RETURN 1
	END
	RETURN 0
END
GO

CREATE OR ALTER FUNCTION ValidareZi (@sir varchar(10))
RETURNS INT
AS
BEGIN
	IF @sir in ('Luni','Marti','Miercuri','Joi','Vineri','Sambata','Duminica')
	BEGIN
		RETURN 1
	END
	RETURN 0
END
GO

CREATE OR ALTER FUNCTION ValidareStringNenul (@sir varchar(100))
RETURNS INT
AS 
BEGIN
	IF @sir IS NOT NULL and @sir <> ''
	BEGIN 
		RETURN 1
	END
	RETURN 0
END
GO

CREATE OR ALTER FUNCTION ValidareStringNenulMare (@sir varchar(500))
RETURNS INT
AS 
BEGIN
	IF @sir IS NOT NULL and @sir <> ''
	BEGIN 
		RETURN 1
	END
	RETURN 0
END
GO

CREATE OR ALTER FUNCTION ValidareOra (@ora time)
RETURNS INT
AS
BEGIN
    IF @ora LIKE '[0-2][0-9] AM' OR @ora LIKE '[0-2][0-9] PM'
    BEGIN
        RETURN 1 
    END
	RETURN 0 
END
GO

CREATE OR ALTER FUNCTION ValidareNumarPozitiv (@numar int)
returns bit
AS
BEGIN
	IF @numar > 0
	BEGIN
		RETURN 1
	END
	RETURN 0
END
GO

CREATE OR ALTER PROCEDURE ValidareDepartament
	@NumeD varchar(100),
	@NrAngajati int,
	@valid bit output
AS
BEGIN
	DECLARE @StringValid int
	DECLARE @NumarValid int

	SET @StringValid = dbo.ValidareStringNenul(@NumeD)
	SET @NumarValid = dbo.ValidareNumarPozitiv(@NrAngajati)

	IF @StringValid = 1 AND @NumarValid = 1
	BEGIN 
		SET @valid = 1 
	END
	ELSE
	BEGIN 
		SET @valid = 0
	END
END
GO

CREATE OR ALTER PROCEDURE CRUD_Departament 
	@NumeD varchar(100),
	@NrAngajati int
AS
BEGIN
	SET NOCOUNT ON

	DECLARE @Verificare bit
	exec dbo.ValidareDepartament @NumeD = @NumeD, @NrAngajati = @NrAngajati, @valid = @Verificare OUTPUT;
	IF @Verificare = 0
	BEGIN 
		PRINT 'Datele introduse nu sunt valide!'
		RETURN;
	END

	INSERT INTO Departament(NumeD,NrAngajati) VALUES (@NumeD, @NrAngajati)

	SELECT * FROM Departament

	UPDATE Departament
	SET NumeD = @NumeD + '_update'
	WHERE Departament.NumeD = @NumeD and Departament.NrAngajati = @NrAngajati
	SELECT * FROM Departament

	DELETE FROM Departament
	WHERE Departament.NumeD LIKE @NumeD + '_update'
	SELECT * FROM Departament

	PRINT 'Operatii CRUD pentru Departament efectuate'
END

EXEC CRUD_Departament 'AccesoriiConsole', 100
EXEC CRUD_Departament 'AccesoriiConsole', -100
EXEC CRUD_Departament '', 100

CREATE OR ALTER PROCEDURE ValidarePozitie
	@Titlu varchar(100),
	@Atributii varchar(500),
	@valid bit output
AS
BEGIN
	DECLARE @StringValid1 int
	DECLARE @StringValid2 int

	SET @StringValid1 = dbo.ValidareStringNenul(@Titlu)
	SET @StringValid2 = dbo.ValidareStringNenulMare(@Atributii)

	IF @StringValid1 = 1 AND @StringValid2 = 1
	BEGIN 
		SET @valid = 1 
	END
	ELSE
	BEGIN 
		SET @valid = 0
	END
END
GO

CREATE OR ALTER PROCEDURE CRUD_Pozitie
	@Titlu varchar(100),
	@Atributii varchar(500)
AS
BEGIN
	SET NOCOUNT ON

	DECLARE @Verificare bit
	exec dbo.ValidarePozitie @Titlu = @Titlu, @Atributii = @Atributii, @valid = @Verificare OUTPUT;
	IF @Verificare = 0
	BEGIN 
		PRINT 'Datele introduse nu sunt valide!'
		RETURN;
	END

	INSERT INTO Pozitie(Titlu,Atributii) VALUES (@Titlu, @Atributii)

	SELECT * FROM Pozitie

	UPDATE Pozitie 
	SET Pozitie.Titlu = @Titlu + '_update', Pozitie.Atributii = @Atributii + '_update'
	WHERE Pozitie.Titlu = @Titlu AND Pozitie.Atributii = @Atributii
	SELECT * FROM Pozitie

	DELETE FROM Pozitie
	WHERE Pozitie.Titlu LIKE @Titlu + '_update' AND Pozitie.Atributii LIKE @Atributii + '_update'
	SELECT * FROM Pozitie

	PRINT 'Operatii CRUD pentru Pozitie efectuate'
END


EXEC CRUD_Pozitie 'Manager', 'Munca in echipa'
EXEC CRUD_Pozitie '',''


CREATE OR ALTER PROCEDURE ValidareAngajat
	@Nume varchar(100),
	@PlataPeOra int,
	@valid bit output
AS
BEGIN
	DECLARE @StringValid INT
	DECLARE @NumarValid INT

	SET @StringValid = dbo.ValidareStringNenul(@Nume)
	SET @NumarValid = dbo.ValidareNumarPozitiv(@PlataPeOra)

	IF @StringValid = 1 AND @NumarValid = 1 --AND
	BEGIN 
		SET @valid = 1 
	END
	ELSE
	BEGIN 
		SET @valid = 0
	END
END
GO

CREATE OR ALTER PROCEDURE CRUD_Angajat
	@Nume varchar(100),
	@PlataPeOra int
AS
BEGIN
	SET NOCOUNT ON

	DECLARE @Verificare bit
	exec dbo.ValidareAngajat @Nume = @Nume, @PlataPeOra = @PlataPeOra, @valid = @Verificare OUTPUT;
	IF @Verificare = 0
	BEGIN 
		PRINT 'Datele introduse nu sunt valide!'
		RETURN;
	END
	declare @cheie_pozitie int

	SELECT TOP 1 @cheie_pozitie = CodP
	FROM Pozitie
	ORDER BY CodP
	
	declare @cheie_departament int
	SELECT TOP 1 @cheie_departament = CodD
	FROM Departament
	ORDER BY CodD

	INSERT INTO Angajat(Nume,PlataPeOra,CodP, CodD) VALUES (@Nume, @PlataPeOra, @cheie_pozitie,@cheie_departament)

	SELECT * FROM Angajat

	UPDATE Angajat 
	SET Angajat.Nume = @Nume + '_update'
	WHERE Angajat.Nume = @Nume AND Angajat.PlataPeOra = @PlataPeOra
	SELECT * FROM Angajat

	DELETE FROM Angajat
	WHERE Angajat.Nume = @Nume + '_update' AND Angajat.PlataPeOra = @PlataPeOra
	SELECT * FROM Angajat

	PRINT 'Operatii CRUD pentru Angajat efectuate'
END

exec CRUD_Angajat 'Andrei Cosma',60
exec CRUD_Angajat '',35


CREATE OR ALTER PROCEDURE ValidareProgram
	@Zi varchar(10),
	@OraIncepere varchar(10),
	@OraSfarsit varchar(10),
	@valid bit output
AS
BEGIN
	DECLARE @StringValid int
	DECLARE @Oravalida1 int
	DECLARE @OraValida2 int

	SET @StringValid = dbo.ValidareZi(@Zi)
	SET @Oravalida1 = dbo.ValidareStringNenulMic(@OraIncepere)
	SET @Oravalida2 = dbo.ValidareStringNenulMic(@OraSfarsit)

	IF @StringValid = 1 AND @Oravalida1 = 1 AND @OraValida2 = 1
	BEGIN 
		SET @valid = 1 
	END
	ELSE
	BEGIN 
		SET @valid = 0
	END
END
GO

CREATE OR ALTER PROCEDURE CRUD_Program
	@Zi varchar(10),
	@OraIncepere varchar(10),
	@OraSfarsit varchar(10)
AS
BEGIN
	SET NOCOUNT ON

	DECLARE @Verificare bit
	exec dbo.ValidareProgram @Zi = @Zi, @OraIncepere = @OraIncepere, @OraSfarsit = @OraSfarsit ,@valid = @Verificare OUTPUT;
	IF @Verificare = 0
	BEGIN 
		PRINT 'Datele introduse nu sunt valide!'
		RETURN;
	END

	INSERT INTO Program(Zi,OraIncepere, OraSfarsit) VALUES (@Zi, @OraIncepere, @OraSfarsit)

	SELECT * FROM Program

	UPDATE Program 
	SET Program.Zi = @Zi + '_'
	WHERE Program.Zi = @Zi AND Program.OraIncepere = @OraIncepere and Program.OraSfarsit = @OraSfarsit
	SELECT * FROM Program

	DELETE FROM Program
	WHERE Program.Zi = @Zi + '_'
	SELECT * FROM Program

	PRINT 'Operatii CRUD pentru Departament efectuate'
END

EXEC CRUD_Program 'Marti', '08 AM', '03 PM'
EXEC CRUD_Program 'Azi', '8 PM','9 PM'
EXEC CRUD_Program 'Azi','','9 PM'


CREATE OR ALTER PROCEDURE ValidareAngajatProgram
	@CodA int,
	@CodProg int,
	@valid INT OUTPUT
AS
BEGIN
	DECLARE @valid1 int
	DECLARE @valid2 int

	SET @valid1=1
	SET @valid2=1
	IF NOT EXISTS(SELECT 1 FROM Angajat WHERE CodA = @CodA)
	BEGIN
		SET @valid1=0
	END

	IF NOT EXISTS(SELECT 1 FROM Program WHERE CodProg = @CodProg)
	BEGIN
		SET @valid2=0
	END

	IF @valid1=1 AND @valid2=1
	BEGIN 
		SET @valid =1 
	END
	ELSE
	BEGIN
		SET @valid = 0
	END
END

alter table AngajatProgram
	add update_column varchar(10);

CREATE OR ALTER PROCEDURE CRUD_AngajatProgram
	@CodA int,
	@CodProg int
AS
BEGIN
	SET NOCOUNT ON

	DECLARE @Verificare bit
	exec dbo.ValidareAngajatProgram @CodA = @CodA, @CodProg = @CodProg, @valid = @Verificare OUTPUT;
	IF @Verificare = 0
	BEGIN 
		PRINT 'Datele introduse nu sunt valide!'
		RETURN;
	END

	INSERT INTO AngajatProgram(CodA,CodProg) VALUES (@CodA, @CodProg)

	SELECT * FROM AngajatProgram

	UPDATE AngajatProgram 
	SET AngajatProgram.update_column = 'yes'
	WHERE AngajatProgram.CodA = @CodA AND AngajatProgram.CodProg = @CodProg
	SELECT * FROM AngajatProgram

	DELETE FROM AngajatProgram
	WHERE AngajatProgram.update_column = 'yes'
	SELECT * FROM AngajatProgram

	PRINT 'Operatii CRUD pentru AngajatProgram efectuate'
END

exec CRUD_AngajatProgram 10,100
exec CRUD_AngajatProgram 7,9

select * from AngajatProgram
select * from Angajat
select * from Program


use VideoGamesStore
go

create or alter view ViewDepartament
as
	select D.NumeD,D.NrAngajati 
	from Departament D
	where NumeD like '%j%'

select * from ViewDepartament ORDER BY ViewDepartament.NumeD

create or alter view ViewAngajat
as
	select A.Nume,P.Titlu,D.NumeD,A.PlataPeOra
	from Angajat A
	inner join Pozitie P on A.CodP=P.CodP
	inner join Departament D on A.CodD=D.CodD
	WHERE PlataPeOra>15


create or alter view ViewPozitie
as
	select P.Titlu,P.Atributii,A.PlataPeOra
	from Pozitie P
	inner join Angajat A on P.CodP=A.CodP
	where Titlu LIKE '%Lucrator'


create or alter view ViewProgram
as
	select P.Zi, P.OraIncepere,A.Nume
	from Program P
	inner join AngajatProgram on P.CodProg=AngajatProgram.CodProg
	inner join Angajat A on AngajatProgram.CodA=A.CodA
	where OraIncepere<'12:00'


create or alter view ViewAngajatProgram
as
	select AP.CodA
	from AngajatProgram AP
	inner join Angajat A on AP.CodA=A.CodA
	inner join Pozitie P ON A.CodP=P.CodP
	inner join Program Prog on AP.CodProg=Prog.CodProg
	where Zi in ('Luni','Marti','Joi')


if exists(select name from sys.indexes where name='N_idx_Departament')
drop index N_idx_Departament on Departament
create nonclustered index N_idx_Departament on Departament(NumeD)

if exists(select name from sys.indexes where name='N_idx_Angajat')
drop index N_idx_Angajat on Angajat
create nonclustered index N_idx_Angajat on Angajat(Nume)

if exists(select name from sys.indexes where name='N_idx_Pozitie')
drop index N_idx_Pozitie on Pozitie
create nonclustered index N_idx_Pozitie on Pozitie(Titlu)

if exists(select name from sys.indexes where name='N_idx_Program')
drop index N_idx_Program on Program
create nonclustered index N_idx_Program on Program(OraIncepere)

if exists(select name from sys.indexes where name='N_idx_AP')
drop index N_idx_AP on AngajatProgram
create nonclustered index N_idx_AP on AngajatProgram(CodA)

