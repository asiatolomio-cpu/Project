Use ScuolaDb;
--ESERCIZIO QUIZ: Crea un Database con Tables e Records
CREATE database AziendaDB;
use AziendaDB;

create table Reparti (
    RepartoID INT NOT NULL Primary key Identity (1,1),
    NomeReparto NVARCHAR(100) not null,
    SedeReparto NVARCHAR(100) NULL
);

Create table Progetti (
    ProgettoID INT NOT NULL Primary key identity (1,1),
    Nome NVARCHAR (100) not null,
    Budget DECIMAL (10,2),
    DataInizio DATE,
    DataFine DATE
);

/*inserisco “foreign key” per introdurre fra parentesi il nome della colonna 
che le 2 tabelle hanno in comune, (quella in creazione e quella già creata in precedenza); 
subito devo specificare il nome della seconda tabella, uso “reference” e tra parentesi di nuovo
il nome della colonna che accomuna le tabelle*/
CREATE TABLE Dipendenti(
    DipendenteID INT NOT NULL Primary key Identity (1,1),
    Nome NVARCHAR (100) NOT NULL,
    Cognome NVARCHAR (100) NOT NULL,
    Email NVARCHAR (100) UNIQUE NULL,
    Stipendio DECIMAL (10,2),
    DataAssunzione DATE,
    RepartoID INT,
    FOREIGN KEY (RepartoID) REFERENCES Reparti(RepartoID)
);

/*se voglio usare come PRIMARY KEY il nome di una colonna già esistente (e che poi sarà l'elemento in comune di 2 o più tabelle), 
allora lo devo specificare subito prima della definizione della FOREIGN KEY, senza dimenticarmi di 
scriverlo come se fosse una colonna ex novo senza però inserire il dettaglio della primary key*/
/*foreign e primary keys servono per collegare fra loro più tabelle*/

/*Progetti ha ProgettoID come primary key
Dipendenti ha DipendenteID come primary key
Assegnazioni ha 2 primary keys: DipendenteID e ProgettoID*/
CREATE TABLE Assegnazioni(
  DipendenteID INT,
  ProgettoID INT,
  Ruolo NVARCHAR (50),
  PRIMARY KEY (DipendenteID, ProgettoID),
  FOREIGN KEY (DipendenteID) REFERENCES Dipendenti(DipendenteID),
  FOREIGN KEY (ProgettoID) REFERENCES Progetti(ProgettoID)
);

SELECT *
FROM Reparti;
SELECT *
FROM Progetti;
SELECT *
FROM Dipendenti;
SELECT *
FROM Assegnazioni;

INSERT INTO Reparti 
(NomeReparto, SedeReparto)
VALUES  
('IT','USA'),
('HR','Roma'),
('Finance','Milano'),
('Operation','Venezia'),
('Marketing','Bologna'),
('Sales','Torino'),
('Support','Napoli'),
('HQ','Oslo'),
('Research','Londra'),
('Customer','Bankok'),
('','Bari'),
('Management','');

SELECT *
FROM Reparti
Where RepartoID in (1,2,5);

INSERT INTO Dipendenti 
(Nome, Cognome, Email, RepartoId)
VALUES  
('Mario','Rossi','mario.rossi@email.com', 1),
('Luca','Bianchi','luca.bianchi@email.com', 2),
('Giulia','Neri','giulia.neri@email.com', 3),
('Francesca','Verdi','francesca.verdi@email.com', 4),
('Marco','Rossi','marco.rossi@email.com', 5),
('Laura','Bianchi','laura.bianchi@email.com', 6),
('Andrea','Neri','andrea.neri@email.com', 7),
('Simona','Verdi','simona.verdi@email.com', 8),
(' Stefano','Rossi','stefano.rossi@email.com', 9),
('Elena','Bianchi','elena.bianchi@email.com', 10),
('Davide','Neri','davide.neri@email.com', 11),
('Sara','Verdi','sara.verdi@email.com', 12);

select* 
from Dipendenti 
where Nome like '%e%';

