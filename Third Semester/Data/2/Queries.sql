use VideoGamesStore
go

-- Toti manageri ce se ocupa de jocuri sau console
SELECT A.Nume AS NumeAngajat, D.NumeD AS Departament, Poz.Titlu AS Pozitie 
FROM Angajat A
INNER JOIN Departament D ON A.CodD = D.CodD 
INNER JOIN Pozitie Poz ON A.CodP = Poz.CodP
WHERE D.NumeD IN ('Jocuri Video','Console jocuri') AND Poz.Titlu LIKE 'Manager%'


-- Angajati ce lucreaza intr-o zi mai mult de 10 ore
SELECT A.Nume, P.Zi,DATEDIFF(HOUR, P.OraIncepere,P.OraSfarsit) AS DurataTura
FROM Angajat A 
INNER JOIN AngajatProgram AP ON A.CodA = AP.CodA 
INNER JOIN Program P ON AP.CodProg = P.CodProg
WHERE DATEDIFF(HOUR, P.OraIncepere,P.OraSfarsit)>10


-- Jocuri de tip shooterc cu pret mai mare de 30e si compania producatoare
SELECT J.Nume,J.DescriereJoc, J.GenJoc, C.Nume as NumeCompanie,C.Website, P.Pret
FROM JocVideo J
INNER JOIN Companie C ON C.CodComp = J.CodComp
INNER JOIN Produs P ON P.CodPr = J.CodJoc
WHERE P.Pret > 30 and J.GenJoc like '%shooter%'


-- Jocuri aparute dupa 2015 lansate de companiile Activision/Game Freak
SELECT P.NumePr, J.Nume,C.Nume,J.DescriereJoc,P.Pret,YEAR(J.DataLansare) AS AnLansare
FROM JocVideo J
INNER JOIN Companie C ON J.CodComp=C.CodComp
INNER JOIN Produs P ON J.CodJoc = P.CodPr
WHERE YEAR(J.DataLansare) > 2015 and C.Nume in ('Activision','Game Freak') 
ORDER BY AnLansare DESC


-- Cantitatea disponibila pentru fiecare produs din categoria accesorii cu pret mai mare de 10e
SELECT D.NumeD,Acc.NumeAcc,P.Cantitate,P.Pret
FROM Accesorii Acc
INNER JOIN Produs P ON P.CodPr=Acc.CodAcc
INNER JOIN Departament D ON D.CodD=P.CodD
WHERE P.Pret>=10
ORDER BY P.Cantitate DESC


-- Valoarea totala a stocului de console PS5/XBOS Series X, acolo unde depaseste 5000
SELECT D.NumeD,P.NumePr,P.Cantitate,SUM(P.Cantitate * P.Pret) AS Valoare,C.Nume
FROM Produs P
INNER JOIN Consola C ON C.CodConsola = P.CodPr
INNER JOIN Departament D ON P.CodD = D.CodD
WHERE P.NumePr like 'Consola%' and C.Nume in ('Playstation 5','XBOX Series X')
GROUP BY P.NumePr, P.Cantitate,C.Nume,D.NumeD
HAVING SUM(P.Cantitate * P.Pret) > 5000


-- Departamentele + produsele a caror cantitatea disponibila e mai mare de 20 
SELECT D.NumeD as Departament, COUNT(P.CodPr) as nr ,  P.Cantitate, J.Nume
from Produs p
INNER JOIN Departament D ON P.CodD = D.CodD
INNER JOIN JocVideo J ON P.CodPr = J.CodJoc
GROUP BY J.Nume, P.Cantitate,D.NumeD
HAVING P.Cantitate > 20


-- Totalul fiecarei achizitii din magazin
SELECT P.NumePr,Ac.DataAchizitie,Ac.cantitate AS CantitateAchizitionata,P.Pret AS PretPerBuc,C.Nume,sum(P.pret *Ac.cantitate) as PretTotal
FROM Produs P
INNER JOIN Achizitie Ac ON P.CodPr = Ac.CodPr
INNER JOIN Client C ON Ac.CodCl = C.CodCl
GROUP BY P.NumePr,Ac.DataAchizitie,Ac.cantitate,P.Pret,C.Nume


-- Toate consolele diferite de tip PS
SELECT DISTINCT P.NumePr AS TipProdus,P.Pret,C.Nume as Consola,C.Descriere,D.NumeD AS Departament
FROM Produs P
INNER join Consola C on C.CodConsola = P.CodPr
inner join Departament D ON D.CodD = P.CodD
WHERE C.Nume like 'PlayStation%'


-- Toate recenziile de la utilizatori diferiti cu nota >= 5 si numele produselor 
SELECT DISTINCT R.Nota,R.Explicatie,P.NumePr as Categorie,Cl.Nume
FROM Recenzie R
INNER JOIN Produs P on P.CodPr = R.CodPr
INNER JOIN Client Cl on Cl.CodCl = R.CodCl
WHERE R.Nota>=5


-- Cate produse au fost vandute din fiecare categorie
SELECT J.Nume as Produs,P.Pret,Ac.cantitate
FROM JocVideo J
INNER JOIN Produs P ON P.CodPr = J.CodJoc
INNER JOIN Achizitie Ac ON P.CodPr = Ac.CodPr
UNION
SELECT C.Nume as Produs,P.Pret,Ac.cantitate
FROM Consola C
INNER JOIN Produs P ON P.CodPr = C.CodConsola
INNER JOIN Achizitie Ac ON P.CodPr = Ac.CodPr
UNION
SELECT Acc.NumeAcc as Produs,P.Pret,Ac.cantitate
FROM Accesorii Acc
INNER JOIN Produs P ON P.CodPr = Acc.CodAcc
INNER JOIN Achizitie Ac ON P.CodPr = Ac.CodPr
ORDER BY Ac.cantitate DESC
