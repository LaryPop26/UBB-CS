CREATE DATABASE OSER;
GO

USE OSER;
GO

CREATE TABLE Hala(
	IdHala int primary key identity,
	Litera char,
	Suprafata int);

CREATE TABLE Tarabe(
	IdTaraba int primary key identity,
	Suprafata int,
	Numar int,
	IdHala int foreign key references Hala(IdHala));

CREATE TABLE CategorieProduse(
	IdCategorie int primary key identity,
	Nume varchar(50));

CREATE TABLE TarabeCategorie(
	IdTaraba int foreign key references Tarabe(IdTaraba),
	IdCategorie int foreign key references CategorieProduse(IdCategorie),
	constraint pk_TarabeCategorie primary key(IdTaraba,IdCategorie));

create table Produs(
	IdProdus int primary key identity,
	Denumire varchar(50),
	Pret int,
	IdCategorie int foreign key references CategorieProduse(IdCategorie));

insert into Hala(Litera,Suprafata) values
('A',100),('F',65),('X',90),('B',50);

insert into Tarabe(Suprafata, Numar, IdHala) values
(5,1,1),(6,2,1),(9,1,2),(10,1,3),(5,1,4)

insert into CategorieProduse (Nume) VALUES
('haine'),('vesela'),('electrocasnice'),('jucarii');

INSERT INTO Produs (Denumire, Pret, IdCategorie) VALUES
    ('Tricou', 90.0, 1),   
    ('Farfurie', 120.0, 2), 
    ('Frigider', 250.0, 3), 
    ('Papusa', 80.0, 4),    
    ('Blender', 150.0, 3),  
    ('Pahar', 70.0, 2);   

INSERT INTO TarabeCategorie (IdTaraba, IdCategorie)
VALUES
    (1, 1), -- Taraba 1 din Hala A vinde haine
    (1, 2), -- Taraba 1 din Hala A vinde vesela
    (2, 3), -- Taraba 2 din Hala A vinde electrocasnice
    (3, 4), -- Taraba 1 din Hala F vinde jucarii
    (4, 2), -- Taraba 1 din Hala X vinde vesela
    (5, 1); -- Taraba 1 din Hala B vinde haine

select * from Hala
select * from Tarabe
select * from TarabeCategorie
select * from CategorieProduse
select * from Produs

create procedure ActualizarePret @IdTaraba int
as
begin 
	update Produs
	set Pret = Pret + 10
	where IdProdus in (select P.IdProdus 
					   from Produs P
					   join TarabeCategorie TC on P.IdCategorie = TC.IdCategorie
					   where TC.IdTaraba = @IdTaraba AND Pret<100);
	
	update Produs
	set Pret = Pret + 50
	where IdProdus in (select P.IdProdus 
					   from Produs P
					   join TarabeCategorie TC on P.IdCategorie = TC.IdCategorie
					   where TC.IdTaraba = @IdTaraba AND Pret>200);

	update Produs
	set Pret = Pret * 1.1
	where IdProdus in (select P.IdProdus 
					   from Produs P
					   join TarabeCategorie TC on P.IdCategorie = TC.IdCategorie
					   where TC.IdTaraba = @IdTaraba AND Pret between 100 and 200);

end

exec ActualizarePret 1;

select * from Produs

exec ActualizarePret 2;

SELECT P.IdProdus, P.Denumire, P.Pret, TC.IdTaraba
FROM Produs P
JOIN TarabeCategorie TC ON P.IdCategorie = TC.IdCategorie
WHERE TC.IdTaraba = 2;

create view Reducere as
select P.Denumire, P.Pret, P.Pret*0.40 as PretRedus
from Produs P
inner join CategorieProduse C on P.IdCategorie = C.IdCategorie
inner join TarabeCategorie TC on C.IdCategorie = TC.IdCategorie
inner join Tarabe T on TC.IdTaraba = T.IdTaraba
inner join Hala H on T.IdHala = H.IdHala
where C.Nume in ('haine','vesela') and H.Litera in ('A','F','X');

select * from Reducere