CREATE DATABASE Trenuri;
GO
 
USE Trenuri;
GO
 
CREATE TABLE Tipuri_de_tren(
	IdTip INT PRIMARY KEY IDENTITY,
	Descriere VARCHAR(50)
);
 
CREATE TABLE Trenuri(
	IdTren INT PRIMARY KEY IDENTITY,
	Nume VARCHAR(50),
	IdTip INT FOREIGN KEY REFERENCES Tipuri_de_tren(IdTip)
);
 
CREATE TABLE Rute(
	IdRute INT PRIMARY KEY IDENTITY,
	Nume VARCHAR(50),
	IdTren INT FOREIGN KEY REFERENCES Trenuri(IdTren)
)
 
CREATE TABLE Statii(
	IdStatie INT PRIMARY KEY IDENTITY,
	Nume VARCHAR(50)
)
 
CREATE TABLE Rute_Statii(
	IdStatie INT FOREIGN KEY REFERENCES Statii(IdStatie),
	IdRute INT FOREIGN KEY REFERENCES Rute(IdRute),
	OraSosire TIME,
	OraPlecare TIME, 
	CONSTRAINT pk_Rute_Statii PRIMARY KEY(IdStatie, IdRute)
)

INSERT INTO Tipuri_de_tren(Descriere) VALUES
('Mocanita'),('Sageata Albastra'),('Personal');

SELECT * FROM Tipuri_de_tren
SELECT * FROM Trenuri
SELECT * FROM Rute
SELECT * FROM Statii
SELECT * FROM Rute_Statii

INSERT INTO Trenuri(Nume, IdTip) VALUES
('Thomas',2),('Percy',1),('Henry',3);

INSERT INTO Rute(Nume,IdTren) VALUES
('Baia Mare - Satu Mare',1), ('Cluj - Bucuresti',2), ('Constanta - Mamaia',3);

INSERT INTO Statii(Nume) VALUES
('GaraNord'),('GaraZzalau'),('GaraCluj');

INSERT INTO Rute_Statii(IdStatie,IdRute,OraSosire, OraPlecare) VALUES
(1,1,'20:00','18:00'), (2,2,'21:30','15:00'), (3,3,'22:30','17:00');

CREATE OR ALTER PROCEDURE procedura 
		@IdRute int,
		@IdStatie int, 
		@OraSosire time, 
		@OraPlecare time
as
begin
	if exists(select * from Rute_Statii 
				where IdStatie = @IdStatie and IdRute= @IdRute)
	begin
		update Rute_Statii 
		set OraSosire=@OraSosire, OraPlecare=@OraPlecare 
		where IdStatie = @IdStatie and IdRute= @IdRute

	end
	else
	begin
		insert into Rute_Statii(IdStatie, IdRute, OraSosire, OraPlecare)
		values(@IdStatie, @IdRute, @OraSosire, @OraPlecare)
	end
end

create or alter view RuteCuToateStatiile
as
	select R.nume as Nume_Ruta from Rute R
	where not exists(select 1 from Statii S
					where not exists(select 1 from Rute_Statii RS
									 where RS.IdRute = R.IdRute AND RS.IdStatie= S.IdStatie
									 )
					)