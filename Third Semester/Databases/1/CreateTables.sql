Create database VideoGamesStore
go
use VideoGamesStore
go

CREATE TABLE Departament
(CodD INT PRIMARY KEY IDENTITY,
NumeD VARCHAR(100) NOT NULL,
NrAngajati INT
);

CREATE TABLE Pozitie
(CodP INT PRIMARY KEY IDENTITY,
Titlu VARCHAR(100) NOT NULL,
Atributii VARCHAR(500)
);

CREATE TABLE Program
(CodProg INT PRIMARY KEY IDENTITY,
Zi VARCHAR(10),
OraIncepere TIME,
OraSfarsit TIME
);

CREATE TABLE Angajat
(CodA INT PRIMARY KEY IDENTITY,
Nume VARCHAR(100) NOT NULL,
PlataPeOra INT,
CodP INT FOREIGN KEY REFERENCES Pozitie(CodP),
CodD INT FOREIGN KEY REFERENCES Departament(CodD)
);

CREATE TABLE AngajatProgram
(CodA INT FOREIGN KEY REFERENCES Angajat(CodA),
CodProg INT FOREIGN KEY REFERENCES Program(CodProg)
CONSTRAINT pk_AngajatProgram PRIMARY KEY (CodA, CodProg)
);

CREATE TABLE Produs
(CodPr INT PRIMARY KEY,
NumePr VARCHAR(100) NOT NULL,
Pret INT NOT NULL,
Cantitate INT,
CodD INT FOREIGN KEY REFERENCES Departament(CodD)
);

CREATE TABLE Client
(CodCl INT PRIMARY KEY IDENTITY,
Nume VARCHAR(100) NOT NULL,
Mail VARCHAR(100),
NrTelefon VARCHAR(15)
);

CREATE TABLE Achizitie
(DataAchizitie DATE,
MetodaPlata VARCHAR(20),
cantitate INT,
CodPr INT FOREIGN KEY REFERENCES Produs(CodPr),
CodCl INT FOREIGN KEY REFERENCES Client(CodCl)
CONSTRAINT pk_Achizitie PRIMARY KEY (CodPr, CodCl)
);

CREATE TABLE Recenzie
(Nota INT CHECK (Nota>=1 and Nota<=10),
Explicatie VARCHAR(1000),
CodPr INT FOREIGN KEY REFERENCES Produs(CodPr),
CodCl INT FOREIGN KEY REFERENCES Client(CodCl),
CONSTRAINT pk_Recenzie PRIMARY KEY (CodPr, CodCl)
);

CREATE TABLE Accesorii
(CodAcc INT FOREIGN KEY REFERENCES Produs(CodPr),
NumeAcc VARCHAR(100) NOT NULL,
Descriere VARCHAR(1000),
Compatibilitate VARCHAR(500),
CONSTRAINT pk_Accesorii PRIMARY KEY (CodAcc)
);

CREATE TABLE Consola
(CodConsola INT FOREIGN KEY REFERENCES Produs(CodPr),
Nume VARCHAR(100) NOT NULL,
Producator VARCHAR(100) NOT NULL,
Capacitate INT,
DataAparitie DATE,
Descriere VARCHAR(1000),
CONSTRAINT pk_Consola PRIMARY KEY (CodConsola)
);

CREATE TABLE Companie
(CodComp INT PRIMARY KEY IDENTITY,
Nume VARCHAR(100) NOT NULL UNIQUE,
Website VARCHAR(100),
StudioPrincipal VARCHAR(100),
AnInfiintare INT
);

CREATE TABLE JocVideo
(CodJoc INT FOREIGN KEY REFERENCES Produs(CodPr),
Nume VARCHAR(100) NOT NULL UNIQUE,
DescriereJoc VARCHAR(1000),
DataLansare DATE,
TipJoc VARCHAR(50),
GenJoc VARCHAR(1000),
Platforma VARCHAR(200),
CodComp INT FOREIGN KEY REFERENCES Companie(CodComp),
CONSTRAINT pk_JocVideo PRIMARY KEY (CodJoc)
);