use VideoGamesStore

create table log_table
(
	id INT PRIMARY KEY IDENTITY,
	TypeOperation VARCHAR(50),
	TableOperation VARCHAR(50),
	ExecutionDate DATETIME
)

create function validate_produs(@NumePr varchar(100),@Pret int,@Cantitate int, @CodD int)
returns varchar(200)
as
begin
	declare @err varchar(200)
	set @err = ''

	if (@NumePr = '')
		set @err = @err + 'NumePr cannot be empty.'

	if (@Pret <= 0)
		set @err = @err + 'Pret must be a positive number.'
		
	if (@Cantitate <= 0)
		set @err = @err + 'Pret must be a positive number.'

	if (not(exists(select * from Departament where CodD = @CodD)))
		set @err = @err + 'CodD does not exist.'

	return @err
end
go


create function validate_client(@Nume varchar(100),@Mail varchar(100),@NrTelefon varchar(15))
returns varchar(200)
as
begin
	declare @err varchar(200)
	set @err = ''

	if (@Nume = '')
		set @err = @err + 'Nume cannot be empty.'

	if (@Mail = '')
		set @err = @err + 'Mail cannot be empty.'

	if (@NrTelefon = '')
		set @err = @err + 'NrTelefon cannot be empty.'

	return @err
end
go


create function validate_achizitie(@DataAchizitie date,@MetodaPlata varchar(20),@cantitateA int,@CodPr int, @CodCl int)
returns varchar(200)
as
begin
	declare @err varchar(200)
	set @err = ''

	if (@DataAchizitie is null)
		set @err = @err + 'DataAchizitie has a wrong format.'

	if (@MetodaPlata = '')
		set @err = @err + 'MetodaPlata cannot be empty.'

	if (@cantitateA <= 0)
		set @err = @err + 'cantitate must be a positive number.'

	if (exists(select * from Achizitie where CodCl = @CodCl and CodPr = @CodPr))
		set @err = @err + 'Achizitie already exists.'


	return @err
end
go

create procedure insert_into_tables(
	@NumePr varchar(100),@Pret int,@Cantitate int, @CodD int,
	@Nume varchar(100),@Mail varchar(100),@NrTelefon varchar(15),
	@DataAchizitie date,@MetodaPlata varchar(20),@cantitateA int)
as 
begin
	BEGIN TRAN
	BEGIN TRY
		declare @error varchar(200)
		set @error = dbo.validate_produs(@NumePr,@Pret,@Cantitate, @CodD)

		if (@error <> '')
		begin 
			RAISERROR(@error,14,1)
		end
		
		declare @NewCodPr int
		select @NewCodPr = ISNULL(max(CodPr),0) + 1 from Produs

		insert into Produs values (@NewCodPr,@NumePr, @Pret, @Cantitate, @CodD)
		insert into log_table values ('insert','Produs', CURRENT_TIMESTAMP)

		set @error = dbo.validate_client(@Nume, @Mail, @NrTelefon)
		if (@error <> '')
		begin 
			RAISERROR(@error,14,1)
		end

		insert into Client values (@Nume, @Mail, @NrTelefon)
		insert into log_table values ('insert','Client', CURRENT_TIMESTAMP)

		declare @CodPr int, @CodCl int
		set @CodPr = (select MAX(@CodPr) from Produs)
		insert into log_table values('select','Produs', CURRENT_TIMESTAMP)

		set @CodCl = (select MAX(@CodCl) from Client)
		insert into log_table values('select','Client', CURRENT_TIMESTAMP)

		set @error = dbo.validate_achizitie(@DataAchizitie, @MetodaPlata, @cantitateA, @CodPr, @CodCl)
		if (@error <> '')
		begin 
			RAISERROR(@error,14,1)
		end
		insert into Achizitie values (@DataAchizitie, @MetodaPlata, @cantitateA, @CodPr, @CodCl)
		insert into log_table values ('insert','Achizitie', CURRENT_TIMESTAMP)

	COMMIT TRAN
	print 'Transaction commited'

	END TRY
	BEGIN CATCH
		print ERROR_MESSAGE()
		ROLLBACK TRAN
		print 'Transaction rollbacked'
	END CATCH
END
GO 
-- drop procedure dbo.insert_into_tables
select * from log_table
select * from Produs
select * from Client
select * from Achizitie

-- error

exec insert_into_tables '',55,60,1,'Popescu Adela','adela@gmail.com','+40756894562','2025-01-15','card',1
exec insert_into_tables 'JoyStick',10,-5,2,'Surdu Daniela','adela@gmail.com','+40756894562','2025-01-15','card',1


--  SUCCES (totul se inserează)
exec insert_into_tables 'Joc Video',55,60,1,'Popescu Adela','adela@gmail.com','+40756894562','2025-01-15','card',1
EXEC insert_into_tables 'Jocuri Copii', 300, 50, 1, 'Ionescu Vlad', 'vlad@gmail.com', '0712345678', '2025-05-01', 'card', 1;