CREATE TABLE Clienti (
    ClientiID INT PRIMARY KEY IDENTITY (1,1),
    Nome NVARCHAR(100) NOT NULL,
    Telefono NVARCHAR (50) NOT NULL,
    Email NVARCHAR(50) UNIQUE 
);

CREATE TABLE Ordini (
    OrdineID INT NOT NULL PRIMARY KEY IDENTITY (1,1),
    ClienteID INT,
    DataOrdine DATE,
    Totale DECIMAL (10,2),
    FOREIGN KEY (ClienteID) REFERENCES Clienti(ClientiID)
);

CREATE TABLE DettagliOrdine (
    DettaglioID INT PRIMARY KEY IDENTITY (1,1),
    OrdineID INT,
    Prodotto NVARCHAR (50) NOT NULL,
    Quantita INT,
    PrezzoUnitario DECIMAL (10,2),
    FOREIGN KEY (OrdineID) REFERENCES Ordini(OrdineID)
);


INSERT INTO Reparti (NomeReparto, SedeReparto) 
VALUES
('IT','Roma'),
('HR','Milano'),
('Vendite','Napoli'),
('Marketing','Torino'),
('Finanza','Bologna'),
('Logistica','Genova'),
('Supporto','Firenze'),('Produzione','Bari'),('Ricerca','Parma'),('Qualità','Verona'),
('Sicurezza','Trieste'),('Acquisti','Padova'),('Legale','Modena'),('Formazione','Perugia'),('Controllo','Pisa'),
('Innovazione','Catania'),('Sviluppo','Palermo'),('Design','Venezia'),('Testing','Lecce'),('HelpDesk','Salerno'),
('Cloud','Aosta'),('AI','Trento'),('Data','Bolzano'),('Networking','Ancona'),('Mobile','Taranto'),
('Web','Rimini'),('Backend','Ferrara'),('Frontend','Siena'),('DevOps','Lucca'),('QA','Udine');


INSERT INTO Reparti
	(NomeReparto, SedeReparto)
		VALUES
		('IT','Roma'),
		('USA','Washington'),
		('UK','Londra'),
		('IT','Palermo'),
		('Ufficio Raccomandazioni','Milano'),
		('Reparto Licenziamenti','Roma');


INSERT INTO Reparti(NomeReparto, SedeReparto)
VALUES 
	('Communication', 'Milano'),
	('IT', 'Roma'),
	('Technologist','Florida'),
	('Human Resources', 'Roma'),
	('Vendite', 'Napoli'),
	('Engineering', 'Milano'),
	('Manager', 'Roma'),
	('Food Technologist','Napoli'),
	('CEO', 'Roma'),
	('Legal', 'Napoli'),
	('Accountant', 'Napoli');


INSERT INTO Reparti 
    (NomeReparto, SedeReparto) 
VALUES
    ('IT','Roma'),
    ('HR','Milano'),
    ('Vendite','Napoli'),
    ('Marketing','Torino'),
    ('Finanza','Bologna'),
    ('Logistica','Genova'),
    ('Supporto','Firenze'),
    ('Produzione','Bari'),
    ('Ricerca','Parma'),
    ('Qualità','Verona'),
    ('Sicurezza','Trieste'),
    ('Acquisti','Padova'),
    ('Legale','Modena'),
    ('Formazione','Perugia'),
    ('Controllo','Pisa'),
    ('Innovazione','Catania'),
    ('Sviluppo','Palermo'),
    ('Design','Venezia'),
    ('Testing','Lecce'),
    ('HelpDesk','Salerno'),
    ('Cloud','Aosta'),
    ('AI','Trento'),
    ('Data','Bolzano'),
    ('Networking','Ancona'),
    ('Mobile','Taranto'),
    ('Web','Rimini'),
    ('Backend','Ferrara'),
    ('Frontend','Siena'),
    ('DevOps','Lucca'),
    ('QA','Udine'),
    ('IT','USA'),
    ('HR','Roma'),
    ('Finance','Milano'),
    ('Operation','Venezia'),
    ('Marketing','Bologna'),
    ('Sales','Torino'),
    ('Support','Napoli'),
    ('HQ','Oslo'),
    ('Research','Londra'),
    ('Customer','Bankok'),
    ('','Bari'),
    ('Management',''),
    ('Communication', 'Milano'),
	('IT', 'Roma'),
	('Technologist','Florida'),
	('Human Resources', 'Roma'),
	('Vendite', 'Napoli'),
	('Engineering', 'Milano'),
	('Manager', 'Roma'),
	('Food Technologist','Napoli'),
	('CEO', 'Roma'),
	('Legal', 'Napoli'),
	('Accountant', 'Napoli');


