use VideoGamesStore
go

-- Departamente
INSERT INTO Departament (NumeD, NrAngajati) VALUES 
('Jocuri Video',15),
('Console jocuri',10),
('Accesorii',7);

-- Pozitii angajati
INSERT INTO Pozitie (Titlu, Atributii) VALUES 
('Manager','Coordonare echipa, supraveghere activitate'),
('Lucrator comercial','Vanzare, consultare clienti, recomandare produse');

-- Program de lucru
INSERT INTO Program (Zi, OraIncepere, OraSfarsit) VALUES 
('Luni','08 AM','08 PM'), --1
('Marti','08 AM','01 PM'), --2
('Marti','02 PM','08 PM'), -- 3
('Miercuri','08 AM','02 PM'), -- 4
('Joi','08 AM','08 PM'), -- 5
('Vineri','10 AM','02 PM'), -- 6
('Vineri','02 AM','08 PM'), -- 7
('Sambata','08 AM','06 PM'),--8
('Duminica','08 AM','08 PM'); --9

-- Detalii Angajati
INSERT INTO Angajat (Nume, PlataPeOra, CodP, CodD) VALUES 
('Gavril Nicolae',15,2,1),
('Cretu Amelia',20,2,3),
('Petrescu Ionut',11,2,2),
('Muresan David',50,1,1),
('Antonescu Irina',25,1,3),
('Lupescu Vlad',40,1,2),
('Voicu Irina',35,1,1);

-- AngajatProgram
INSERT INTO AngajatProgram (CodA, CodProg) 
VALUES 
(1,1), (1,7), (2,2), (2,9), (3,5), (3,6), (4,6), (5,3), (5,8), (6,4), (7,3), (7,5);

-- Produse
INSERT INTO Produs (CodPr, NumePr, Pret, Cantitate, CodD) VALUES 
(1,'Joc Video Adulti',60,50,1),
(2,'Joc Video Copii',30,100,1),
(3,'Consola jocuri',500,25,2),
(4,'Consola jocuri',700,15,2),
(5,'Controller',50,100,3),
(6,'Baterii',5,20,3),
(7,'Suport controller',10,500,3),
(8,'Joc Video Adulti',50,70,1),
(9,'Joc Video Adulti',100,60,1),
(10,'Joc Video Copii',50,10,1),
(11,'Consola',450,75,2),
(12,'Consola',300,35,2),
(13,'Consola jocuri',700,15,2),
(7,'Suport controller',10,500,3);

-- Clienti
INSERT INTO Client (Nume, Mail, NrTelefon) VALUES 
('Constantinescu Viorica','vio.constantinescu13@gmail.com','+40722963582'),
('Marcu George','george16@gmail.com','+40784694447'),
('Danciu Sandu','vio.constantinescu13@gmail.com','+40794568785');
INSERT INTO Client (Nume, NrTelefon) VALUES ('Ichim Diana','+40735645185');
INSERT INTO Client (Nume, Mail, NrTelefon) VALUES 
('Danciu Sandu','vio.constantinescu13@gmail.com','+40794568785'),
('Danciu Sandu','vio.constantinescu13@gmail.com','+40794568785');

-- Achizitii
INSERT INTO Achizitie (DataAchizitie, MetodaPlata, cantitate, CodCl, CodPr) VALUES 
('2024-01-15','card',1,1,1),
('2024-02-09','cash',3,2,5),
('2023-10-15','card',2,3,7),
('2023-07-26','card',1,1,3),
('2023-09-18','cash',7,2,6),
('2024-03-19','cash',6,4,4);

-- Recenzii
INSERT INTO Recenzie (Nota, Explicatie, CodPr, CodCl) VALUES
(10,'Ruleaza excelent la grafice inalte',1,1),
(10,'Ruleaza excelent la grafice inalte',1,3),
(10,'Ruleaza excelent la grafice inalte',1,6),
(5,'Se putea calitatea mai inalta',5,2),
(7,'Destul de zgomotoasa in timpul gameplay-ului',3,1),
(1,'S-a stricat la putin timp de la achizitionare',7,3);

-- Accesorii
INSERT INTO Accesorii (CodAcc, NumeAcc, Compatibilitate) VALUES
(6,'Baterii DuraCell', 'Controller console');
INSERT INTO Accesorii (CodAcc, NumeAcc, Descriere, Compatibilitate) VALUES
(5,'Controller PS','Versiune imbunatatita, miscare mai rapida','PlayStation'),
(7,'Suport controller','Suport pentru depozitarea controller-ului cand nu e folosit. Poate fi prins sub birou.','Controller XBOX'),
(14,'Suport controller','Suport pentru depozitarea controller-ului cand nu e folosit. Poate fi prins sub birou.','Controller XBOX');

-- Console
INSERT INTO Consola (CodConsola, Nume, Producator, Capacitate, DataAparitie, Descriere) VALUES
(3,'PlayStation 4','Sony','500','2013-11-15','Performante grafice avansate, rezolutie video inalta.'),
(4,'PlayStation 5','Sony','825','2020-11-12','Hardware puternic, SSD ultra rapid, rezolutie 4k, ray-tracing, pana la 120 fps'),
(11,'XBOX Series X','Microsoft','802','2020-11-10','Grafica 4k, pana la 120 fps'),
(12,'Nintendo Switch','Nintendo','64','2017-03-03','Tableta ce poate fi folosita si portabil, transformabila in consola'),
(13,'PlayStation 5','Sony','825','2020-11-12','Hardware puternic, SSD ultra rapid, rezolutie 4k, ray-tracing, pana la 120 fps'),;

-- Companii
INSERT INTO Companie (Nume, Website, StudioPrincipal,AnInfiintare) VALUES
('Rockstar Games','www.rockstargames.com','Santa Monica','1998'),
('Mojang Studios','www.minecraft.net','Stockholm','2009'),
('Activision','www.activision.com','Santa Monica','1979'),
('Game Freak','www.gamefreak.co.jp','Tokyo','1989');

-- Jocuri Video
INSERT INTO JocVideo(CodJoc, Nume, DescriereJoc, DataLansare, TipJoc, GenJoc, Platforma, CodComp) VALUES
(1,'Grand Theft Auto V','Acțiunea se desfășoară în statul fictiv San Andreas, urmarind viata a 3 protagonisti.','2013-09-17','singleplayer / multiplayer','actiune, aventura, shooter','Windows, PS, XBOX',1),
(2,'Minecraft','Joc de tip sandbox ce da frau liber imaginatiei','2009-05-17','singleplayer / multiplayer','survival, sandbox','Windows',2),
(9,'Call of Duty: Modern Warfare III','Recreeaza scene de razboi atat in timpul povestii, cat si in dueluri alaturi de alti jucatori','2023-11-09','singleplayer / multiplayer','shooter','Windows, PS, XBOX',3),
(10,'Pokemon','Captureaza si antreneaza Pokemoni pentru a deveni mai bun','2019-11-15','singleplayer','role-playing','Nintendo',4);

SELECT * FROM Departament
SELECT * FROM Pozitie
SELECT * FROM Program
SELECT * FROM Angajat
SELECT * FROM AngajatProgram
SELECT * FROM Produs
SELECT * FROM Client
SELECT * FROM Achizitie
SELECT * FROM Recenzie
SELECT * FROM Accesorii
SELECT * FROM Consola
SELECT * FROM Companie
SELECT * FROM JocVideo