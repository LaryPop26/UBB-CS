use VideoGamesStore
go

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