INSERT INTO Dipendenti (Nome, Cognome, Email, Stipendio, RepartoID, DataAssunzione) 
VALUES
('Mario','Rossi','m1@mail.com',2500,1,'2022-01-01'),
('Luigi','Verdi','m2@mail.com',2300,2,'2022-01-02'),
('Anna','Bianchi','m3@mail.com',2700,3,'2022-01-03'),
('Paolo','Neri','m4@mail.com',2100,4,'2022-01-04'),
('Sara','Gialli','m5@mail.com',3000,5,'2022-01-05'),
('Luca','Blu','m6@mail.com',2400,6,'2022-01-06'),
('Elena','Rosa','m7@mail.com',2600,7,'2022-01-07'),
('Marco','Viola','m8@mail.com',2800,8,'2022-01-08'),
('Giulia','Grigi','m9@mail.com',2300,9,'2022-01-09'),
('Davide','Marrone','m10@mail.com',2900,10,'2022-01-10'),
('Alessio','Nero','m11@mail.com',2500,11,'2022-01-11'),
('Franco','Bianco','m12@mail.com',2600,12,'2022-01-12'),
('Chiara','Blu','m13@mail.com',2700,13,'2022-01-13'),
('Andrea','Rossi','m14@mail.com',2200,14,'2022-01-14'),
('Simone','Verdi','m15@mail.com',2100,15,'2022-01-15'),
('Irene','Bianchi','m16@mail.com',2800,16,'2022-01-16'),
('Fabio','Neri','m17@mail.com',3000,17,'2022-01-17'),
('Laura','Gialli','m18@mail.com',2400,18,'2022-01-18'),
('Matteo','Blu','m19@mail.com',2500,19,'2022-01-19'),
('Stefano','Rosa','m20@mail.com',2600,20,'2022-01-20'),
('Valentina','Viola','m21@mail.com',2700,21,'2022-01-21'),
('Giorgio','Grigi','m22@mail.com',2800,22,'2022-01-22'),
('Silvia','Marrone','m23@mail.com',2900,23,'2022-01-23'),
('Davide','Nero','m24@mail.com',2200,24,'2022-01-24'),
('Alberto','Bianco','m25@mail.com',2300,25,'2022-01-25'),
('Martina','Blu','m26@mail.com',2400,26,'2022-01-26'),
('Riccardo','Rossi','m27@mail.com',2500,27,'2022-01-27'),
('Francesca','Verdi','m28@mail.com',2600,28,'2022-01-28'),
('Claudio','Bianchi','m29@mail.com',2700,29,'2022-01-29'),
('Beatrice','Neri','m30@mail.com',2800,30,'2022-01-30');

