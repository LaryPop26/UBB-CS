create database GestiuneVanzari
go

use GestiuneVanzari;
go

create table Clienti(
	IdCl int primary key identity,
	Denumire varchar(50),
	CodFiscal varchar(50)
	);

create table AgentiVanzare(
	IdAgent int primary key identity,
	Nume varchar(50),
	Prenume varchar(50)
	);

create table Produse(
	IdProdus int primary key identity,
	Denumire varchar(50),
	UM varchar(50)
	);

create table Facturi(
	IdFactura int primary key identity,
	Numar int,
	DataEmitere date,
	IdClient int foreign key references Clienti(IdCl),
	IdAgent int foreign key references AgentiVanzare(IdAgent)
	);

create table FacturiProduse(
	IdProdus int foreign key references Produse(IdProdus),
	IdFactura int foreign key references Facturi(IdFactura),
	constraint pk_FacturiProduse primary key (IdProdus,IdFactura),
	NrOrdine int,
	Pret int,
	Cantitate int
	);

create procedure Schimbare
	@IdFactura int,
	@IdProdus int,
	@NrOrdine int,
	@Pret int,
	@Cantitate int
as
begin 
	declare @Valoare as int 
	set @Valoare = 0
	if exists(select 1 from FacturiProduse
			  where IdProdus = @IdProdus AND IdFactura = @IdFactura)
		begin
			update FacturiProduse
			set @Valoare = -@Cantitate
		end
	else
		begin 
			set @Valoare = @Cantitate
		end
	insert into FacturiProduse(IdProdus, IdFactura, NrOrdine, Pret, Cantitate)
	values (@IdProdus, @IdFactura, @NrOrdine, @Pret, @Valoare)
end


-- Insert into Clienti
INSERT INTO Clienti (Denumire, CodFiscal) VALUES 
('SC Alpha SRL', 'RO123456'),
('SC Beta SRL', 'RO654321'),
('SC Gamma SRL', 'RO987654');

-- Insert into AgentiVanzare
INSERT INTO AgentiVanzare (Nume, Prenume) VALUES 
('Popescu', 'Ion'),
('Ionescu', 'Maria'),
('Georgescu', 'Adrian');

-- Insert into Produse
INSERT INTO Produse (Denumire, UM) VALUES 
('Laptop', 'Buc'),
('Telefon', 'Buc'),
('Imprimanta', 'Buc');

-- Insert into Facturi
INSERT INTO Facturi (Numar, DataEmitere, IdClient, IdAgent) VALUES 
(1001, '2025-01-01', 1, 1),
(1002, '2025-01-02', 2, 2),
(1003, '2025-01-03', 3, 3);

-- Insert into FacturiProduse
INSERT INTO FacturiProduse (IdProdus, IdFactura, NrOrdine, Pret, Cantitate) VALUES 
(1, 1, 1, 4500, 2), -- 2 Laptops for Factura 1001
(2, 1, 2, 1500, 3), -- 3 Phones for Factura 1001
(3, 2, 1, 1200, 1), -- 1 Printer for Factura 1002
(1, 3, 1, 4500, 1), -- 1 Laptop for Factura 1003
(2, 3, 2, 1500, 2); -- 2 Phones for Factura 1003

select * from FacturiProduse

EXEC Schimbare 
    @IdFactura = 1,
    @IdProdus = 2,
    @NrOrdine = 3,
    @Pret = 2000,
    @Cantitate = 5;