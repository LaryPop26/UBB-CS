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