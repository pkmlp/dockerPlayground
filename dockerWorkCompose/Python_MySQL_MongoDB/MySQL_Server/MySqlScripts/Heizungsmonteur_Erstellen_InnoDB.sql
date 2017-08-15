--
--
-- Peter Kessler's Moodle Lernportal, PKMLP
-- www.pkmlp.ch
--
-- Datenbanken Grundlagen
-- Beispieldatenbank: Heizungsmonteur
--
--
--
-- loeschen, erstellen der Datenbank (des Schemas) Heizungsmonteur
--

DROP DATABASE IF EXISTS Heizungsmonteur;
CREATE DATABASE IF NOT EXISTS Heizungsmonteur;
USE Heizungsmonteur;

--
-- loeschen aller Tabellen in der Datenbank (im Schema) heizungsmonteur
--

DROP TABLE IF EXISTS Monteur,
                     Funktion,
                     Abteilung,
                     Kunde,
                     Fahrzeug,
                     Fahrt,
                     Rapport;

--
-- erstellen der Tabelle funktion
--               Achtung Reihenfolge: zuerst die Tabellen ohne Fremdschluessel erstellen,
--                                    da sonst auf Tabellen referenziert wird,
--                                    die allenfalls noch nicht vorhanden sind !
--

CREATE TABLE Funktion (
    F_Nr         CHAR(2)         NOT NULL,
    Funktion     VARCHAR(16)     NOT NULL,
    PRIMARY KEY (F_Nr)
)engine=InnoDB;

INSERT INTO Funktion VALUES ('F1' ,'Monteur-B');
INSERT INTO Funktion VALUES ('F2' ,'Monteur-A');



CREATE TABLE Abteilung (
    A_Nr         CHAR(2)         NOT NULL,
    Abteilung    VARCHAR(16)     NOT NULL,
    PRIMARY KEY (A_Nr)
)engine=InnoDB;

INSERT INTO Abteilung VALUES ('A1' ,'Heizung');
INSERT INTO Abteilung VALUES ('A2' ,'Sanitaer');



CREATE TABLE Monteur (
    M_NR          CHAR(2)         NOT NULL,
    M_Name        VARCHAR(16)     NOT NULL,
    F_Nr          CHAR(2)         NOT NULL,
    A_Nr          CHAR(2)         NOT NULL,
    FOREIGN KEY (F_Nr)    REFERENCES Funktion  (F_Nr)   ON DELETE NO ACTION,
    FOREIGN KEY (A_NR)    REFERENCES Abteilung (A_Nr)   ON DELETE NO ACTION,
    PRIMARY KEY (M_NR)
)engine=InnoDB;

INSERT INTO Monteur VALUES ('M1','Roth','F2','A1');
INSERT INTO Monteur VALUES ('M2','Gelb','F1','A2');
INSERT INTO Monteur VALUES ('M3','Braun','F1','A1');
INSERT INTO Monteur VALUES ('M4','Weiss','F2','A2');



CREATE TABLE Kunde (
    K_Nr                CHAR(2)         NOT NULL,
    K_Name              VARCHAR(16)     NOT NULL,
    PRIMARY KEY (K_Nr)
)engine=InnoDB;

INSERT INTO Kunde VALUES ('K1' ,'Osiris AG');
INSERT INTO Kunde VALUES ('K2' ,'STFW');
INSERT INTO Kunde VALUES ('K3' ,'Ariel GmbH');



CREATE TABLE Fahrzeug (
    FZ_Nr               CHAR(4)         NOT NULL,
    Kontrollschildnr    VARCHAR(16)     NOT NULL,
    Plaetze             INT             NOT NULL,
    PRIMARY KEY (FZ_Nr)
)engine=InnoDB;

INSERT INTO Fahrzeug VALUES ('FZ10' ,'ZH 112 100', 2);
INSERT INTO Fahrzeug VALUES ('FZ11' ,'ZH 187 333', 3);
INSERT INTO Fahrzeug VALUES ('FZ12' ,'TG 214 956', 5);



CREATE TABLE Fahrt (
    FZ_Nr        CHAR(4)         NOT NULL,
    M_Nr         CHAR(2)         NOT NULL,
    Datum        DATE            NOT NULL,
    Kilometer    INT             NOT NULL,
    FOREIGN KEY (FZ_Nr)       REFERENCES Fahrzeug (FZ_Nr)  ON DELETE NO ACTION,
    FOREIGN KEY (M_Nr)        REFERENCES Monteur (M_Nr)    ON DELETE NO ACTION,
    PRIMARY KEY (FZ_Nr, M_Nr, Datum)
)engine=InnoDB;

INSERT INTO Fahrt VALUES ('FZ10' ,'M1','2010-08-21', 4);
INSERT INTO Fahrt VALUES ('FZ10' ,'M2','2010-08-21', 4);
INSERT INTO Fahrt VALUES ('FZ12' ,'M2','2010-08-22', 8);
INSERT INTO Fahrt VALUES ('FZ11' ,'M1','2010-08-22', 8);
INSERT INTO Fahrt VALUES ('FZ12' ,'M3','2010-08-22', 2);



CREATE TABLE Rapport (
    M_Nr            CHAR(2)         NOT NULL,
    K_Nr            CHAR(2)         NOT NULL,
    Datum           DATE            NOT NULL,
    Zeit            INT             NOT NULL,
    FOREIGN KEY (K_Nr)      REFERENCES Kunde (K_Nr)      ON DELETE NO ACTION,
    FOREIGN KEY (M_Nr)      REFERENCES Monteur (M_Nr)    ON DELETE NO ACTION,
    PRIMARY KEY (M_Nr, K_Nr, Datum)
)engine=InnoDB;

INSERT INTO Rapport VALUES ('M1' ,'K1','2010-08-21', 4);
INSERT INTO Rapport VALUES ('M1' ,'K3','2010-08-21', 4);
INSERT INTO Rapport VALUES ('M2' ,'K2','2010-08-21', 8);
INSERT INTO Rapport VALUES ('M3' ,'K1','2010-08-20', 8);
INSERT INTO Rapport VALUES ('M3' ,'K2','2010-08-21', 2);
INSERT INTO Rapport VALUES ('M3' ,'K1','2010-08-21', 3);
INSERT INTO Rapport VALUES ('M4' ,'K1','2010-08-22', 2);