INSERT INTO Progetti (Nome, Budget, DataInizio, DataFine) VALUES
('Proj1',1000,'2024-01-01','2024-02-01'),
('Proj2',2000,'2024-01-02','2024-02-02'),
('Proj3',3000,'2024-01-03','2024-02-03'),
('Proj4',4000,'2024-01-04','2024-02-04'),
('Proj5',5000,'2024-01-05','2024-02-05'),
('Proj6',6000,'2024-01-06','2024-02-06'),
('Proj7',7000,'2024-01-07','2024-02-07'),
('Proj8',8000,'2024-01-08','2024-02-08'),
('Proj9',9000,'2024-01-09','2024-02-09'),
('Proj10',10000,'2024-01-10','2024-02-10'),
('Proj11',11000,'2024-01-11','2024-02-11'),
('Proj12',12000,'2024-01-12','2024-02-12'),
('Proj13',13000,'2024-01-13','2024-02-13'),
('Proj14',14000,'2024-01-14','2024-02-14'),
('Proj15',15000,'2024-01-15','2024-02-15'),
('Proj16',16000,'2024-01-16','2024-02-16'),
('Proj17',17000,'2024-01-17','2024-02-17'),
('Proj18',18000,'2024-01-18','2024-02-18'),
('Proj19',19000,'2024-01-19','2024-02-19'),
('Proj20',20000,'2024-01-20','2024-02-20'),
('Proj21',21000,'2024-01-21','2024-02-21'),
('Proj22',22000,'2024-01-22','2024-02-22'),
('Proj23',23000,'2024-01-23','2024-02-23'),
('Proj24',24000,'2024-01-24','2024-02-24'),
('Proj25',25000,'2024-01-25','2024-02-25'),
('Proj26',26000,'2024-01-26','2024-02-26'),
('Proj27',27000,'2024-01-27','2024-02-27'),
('Proj28',28000,'2024-01-28','2024-02-28'),
('Proj29',29000,'2024-01-29','2024-03-01'),
('Proj30',30000,'2024-01-30','2024-03-02');


select *
from Reparti;
select*
from Dipendenti;
select*
from Progetti
where ProgettoID=13;
select*
from Assegnazioni;  

INSERT INTO Assegnazioni
(ProgettoID, DipendenteID, Ruolo) 
VALUES
(16,16,'Analista'),
(17,17,'Dev'),
(18,18,'Dev'),
(19,19,'HR'),
(20,20,'Manager'),
(21,21,'Dev'),
(22,22,'Tester'),
(23,23,'PM'),
(24,24,'Dev'),
(25,25,'Marketing'),
(26,26,'Analista'),
(27,27,'Dev'),
(28,28,'Dev'),
(29,29,'HR'),
(30,30,'Manager');

INSERT INTO Ordini (ClienteID, DataOrdine, Totale) VALUES
    (1,'2025-01-01',1500),
    (1,'2025-01-10',2000),
    (2,'2025-02-01',500),
    (3,'2025-02-10',1200),
    (4,'2025-03-01',800),
    (5,'2025-03-10',3000);

INSERT INTO Clienti (Nome, Email, Telefono) VALUES
    ('Acme SRL','acme@mail.com','3331111111'),
    ('Beta Spa','beta@mail.com','3332222222'),
    ('Gamma Srl','gamma@mail.com','3333333333'),
    ('Delta Srl','delta@mail.com','3334444444'),
    ('Omega Spa','omega@mail.com','3335555555');

SELECT * FROM Ordini;


INSERT INTO Assegnazioni (DipendenteID, ProgettoID, Ruolo)
VALUES 
    (1, 1, 'Dev'),
    (2, 1, 'Tester'),
    (3, 2, 'PM'),
    (4, 3, 'Dev'),
    (5, 4, 'Marketing'),
    (6, 5, 'Analista'),
    (7, 1, 'Dev'),
    (8, 2, 'Dev'),
    (9, 3, 'HR Support'),
    (10, 4, 'Manager');


