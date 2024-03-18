-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: scoala_de_soferi
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `programari_examen`
--

DROP TABLE IF EXISTS `programari_examen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `programari_examen` (
  `ProgramareID` int NOT NULL,
  `EvaluareID` int DEFAULT NULL,
  `CursantID` int DEFAULT NULL,
  `InstructorID` int DEFAULT NULL,
  `MasinaID` int DEFAULT NULL,
  `CategorieID` int DEFAULT NULL,
  `DataExamen` date DEFAULT NULL,
  PRIMARY KEY (`ProgramareID`),
  KEY `CursantID` (`CursantID`),
  KEY `InstructorID` (`InstructorID`),
  KEY `MasinaID` (`MasinaID`),
  KEY `CategorieID` (`CategorieID`),
  KEY `EvaluareID` (`EvaluareID`),
  CONSTRAINT `programari_examen_ibfk_1` FOREIGN KEY (`CursantID`) REFERENCES `cursanti` (`CursantID`),
  CONSTRAINT `programari_examen_ibfk_2` FOREIGN KEY (`InstructorID`) REFERENCES `instructori` (`InstructorID`),
  CONSTRAINT `programari_examen_ibfk_3` FOREIGN KEY (`MasinaID`) REFERENCES `masini` (`MasinaID`),
  CONSTRAINT `programari_examen_ibfk_4` FOREIGN KEY (`CategorieID`) REFERENCES `categorii_permis` (`CategorieID`),
  CONSTRAINT `programari_examen_ibfk_5` FOREIGN KEY (`EvaluareID`) REFERENCES `rezultate_examen` (`EvaluareID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `programari_examen`
--

LOCK TABLES `programari_examen` WRITE;
/*!40000 ALTER TABLE `programari_examen` DISABLE KEYS */;
/*!40000 ALTER TABLE `programari_examen` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-26 17:47:55
