create database Restaurante
go

use Restaurante
go

create table TipuriRestaurante(
	IdTip int primary key identity,
	Nume nvarchar(50) not null,
	Descriere nvarchar(100)
	);

create table Orase(
	IdOras int primary key identity,
	Nume nvarchar(50) not null
	);

create table Restaurante(
	IdRestaurant int primary key identity,
	Nume nvarchar(50) not null,
	Adresa nvarchar(100),
	NumarTelefon nvarchar(15),
	IdTip int foreign key references TipuriRestaurante(IdTip),
	IdOras int foreign key references Orase(IdOras)
	);

create table Utilizatori(
	IdUtilizator int primary key identity,
	Nume nvarchar(50) not null,
	AdresaMail nvarchar(100) not null unique,
	Parola nvarchar(50) not null
	);

create table Note(
	IdRestaurant int foreign key references Restaurante(IdRestaurant),
	IdUtilizator int foreign key references Utilizatori(IdUtilizator),
	constraint pk_Note primary key (IdRestaurant, IdUtilizator),
	Nota float check (Nota>=0 and Nota<=10)
	);

create or alter procedure Ranking
	@IdRestaurant int,
	@IdUtilizator int,
	@Nota float
as
begin 
	if exists(select 1 from Note
			  where Note.IdRestaurant = @IdRestaurant and Note.IdUtilizator = @IdUtilizator)
		begin 
			update Note
			set Nota = @Nota
			where Note.IdRestaurant = @IdRestaurant and Note.IdUtilizator = @IdUtilizator
		end
	else
	begin
		insert into Note(IdRestaurant,IdUtilizator,Nota) 
		values (@IdRestaurant, @IdUtilizator, @Nota)
	end
end

create or alter function Informatii
(
	@Mail nvarchar(100)
)
returns table
as
return
(
	select Tr.Nume as Tip, R.Nume as Restaurant, R.NumarTelefon,O.Nume as Oras,N.Nota,U.Nume,U.AdresaMail
	from Utilizatori U
	inner join Note N on U.IdUtilizator = N.IdUtilizator
	inner join Restaurante R on N.IdRestaurant = R.IdRestaurant
	inner join Orase O on R.IdOras = O.IdOras
	inner join TipuriRestaurante Tr on R.IdTip = Tr.IdTip
	where U.AdresaMail = @Mail
	);