select * from Reparti;
select * from Progetti;
-- Insert Progetti
INSERT INTO Progetti (Nome, Budget, DataInizio, DataFine) VALUES
('Proj1',1000,'2024-01-01','2024-02-01'),
('Proj2',2000,'2024-01-02','2024-02-02'),
('Proj3',3000,'2024-01-03','2024-02-03'),
('Proj4',4000,'2024-01-04','2024-02-04'),
('Proj5',5000,'2024-01-05','2024-02-05'),
('Proj6',6000,'2024-01-06','2024-02-06'),
('Proj7',7000,'2024-01-07','2024-02-07'),
('Proj8',8000,'2024-01-08','2024-02-08'),
('Proj9',9000,'2024-01-09','2024-02-09'),
('Proj10',10000,'2024-01-10','2024-02-10'),
('Proj11',11000,'2024-01-11','2024-02-11'),
('Proj12',12000,'2024-01-12','2024-02-12'),
('Proj13',13000,'2024-01-13','2024-02-13'),
('Proj14',14000,'2024-01-14','2024-02-14'),
('Proj15',15000,'2024-01-15','2024-02-15'),
('Proj16',16000,'2024-01-16','2024-02-16'),
('Proj17',17000,'2024-01-17','2024-02-17'),
('Proj18',18000,'2024-01-18','2024-02-18'),
('Proj19',19000,'2024-01-19','2024-02-19'),
('Proj20',20000,'2024-01-20','2024-02-20'),
('Proj21',21000,'2024-01-21','2024-02-21'),
('Proj22',22000,'2024-01-22','2024-02-22'),
('Proj23',23000,'2024-01-23','2024-02-23'),
('Proj24',24000,'2024-01-24','2024-02-24'),
('Proj25',25000,'2024-01-25','2024-02-25'),
('Proj26',26000,'2024-01-26','2024-02-26'),
('Proj27',27000,'2024-01-27','2024-02-27'),
('Proj28',28000,'2024-01-28','2024-02-28'),
('Proj29',29000,'2024-01-29','2024-03-01'),
('Proj30',30000,'2024-01-30','2024-03-02');


-- Insert Assegnazioni
INSERT INTO Assegnazioni VALUES
(1,1,'Dev'),(2,2,'Tester'),(3,3,'PM'),(4,4,'Dev'),(5,5,'Marketing'),
(6,6,'Analista'),(7,7,'Dev'),(8,8,'Dev'),(9,9,'HR'),(10,10,'Manager'),
(11,11,'Dev'),(12,12,'Tester'),(13,13,'PM'),(14,14,'Dev'),(15,15,'Marketing'),
(16,16,'Analista'),(17,17,'Dev'),(18,18,'Dev'),(19,19,'HR'),(20,20,'Manager'),
(21,21,'Dev'),(22,22,'Tester'),(23,23,'PM'),(24,24,'Dev'),(25,25,'Marketing'),
(26,26,'Analista'),(27,27,'Dev'),(28,28,'Dev'),(29,29,'HR'),(30,30,'Manager');

select * from Assegnazioni;
-- Insert Ordini
INSERT INTO Ordini (ClienteID, DataOrdine, Totale) VALUES
    (1,'2025-01-01',1500),
    (1,'2025-01-10',2000),
    (2,'2025-02-01',500),
    (3,'2025-02-10',1200),
    (4,'2025-03-01',800),
    (5,'2025-03-10',3000);

SELECT * FROM Ordini;
-- Insert Clienti
INSERT INTO Clienti (Nome, Email, Telefono) VALUES
    ('Acme SRL','acme@mail.com','3331111111'),
    ('Beta Spa','beta@mail.com','3332222222'),
    ('Gamma Srl','gamma@mail.com','3333333333'),
    ('Delta Srl','delta@mail.com','3334444444'),
    ('Omega Spa','omega@mail.com','3335555555');
SELECT * FROM Clienti;

-- Insert DettagliOrdine
INSERT INTO DettagliOrdine (OrdineID, Prodotto, Quantita, PrezzoUnitario) VALUES
    (1,'Laptop',1,1500),
    (2,'Server',1,2000),
    (3,'Mouse',5,100),
    (3,'Tastiera',1,100),
    (4,'Monitor',2,600),
    (5,'Stampante',1,800),
    (6,'PC Gaming',1,3000);

SELECT * FROM DettagliOrdine;
SELECT * FROM Ordini;

-- Insert DettagliOrdine
INSERT INTO DettagliOrdine (OrdineID, Prodotto, Quantita, PrezzoUnitario) VALUES
    (5,'Laptop',1,1500),
    (6,'Server',1,2000),
    (7,'Mouse',5,100),
    (8,'Tastiera',1,100),
    (9,'Monitor',2,600),
    (10,'Stampante',1,800),
    (5,'PC Gaming',1,3000);

SELECT * FROM DettagliOrdine;

