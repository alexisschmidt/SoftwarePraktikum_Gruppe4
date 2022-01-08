-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: spoverwaltung
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `module`
--

DROP TABLE IF EXISTS `module`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `module` (
  `id` int NOT NULL,
  `creationdate` datetime NOT NULL,
  `name` varchar(45) NOT NULL,
  `title` varchar(45) NOT NULL,
  `requirement` varchar(45) DEFAULT NULL,
  `examtype` varchar(45) NOT NULL,
  `instructor` int NOT NULL,
  `outcome` varchar(45) NOT NULL,
  `type` varchar(45) NOT NULL,
  `moduleparts` int NOT NULL,
  `ects` int NOT NULL,
  `edvnr` varchar(45) NOT NULL,
  `workload` varchar(45) NOT NULL,
  `module_hash` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `instructor_idx` (`instructor`),
  KEY `moduleparts_idx` (`moduleparts`),
  CONSTRAINT `instructor` FOREIGN KEY (`instructor`) REFERENCES `person` (`id`),
  CONSTRAINT `moduleparts` FOREIGN KEY (`moduleparts`) REFERENCES `modulepart` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `module`
--

LOCK TABLES `module` WRITE;
/*!40000 ALTER TABLE `module` DISABLE KEYS */;
/*!40000 ALTER TABLE `module` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `modulepart`
--

DROP TABLE IF EXISTS `modulepart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `modulepart` (
  `id` int NOT NULL,
  `creationdate` datetime NOT NULL,
  `name` varchar(45) NOT NULL,
  `title` varchar(45) NOT NULL,
  `language` varchar(45) NOT NULL,
  `literature` varchar(45) DEFAULT NULL,
  `semester` int NOT NULL,
  `sources` varchar(45) DEFAULT NULL,
  `connection` varchar(600) NOT NULL,
  `description` varchar(45) NOT NULL,
  `sws` varchar(45) NOT NULL,
  `professor` int NOT NULL,
  `ects` varchar(45) NOT NULL,
  `edvnr` varchar(45) NOT NULL,
  `workload` varchar(45) NOT NULL,
  `modulepart_hash` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `semester_idx` (`semester`),
  KEY `professor_idx` (`professor`),
  CONSTRAINT `professor` FOREIGN KEY (`professor`) REFERENCES `person` (`id`),
  CONSTRAINT `semester` FOREIGN KEY (`semester`) REFERENCES `semester` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modulepart`
--

LOCK TABLES `modulepart` WRITE;
/*!40000 ALTER TABLE `modulepart` DISABLE KEYS */;
/*!40000 ALTER TABLE `modulepart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `id` int NOT NULL,
  `creationdate` datetime NOT NULL,
  `title` varchar(45) DEFAULT NULL,
  `firstname` varchar(45) NOT NULL,
  `lastname` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `person_hash` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `semester`
--

DROP TABLE IF EXISTS `semester`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `semester` (
  `id` int NOT NULL,
  `creationdate` datetime NOT NULL,
  `name` varchar(45) NOT NULL,
  `title` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `semester`
--

LOCK TABLES `semester` WRITE;
/*!40000 ALTER TABLE `semester` DISABLE KEYS */;
/*!40000 ALTER TABLE `semester` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `spo`
--

DROP TABLE IF EXISTS `spo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `spo` (
  `id` int NOT NULL,
  `creationdate` datetime NOT NULL,
  `name` varchar(45) NOT NULL,
  `title` varchar(45) NOT NULL,
  `start_semester` int NOT NULL,
  `end_semester` int DEFAULT NULL,
  `studycourse` int NOT NULL,
  `spo_hash` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `studycourse_idx1` (`studycourse`),
  KEY `start_semester_idx` (`start_semester`),
  KEY `end_semester_idx` (`end_semester`),
  CONSTRAINT `studycourse` FOREIGN KEY (`studycourse`) REFERENCES `studycourse` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spo`
--

LOCK TABLES `spo` WRITE;
/*!40000 ALTER TABLE `spo` DISABLE KEYS */;
INSERT INTO `spo` VALUES (1,'2030-12-20 21:00:00','SPO1','labl',2,3,1,NULL),(3,'2050-10-20 00:00:00','SPO2','HALLO',3,4,1,NULL);
/*!40000 ALTER TABLE `spo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studycourse`
--

DROP TABLE IF EXISTS `studycourse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `studycourse` (
  `id` int NOT NULL,
  `creationdate` datetime NOT NULL,
  `name` varchar(45) NOT NULL,
  `title` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studycourse`
--

LOCK TABLES `studycourse` WRITE;
/*!40000 ALTER TABLE `studycourse` DISABLE KEYS */;
INSERT INTO `studycourse` VALUES (1,'2022-01-04 00:00:00','WI','Wirtschaftsinformatik'),(2,'2022-01-04 00:00:00','OMM','Online Medien mAnagaement');
/*!40000 ALTER TABLE `studycourse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL,
  `creationdate` datetime NOT NULL,
  `firstname` varchar(45) NOT NULL,
  `lastname` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `google_user_id` varchar(60) NOT NULL,
  `isadmin` tinyint(1) NOT NULL,
  `user_hash` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'0001-01-01 00:00:00','Sebastian','Hennich','sh@hdm-de','',0,NULL),(2,'2022-01-04 00:00:00','deniz','gazitepe','dz@hdm.de','',0,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-08 13:27:16