-- Eroare – produs invalid (@NumePr gol) => rollback complet
EXEC insert_into_tables '', 300, 50, 1, 'Ionescu Vlad', 'vlad@gmail.com', '+40712345678', '2025-05-01', 'card', 1;

-- Eroare – client invalid (@Mail gol) => rollback complet
EXEC insert_into_tables 'Joc', 200, 20, 1, 'Maria Pop', '', '+40700000000', '2025-05-01', 'cash', 2;

-- Eroare – achiziție duplicat (presupune rulare anterioară de succes) => rollback complet
EXEC insert_into_tables 'Jocuri Copii', 300, 50, 1, 'Ionescu Vlad', 'vlad@gmail.com', '+40712345678', '2025-05-01', 'card', 1;


create procedure insert_into_tables_v2(
	@NumePr varchar(100),@Pret int,@Cantitate int, @CodD int,
	@Nume varchar(100),@Mail varchar(100),@NrTelefon varchar(15),
	@DataAchizitie date,@MetodaPlata varchar(20),@cantitateA int)
as 
begin
	declare @err bit
	set @err = 0

	BEGIN TRAN
	BEGIN TRY
		declare @error varchar(200)
		set @error = dbo.validate_produs(@NumePr,@Pret,@Cantitate, @CodD)

		if (@error <> '')
		begin 
			RAISERROR(@error,14,1)
		end
		
		declare @NewCodPr int
		select @NewCodPr = ISNULL(max(CodPr),0) + 1 from Produs

		insert into Produs values (@NewCodPr,@NumePr, @Pret, @Cantitate, @CodD)
		insert into log_table values ('insert','Produs', CURRENT_TIMESTAMP)

		COMMIT TRAN
		print 'Transaction commited'
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
		insert into log_table values ('insert error','Produs', CURRENT_TIMESTAMP)
		print 'Transaction rollbacked'
		set @err = 1
	END CATCH

	BEGIN TRAN
	BEGIN TRY
		set @error = dbo.validate_client(@Nume, @Mail, @NrTelefon)
		if (@error <> '')
		begin 
			RAISERROR(@error,14,1)
		end

		insert into Client values (@Nume, @Mail, @NrTelefon)
		insert into log_table values ('insert','Client', CURRENT_TIMESTAMP)

	COMMIT TRAN
		print 'Transaction commited'
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
		insert into log_table values ('insert error','Client', CURRENT_TIMESTAMP)
		print 'Transaction rollbacked'
		set @err = 1
	END CATCH

	if @err = 1 return

	BEGIN TRAN
	BEGIN TRY

		declare @CodPr int, @CodCl int
		set @CodPr = (select MAX(@CodPr) from Produs)
		insert into log_table values('select','Produs', CURRENT_TIMESTAMP)

		set @CodCl = (select MAX(@CodCl) from Client)
		insert into log_table values('select','Client', CURRENT_TIMESTAMP)
		
		set @error = dbo.validate_achizitie(@DataAchizitie, @MetodaPlata, @cantitateA, @CodPr, @CodCl)
		if (@error <> '')
		begin 
			RAISERROR(@error,14,1)
		end
		insert into Achizitie values (@DataAchizitie, @MetodaPlata, @cantitateA, @CodPr, @CodCl)
		insert into log_table values ('insert','Achizitie', CURRENT_TIMESTAMP)

		COMMIT TRAN
		print 'Transaction commited'
	 
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
		insert into log_table values ('insert error','Achizitie', CURRENT_TIMESTAMP)
		print 'Transaction rollbacked'
	END CATCH
END
GO 

select * from log_table
select * from Produs
select * from Client
select * from Achizitie

-- chat gpt

-- SUCCES (toate cele 3 tranzacții reușesc)
EXEC insert_into_tables_v2 'Joc Video', 120, 15, 1, 'Dobre Ana', 'ana.dobre@yahoo.com', '+40722334455', '2025-05-02', 'cash', 1;

-- EroareC – produs invalid (@Pret <= 0)
EXEC insert_into_tables_v2 'Jocuri Copii', 0, 10, 1, 'Popa Andrei', 'andrei.popa@mail.com', '+40711122233', '2025-05-03', 'card', 1;

-- Eroare – client invalid (@NrTelefon gol)
EXEC insert_into_tables_v2 'Jocuri Copii', 200, 5, 1, 'Ioana Petrescu', 'ioana@mail.com', '', '2025-05-03', 'card', 1;

-- Eroare – achiziție duplicat
EXEC insert_into_tables_v2 'Joc Video', 120, 15, 1, 'Dobre Ana', 'ana.dobre@yahoo.com', '+40722334455', '2025-05-02', 'cash', 1;