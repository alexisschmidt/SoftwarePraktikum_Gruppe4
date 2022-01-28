-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema spoverwaltung
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `spoverwaltung` ;

-- -----------------------------------------------------
-- Schema spoverwaltung
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `spoverwaltung` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `spoverwaltung` ;

-- -----------------------------------------------------
-- Table `spoverwaltung`.`module`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `spoverwaltung`.`module` ;

CREATE TABLE IF NOT EXISTS `spoverwaltung`.`module` (
  `id` INT NOT NULL,
  `creationdate` DATETIME NOT NULL,
  `createdby` BIGINT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `title` VARCHAR(45) NOT NULL,
  `requirement` VARCHAR(2000) NULL DEFAULT NULL,
  `examtype` VARCHAR(45) NOT NULL,
  `outcome` VARCHAR(2000) NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  `ects` INT NOT NULL,
  `edvnr` VARCHAR(45) NOT NULL,
  `workload` VARCHAR(2000) NOT NULL,
  `module_hash` BIGINT NOT NULL,
  `instructor_hash` BIGINT NOT NULL,
  PRIMARY KEY (`module_hash`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

LOCK TABLES `module` WRITE;
/*!40000 ALTER TABLE `module` DISABLE KEYS */;
INSERT INTO `module` VALUES (1,'2022-01-27 10:23:00',3242341,'MODUL MARKETING & ORGANISATION','(MARKETING & ORGANISATION )','-','KL 90 Min','Nach Abschluss des Moduls\nkennen die Studierenden die wichtigsten Grundbegriffe der Disziplinen Marketing und Organisation','Pflichtmodul im Grundstudium',5,335120,'Siehe einzelne Lehrveranstaltung',342357,112313),(2,'2022-01-27 18:00:32',213123,'MODUL GRUNDLAGEN WIRTSCHAFTSINFORMATIK','(FUNDAMENTALS OF INFORMATION SYSTEMS)','-','KMP','Die Studierenden erhalten einen umfassenden Überblick über die Wirtschaftsinformatik, ihre Ziele, Methoden, Konzepte und Kernbegriffe. Dadurch werden die Studierenden befähigt, ein Verständnis für die betriebliche Datenverarbeitung zu entwickeln und die Zusammenhänge zwischen technischen und wirtschaftlichen Aspekten von Informationssystemen zu beurteilen','Pflichtmodul im Grundstudium',5,335121,'5 ECTS= 150 Stunden - Vorlesung: 72h - Vor/Nacharbeit Vorlesung & Klausurvorbereitung: 78h',56673,231345),(3,'2022-01-27 18:00:00',435435112,'GRUNDLAGEN DATENBANKEN','(FUNDAMENTALS OF DATABASES)','-','KMP','Die Studierenden kenne die Grundlagen zur Datenbanktheorie, können die verschiedenen Datenbanktypen unterscheiden. Sie verfügen über die Grundlagen zum Aufbau von einfachen Datenbanken und können diese selbstständig auch praktisch umsetzen.','Pflichtmodul im Grundstudium',5,335122,'Gesamtaufwand: 5 ECTS = 150 Stunden für Vorlesung, Übung und Klausurvorbereitung',12346457,787684234),(4,'2022-01-27 19:06:20',2312312,'MODUL PROGRAMMIEREN','(PROGRAMMING)','-','KMP','Im Rahmen dieses Moduls erlernen die Teilnehmer\nallgemeine technologische Grundlagen von Programmiersprachen\nGrundlagen der Programmierung am Beispiel einer aktuellen, praxisrelevanten Programmiersprache\nObjektorientierte Programmierungmit dem Ziel, eigene Software-Systeme umsetzen zu können.','Pflichtmodul im Grundstudium',5,335123,'15 Termine zu je 2 SWS Vorlesung & 2 SWS Übung: 45 h Kontaktzeit\n15x Vor- und Nachbereitung bzgl. o.g. Termine zu je 7 h: 105 h Selbststudium\nSumme: 150 h (5 ECTS Äquivalent)',56542342456,2132354),(5,'2022-01-27 19:35:00',6767442,'MODUL EXTERNES UND INTERNES RECHNUNGSWESEN','(EXTERNAL AND INTERNAL ACCOUNTING )','-','KL, 90 Min','Nach erfolgreicher Teilnahme an der Veranstaltung verfügen die Studierenden über ein fundiertes Basiswissen im Themengebiet Betriebliches Rechnungswesen','Pflichtmodul im Grundstudium',5,335125,'Gesamter Zeitaufwand (Workload) = 150 Zeitstunden',34513123,23423565476),(6,'2022-01-27 20:00:00',32423111,'PROPÄDEUTIK WI','Propädeutik WI','-','KMP','Nach erfolgreichem Besuch des Moduls kennen und verstehen die Studierenden die wesentlichen Grundlagen der Wirtschaftsinformatik und hierbei insbesondere die Grundlagen der quantitativ orientierten betriebswirtschaftlichen Modulen des Studiengangs Wirtschaftsinformatik und digitale Medien.','Pflichtmodul im Grundstudium',5,335126,'	Gesamter Zeitaufwand (Workload) = 150 Zeitstunden',123677876,65768),(7,'2022-01-27 18:23:00',324211234,'DIENSTLEISTUNGSMANAGMENT','(MANAGEMENT OF SERVICES )','-','KMP','Im Modul werden die Grundlagen zum Management von Dienstleistungen vermittelt. Die umfasst a) die Grundlagen des Dienstleistungsmanagement (Definition, Bedeutung, Abgrenzung von Sachgütern, Strategieentscheidungen, Dienstleistungsprozesse, Kundenintegration und -Erlebnisse, Dienstleistungsinnovation) b) die Definition von Qualitätsmerkmalen von Dienstleistungen, Ansätze zu deren Erfassung (Qualitätsmessung) und die Umsetzung im Rahmen von Qualitätsmanagementansätze','(Pflichtmodul im Grundstudium)',5,335132,'Präsenzzeiten:\n15 Termine zu je 4 SWS = 45 Zeitstunden:\nIndividualarbeit und Gruppenarbeit 60 Zeitstunden\nGesamter Zeitaufwand (Workload) = 150 Zeitstunden',23423476,7867456);
/*!40000 ALTER TABLE `module` ENABLE KEYS */;
UNLOCK TABLES;

-- -----------------------------------------------------
-- Table `spoverwaltung`.`modulepart`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `spoverwaltung`.`modulepart` ;

CREATE TABLE IF NOT EXISTS `spoverwaltung`.`modulepart` (
  `id` INT NOT NULL,
  `creationdate` DATETIME NOT NULL,
  `createdby` BIGINT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `title` VARCHAR(45) NOT NULL,
  `language` VARCHAR(45) NOT NULL,
  `literature` VARCHAR(2000) NULL DEFAULT NULL,
  `semester` INT NOT NULL,
  `sources` VARCHAR(2000) NULL DEFAULT NULL,
  `connection` VARCHAR(2000) NOT NULL,
  `description` VARCHAR(2000) NOT NULL,
  `sws` INT NOT NULL,
  `ects` INT NOT NULL,
  `edvnr` VARCHAR(45) NOT NULL,
  `workload` VARCHAR(2000) NOT NULL,
  `modulepart_hash` BIGINT NOT NULL,
  `professor_hash` BIGINT NOT NULL,
  `module_hash` BIGINT NOT NULL,
  PRIMARY KEY (`modulepart_hash`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

LOCK TABLES `modulepart` WRITE;
/*!40000 ALTER TABLE `modulepart` DISABLE KEYS */;
INSERT INTO `modulepart` VALUES (3,'2022-01-25 16:20:02',57657,'335121A GRUNDLAGEN WIRTSCHAFTSINFORMATIK','Grundlagen WI','Deutsch','Keine',1,'https://e-learning.hdm-stuttgart.de/moodle/course/view.php?id=3036','Keine','(siehe Modulbeschreibung)',4,5,3351211,'(siehe Modulbeschreibung)',6546,2131235,345345),(8,'2022-01-27 18:00:07',234234,'335125 EXTERNES UND INTERNES RECHNUNGSWESEN','Vorlesung Rechnungswesen','Deutsch','Weber, J./Weißenberger, B.: Einführung in das Rechnungswesen, 7., 8. oder 9.,Aufl., Stuttgart 2006, 2009, 2015.\nSchultz, V., Basiswissen Rechnungswesen, 5. Aufl., München 2008',2,'Eine ausführliche Beschreibung der Lehrinhalte, der Lernziele, der Struktur sowie zusätzliches Lehrmaterial (Gliederung, Skript, Übungsaufgaben/Fallstudien etc.) finden Sie im Online-Kurs zur Veranstaltung auf der Moodle-Plattform der HDM.','keine','Einführung in das Betriebliche Rechnungswesen und Einordnung in den Unternehmensprozess\nDoppelte Buchführung\nGrundlagen der Buchführung\nMethodik der Buchführung\nOrganisation der Buchführung\nGrundlegende Abbildungs- und Buchungsvorgänge\nBilanzierung und Jahresabschluss\nGrundlagen des Jahresabschlusses\nGrundlagen der Bilanzierung\nKosten- und Leistungsrechnung\nGrundlagen der Kosten- und Leistungsrechnung\nKostenartenrechnung\nKostenstellenrechnung\nKostenträgerrechnung',4,5,3351251,'Präsenzzeiten:\n13 Wochen zu je 4 SWS = 37 Zeitstunden\nSelbstlernzeiten:\nVor-/Nachbereitung der Veranstaltungen: 70 Zeitstunden\nVor-/Nachbereitung und Prüfungsvorbereitung: 43 Zeitstunden\nGesamter Zeitaufwand (Workload) = 150 Zeitstunden',98797,4435456,756735),(7,'2022-01-27 17:10:06',45431,'335123B ÜBUNG PROGRAMMIEREN','Übung Programmieren','Deutsch','siehe Vorlesung',1,'siehe Vorlesung','Bei dieser Lehrveranstaltung handelt es sich um inhaltlich abgestimmte Übungen zur gleichnamigen Vorlesung in diesem Modul.','Abgegrenzte, überschaubare Aufgaben zu den einzelnen in der Vorlesung behandelten Themen.',2,3,3351232,'siehe Modul',256757,46899996,768678),(10,'2022-01-27 18:00:09',6546546,'MATHEMATISCHE GRUNDLAGEN DER INFORMATIK','Mathematische Grundlagen der Informatik','Deutsch','keine',2,'keine','Statistik von Propädeutik','keine',2,2,3351264,'-',332425,65654543,657909097),(1,'2022-01-27 16:00:00',546456,'335120A MARKETING','Markting','Deutsch','Voeth, M., Herbst, U., Marketing-Management, Stuttgart 2013.',1,'https://e-learning.hdm-stuttgart.de/moodle/course/view.php?id=1570','Organisation','Gem. Senatssitzung v. 15.10.21 ab WS 21/22: Änd.d.Prüfungsform in KL, 90 MinGrundlagen des Marketing: der Marketingbegriff und das ihm zu Grunde liegende Verständnis Wissen sammeln: Erforschung des Konsumentenverhaltens, Zielgruppenanalyse, Marktforschung\nFestlegung der Marketingstrategie und der Marketingziele Der Marketingmix: Produkt-, Preis-, Kommunikations- und Distributionspolitik',2,2,3351201,'Präsenzveranstaltung (15 Termine à 2 SWS) = 22,5 Zeitstunden.\nVor- und Nachbereitung = 22,5 Zeitstunden\nKlausurvorbereitung: 5,5 Tage zu je 8 Zeitstunden = 44 Zeitstunden\nGesamter Zeitaufwand (Workload) = 89 Zeitstunde',435345,54656,546456),(2,'2022-01-27 16:00:01',54645,'335120B ORGANISATION','Organisation','Deutsch','Frese, E., Graumann, M., Talaulicar, T., Theuvsen, L.: Grundlagen der Organisation. Entscheidungsorientiertes Konzept der Organisationsgestaltung, 11. Aufl., Wiesbaden: Springer Gabler 2019 (-> SpringerLink)',1,'Moodle-Kurs: https://e-learning.hdm-stuttgart.de/moodle/course/view.php?id=460','Marketing','Einführung und Organisationsverständnis\nOrganisationsbegriff\nWesentliche Frage- und Problemstellungen der Organisationslehre\nOrganisationstheorien\nEntwicklungslinien der Organisationstheorie\nEinordnung und Diskussion ausgewählter Theorien\nAufgabenbegriff in der Organisation\nAufgabe als Grundelement der Organisationsgestaltung (Aufbau- und Ablauforganisation)\nAufbauorganisation',2,3,3351202,'Vorlesung:\n22,5 Zeitstunden\nÜbungen und Prüfungsvorbereitung:\nVorlesungsbegleitende Übungsaufgaben:Zeitstunden\nPrüfungsvorbereitung: 2,5 Tage zu je 8 Zeitstunden = 20 Zeitstunden\nGesamtaufwand\nGesamter Zeitaufwand (Workload)= 87,5 Zeitstunden',435435,123123,34243),(6,'2022-01-27 17:00:05',1232135,'335123A VORLESUNG PROGRAMMIEREN','Vorlesung Programmieren','Deutsch','Klein, B. (2018). Einführung in Python 3: für Ein- und Umsteiger (3., überarbeitete Auflage). München: Hanser.\n\nBeazley, D. M., & Jones, B. K. (2013). Python cookbook (Third edition). Sebastopol, CA: O’Reilly.',1,'www.python.org\nHomepage des Dozenten','	Zu dieser Grundlagenvorlesung gibt es im Modul eine inhaltlich abgestimmte Übung.','	\nAllgemeine Einführung in Programmiersprachen\nEinführung in die Programmiersprache Python\nBausteine der Programmierung: Variable, Operatoren, Ausdrücke, Funktionen\nBerechnungen: Anweisungen, Kontrollfluss\nObjektorientierte Konzepte: Objekte, Klassen, Methoden, Vererbung\nSpezielle Datenstrukturen: Zeichenketten, Listen & Tupel, Dictionaries, Mengen',2,2,3351231,'siehe Modul',656675,234234,3246546),(12,'2022-01-27 18:00:11',231312,'QUALITÄTSMANAGEMENT FÜR DIENSTLEISTUNGEN','Qualitätsmanagement','Deutsch','Bruhn, M. (2016): Qualitätsmanagement für Dienstleistungen: Grundlagen, Konzepte, Methoden. 9. Auflage. Berlin: Springer Gabler\nHaller, S. (2017): Dienstleistungsmanagement, Grundlagen - Konzepte - Instrumente, 7., Aufl., Wiesbaden: Springer Gabler (-> Kap. 8)',2,'Moodle-Kurs: https://e-learning.hdm-stuttgart.de/moodle/course/view.php?id=1842','Dienstleistungsmangement','In der Lehrveranstaltung werden folgende Themen behandelt:\nDienstleistungsqualität\nAllgemeiner Qualitätsbegriff\nAspekte der Dienstleistungsqualität\n\nAnalyse und Messung der Dienstleistungsqualität\nModelle zur Analyse der Dienstleistungsqualität\nMethoden zur Messung der Dienstleistungsqualität\n\nVerankerung des QM in Unternehmen\nQualitätsmanagementsysteme\nEinführung von QM in Unternehmen',2,3,3351322,'Präsenzzeiten:\n15 Termine zu je 2 SWS = 22,5 Zeitstunden\nSelbstlernzeiten:\nVor-/Nachbereitung der theoretischen Grundlagen: 22,5 Zeitstunden\nIndividuelle Fallstudienbearbeitung:\nIndividuelle Umsetzung der Grundlagen in einer Fallstudienarbeit: 45 Zeitstunden',886643,23423422,35467882),(9,'2022-01-27 18:00:08',23423543,'335126C STATISTIK','Statistik von Propädeutik','Deutsch','keine',2,'keine','Mathematische Grundlagen der Informatik','keine',2,3,3351263,'-',896785,764625,566753),(5,'2022-01-27 16:00:04',45462,'335122B ÜBUNG DATENBANKEN','ÜBUNG DATENBANKEN','Deutsch','siehe Vorlesung',1,'siehe Vorlesung','Vorlesung Datenbanken','Die theoretischen Grundlagen aus der Vorlesung werden geübt:\nTheoretische Grundlagen\nEntity-Relationship-Modell\nNormalisierung\nvom ERM zum Relationalen Modell\nEinführung in SQL\nSQL Joins\nNoSQL-Übungen',2,3,3351222,'Übungen\n15 Wochen, 1,5 Std. = 22 Std.\nVorbereitung\n15 Wochen, 3 Std. = 45 Std.',6786786,978675,345352),(4,'2022-01-27 16:45:09',3123213,'335122A VORLESUNG DATENBANKEN','VORLESUNG DATENBANKEN','Deutsch','Datenbanken für Wirtschaftsinformatiker. Autoren: Sönke Cordts, Gerold Blakowski und Gerhard Brosius. Vieweg+Teubner (2011). eBook bei SpringerLink\nGrundkurs Relationale Datenbanken (8. Auflage). Autor: René Steiner. Springer Vieweg (2014). eBook bei SpringerLink\nDatenbanken und SQL (5. Auflage). Autor: Edwin Schicker. Springer Vieweg (2017). eBook bei SpringerLink',1,'Alle Kursunterlagen und sonstigen Informationen sind im Moodle-Kurs Datenbanken Grundlagen (335122) - SoSe 2020 zu finden.','Übung Datenbanken','In diesem Modul beschäftigen wir uns mit Aspekten der Datenhaltung. Im Mittelpunkt stehen dabei Datenbanken. Unter anderem behandeln wir die folgenden Inhalte:\nDaten, Informationen und Wissen\nArchitekturaspekte von Datenbanksystemen\nDatenmodellierung\nRelationale Datenbanksysteme\nNormalisierung von Datenbankschemata\nNoSQL und NewSQL',2,2,3351221,'Vorlesung\n15 Wochen, 1,5 Std. = 22 Std.\nVorbereitung\n15 Wochen, 3 Std. = 45 Std.',21987987,3254561,234234),(11,'2022-01-27 18:10:10',4353451,'335132A DIENSTLEISTUNGSMANAGEMENT','Dienstleistungsmangement','Deutsch','Haller, S. (2017): Dienstleistungsmanagement, Grundlagen - Konzepte - Instrumente, 7., Aufl., Wiesbaden: Springer Gabler\nFließ, S. (2009): Dienstleistungsmanagement. Kundenintegration gestalten und steuern, Wiesbaden: Gabler',2,'Moodle-Kurs: https://e-learning.hdm-stuttgart.de/moodle/course/view.php?id=1842','Qualitätsmanagement','Einführung und Vertiefung ausgewählter Aspekte des Dienstleistungsmanagements:\n- Ökonomische Bedeutung des Dienstleistungssektors\n- Dienstleistungsbegriff und Kategorisierung\n- Strategische Entscheidungen im Dienstleistungsmanagement\n- Kundenmanagement und Kundenintegration\n- Dienstleistungsentwicklung / -design\n- Management von Dienstleistungsprozessen\n- Personalmanagement in Dienstleistungsunternehmen\n- Innovation (Formen und Aspekte)',2,2,3351321,'Präsenzzeiten:\n15 Termine zu je 2 SWS = 22,5 Zeitstunden\nSelbstlernzeiten:\nVor-/Nachbereitung der theoretischen Grundlagen: 22,5 Zeitstunden\nIndividuelle Fallstudienbearbeitung:\nIndividuelle Umsetzung der Grundlagen in einer Fallstudienarbeit: 15 Zeitstunden',54767833,5633455,776653);
/*!40000 ALTER TABLE `modulepart` ENABLE KEYS */;
UNLOCK TABLES;

-- -----------------------------------------------------
-- Table `spoverwaltung`.`person`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `spoverwaltung`.`person` ;

CREATE TABLE IF NOT EXISTS `spoverwaltung`.`person` (
  `id` INT NOT NULL,
  `creationdate` DATETIME NOT NULL,
  `createdby` BIGINT NOT NULL,
  `firstname` VARCHAR(45) NOT NULL,
  `lastname` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `person_hash` BIGINT NOT NULL,
  PRIMARY KEY (`person_hash`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES (1,'2022-01-27 15:00:30',1234,'Peter','Thies','xy@web.de',324235),(2,'2022-01-27 15:00:30',1235,'Christoph','Kunz','xy@web.de',5435435),(3,'2022-01-27 15:00:30',21335,'David','Klotz','xy@web.de',213123),(4,'2022-01-27 15:00:30',324234,'Martin','Engstler','xy@web.de',4324324),(5,'2022-01-27 15:00:30',213124,'Udo','Mildenberger','xy@web.de',454351),(6,'2022-01-27 15:00:30',45234,'Hendrik','Meth','xy@web.de',123123),(7,'2022-01-27 15:00:30',123123,'Bettina','Schwarzer','xy@web.de',2456765);
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

-- -----------------------------------------------------
-- Table `spoverwaltung`.`semester`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `spoverwaltung`.`semester` ;

CREATE TABLE IF NOT EXISTS `spoverwaltung`.`semester` (
  `id` INT NOT NULL,
  `creationdate` DATETIME NOT NULL,
  `createdby` BIGINT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `title` VARCHAR(45) NOT NULL,
  `semester_hash` BIGINT NOT NULL,
  PRIMARY KEY (`semester_hash`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

LOCK TABLES `semester` WRITE;
/*!40000 ALTER TABLE `semester` DISABLE KEYS */;
INSERT INTO `semester` VALUES (1,'2022-01-28 10:10:20',32467333,'Wintersemester 2021/2022','WS 21/22',90823402),(2,'2022-01-28 10:10:20',32467976976,'Sommersemester 2022','SS 22',908234044123),(3,'2022-01-28 10:10:20',3246792456336,'Wintersemester 2022/2023','WS 22/23',908234048880);
/*!40000 ALTER TABLE `semester` ENABLE KEYS */;
UNLOCK TABLES;

-- -----------------------------------------------------
-- Table `spoverwaltung`.`spo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `spoverwaltung`.`spo` ;

CREATE TABLE IF NOT EXISTS `spoverwaltung`.`spo` (
  `id` INT NOT NULL,
  `creationdate` DATETIME NOT NULL,
  `createdby` BIGINT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `title` VARCHAR(45) NOT NULL,
  `spo_hash` BIGINT NOT NULL,
  `studycourse_hash` BIGINT NOT NULL,
  PRIMARY KEY (`spo_hash`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `spoverwaltung`.`spocomposition`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `spoverwaltung`.`spocomposition` ;

CREATE TABLE IF NOT EXISTS `spoverwaltung`.`spocomposition` (
  `id` INT NOT NULL,
  `module_hash` BIGINT NOT NULL,
  `spo_hash` BIGINT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `spoverwaltung`.`spovalidity`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `spoverwaltung`.`spovalidity` ;

CREATE TABLE IF NOT EXISTS `spoverwaltung`.`spovalidity` (
  `id` INT NOT NULL,
  `spo_hash` BIGINT NOT NULL,
  `semester_hash` BIGINT NOT NULL,
  `startsem` TINYINT(1) NOT NULL DEFAULT '0',
  `endsem` TINYINT(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `spoverwaltung`.`studycourse`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `spoverwaltung`.`studycourse` ;

CREATE TABLE IF NOT EXISTS `spoverwaltung`.`studycourse` (
  `id` INT NOT NULL,
  `creationdate` DATETIME NOT NULL,
  `createdby` BIGINT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `title` VARCHAR(45) NOT NULL,
  `studycourse_hash` BIGINT NOT NULL,
  PRIMARY KEY (`studycourse_hash`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


LOCK TABLES `studycourse` WRITE;
/*!40000 ALTER TABLE `studycourse` DISABLE KEYS */;
INSERT INTO `studycourse` VALUES (1,'2022-01-28 11:10:20',97675643,'Wirtschaftsinformatik und digitale Medien','WI7',932492586),(2,'2022-01-28 11:10:20',54654634,'Online Meedienmangagement','OMM',3244234),(3,'2022-01-28 11:10:20',2342345,'Wirtschaftsingeneurwesen','WIN',6546546),(4,'2022-01-28 11:10:20',4365654,'Informationsdesign','ID',123213),(5,'2022-01-28 11:10:20',13213,'Medieninformatik','MI',657657);
/*!40000 ALTER TABLE `studycourse` ENABLE KEYS */;
UNLOCK TABLES;

-- -----------------------------------------------------
-- Table `spoverwaltung`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `spoverwaltung`.`user` ;

CREATE TABLE IF NOT EXISTS `spoverwaltung`.`user` (
  `id` INT NOT NULL,
  `creationdate` DATETIME NOT NULL,
  `createdby` BIGINT NOT NULL,
  `firstname` VARCHAR(45) NOT NULL,
  `lastname` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `google_user_id` VARCHAR(60) NOT NULL,
  `isadmin` TINYINT(1) NOT NULL,
  `user_hash` BIGINT NOT NULL,
  `spo_hash` BIGINT NULL DEFAULT NULL,
  PRIMARY KEY (`user_hash`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;