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
  `ects` int NOT NULL,
  `edvnr` varchar(45) NOT NULL,
  `workload` varchar(45) NOT NULL,
  `module_hash` int NOT NULL,
  PRIMARY KEY (`module_hash`),
  KEY `instructor_idx` (`instructor`),
  CONSTRAINT `instructor` FOREIGN KEY (`instructor`) REFERENCES `person` (`person_hash`)
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
-- Table structure for table `modulelist`
--

DROP TABLE IF EXISTS `modulelist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `modulelist` (
  `id` int NOT NULL,
  `creationdate` varchar(45) NOT NULL,
  `module` int NOT NULL,
  `modulepart` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `module_idx` (`module`),
  KEY `modulepart_idx` (`modulepart`),
  CONSTRAINT `module` FOREIGN KEY (`module`) REFERENCES `module` (`module_hash`),
  CONSTRAINT `modulepart` FOREIGN KEY (`modulepart`) REFERENCES `modulepart` (`modulepart_hash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modulelist`
--

LOCK TABLES `modulelist` WRITE;
/*!40000 ALTER TABLE `modulelist` DISABLE KEYS */;
/*!40000 ALTER TABLE `modulelist` ENABLE KEYS */;
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
  `modulepart_hash` int NOT NULL,
  PRIMARY KEY (`modulepart_hash`),
  KEY `professor_idx` (`professor`),
  CONSTRAINT `professor` FOREIGN KEY (`professor`) REFERENCES `person` (`person_hash`)
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
  `firstname` varchar(45) NOT NULL,
  `lastname` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `person_hash` int NOT NULL,
  PRIMARY KEY (`person_hash`)
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
  `semester_hash` int NOT NULL,
  PRIMARY KEY (`semester_hash`)
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
  `spo_hash` int NOT NULL,
  PRIMARY KEY (`spo_hash`),
  KEY `studycourse_idx` (`studycourse`),
  KEY `start_semester_idx` (`start_semester`),
  KEY `end_semester_idx` (`end_semester`),
  CONSTRAINT `end_semester` FOREIGN KEY (`end_semester`) REFERENCES `semester` (`semester_hash`),
  CONSTRAINT `start_semester` FOREIGN KEY (`start_semester`) REFERENCES `semester` (`semester_hash`),
  CONSTRAINT `studycourse` FOREIGN KEY (`studycourse`) REFERENCES `studycourse` (`studycourse_hash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spo`
--

LOCK TABLES `spo` WRITE;
/*!40000 ALTER TABLE `spo` DISABLE KEYS */;
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
  `studycourse_hash` int NOT NULL,
  PRIMARY KEY (`studycourse_hash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studycourse`
--

LOCK TABLES `studycourse` WRITE;
/*!40000 ALTER TABLE `studycourse` DISABLE KEYS */;
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
  `user_hash` int NOT NULL,
  PRIMARY KEY (`user_hash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
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

-- Dump completed on 2022-01-19 10:15:06
