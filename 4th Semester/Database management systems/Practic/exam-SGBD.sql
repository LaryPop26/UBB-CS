USE master
GO
IF(EXISTS(SELECT * FROM sys.databases WHERE name='Masini'))
	DROP DATABASE Masini;
GO
CREATE DATABASE Masini;
GO
USE Masini;
GO

CREATE TABLE Colectie(
	CodColectie int primary key identity,
	NumeColectie varchar(100),
	CategorieIstorica varchar(100)
	);


CREATE TABLE Masina( 
	CodMasina int primary key identity,
	Marca varchar(100),
	Model varchar(100),
	AnFabricatie int,
	ValoareEstimata int,
	Proprietar varchar(100),
	CodColectie int foreign key REFERENCES Colectie(CodColectie)
	);

insert into Colectie values
('Colectie Interbelica', 'interbelica'),
('Colectie Postmoderna', 'postmoderna');

insert into Masina (Marca, Model, AnFabricatie, ValoareEstimata, Proprietar, CodColectie) values
('Ford', 'Model T', 1925, 30000, 'Ion Popescu', 1),
('Chevrolet', 'Bel Air', 1957, 45000, 'Ana Georgescu', 1),
('Tesla', 'Model 3', 2022, 42000, 'Radu Ionescu', 2),
('Dacia', 'Logan', 2007, 6000, 'Maria Popa', 2);

select * from Masina
select * from Colectie


/*Scrieti un SQL ce returneaza codurile colectiilor in care media valorii masinilor fabricate dupa anul 2000 e sub 25000*/
SELECT CodColectie
FROM Masina
WHERE AnFabricatie > 2000
GROUP BY CodColectie
HAVING AVG(ValoareEstimata) < 25000;

/*Scrieti un SQL ce returneaza modelul celei mai scumpe masini din colectiile cu categoria interbelica*/
SELECT TOP 1 M.Model
FROM Masina M
INNER JOIN Colectie C ON M.CodColectie = C.CodColectie
WHERE C.CategorieIstorica = 'interbelica'
ORDER BY M.ValoareEstimata DESC;


/*Creati un index pt o interogare.*/
CREATE INDEX idx_Masina_AnFabricatie_Valoare
ON Masina(AnFabricatie, ValoareEstimata)
INCLUDE(CodColectie);

DROP INDEX idx_Masina_AnFabricatie_Valoare ON Masina;

CREATE INDEX idx_Colectie_Categorie
ON Colectie(CategorieIstorica);

DROP INDEX idx_Colectie_Categorie ON Colectie;