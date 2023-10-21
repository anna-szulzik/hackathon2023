-- MySQL dump 10.13  Distrib 8.0.27, for macos11 (x86_64)
--
-- Host: localhost    Database: hackathon
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `quotation`
--

DROP TABLE IF EXISTS `quotation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quotation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `client_id` int DEFAULT NULL,
  `event_type` bigint DEFAULT NULL,
  `event_model` bigint DEFAULT NULL,
  `event_suppliers` bigint DEFAULT NULL,
  `venue` bigint DEFAULT NULL,
  `structure` bigint DEFAULT NULL,
  `custom_decoration` tinyint(1) DEFAULT NULL,
  `custom_prints` tinyint(1) DEFAULT NULL,
  `marketing` tinyint(1) DEFAULT NULL,
  `init_time` varchar(20) DEFAULT NULL,
  `end_time` varchar(20) DEFAULT NULL,
  `service` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `event_type` (`event_type`),
  KEY `event_model` (`event_model`),
  KEY `event_suppliers` (`event_suppliers`),
  KEY `venue` (`venue`),
  KEY `structure` (`structure`),
  KEY `service` (`service`),
  CONSTRAINT `quotation_ibfk_1` FOREIGN KEY (`event_type`) REFERENCES `event_type` (`id`),
  CONSTRAINT `quotation_ibfk_2` FOREIGN KEY (`event_model`) REFERENCES `event_model` (`id`),
  CONSTRAINT `quotation_ibfk_3` FOREIGN KEY (`event_suppliers`) REFERENCES `supplier` (`id`),
  CONSTRAINT `quotation_ibfk_4` FOREIGN KEY (`venue`) REFERENCES `venue` (`id`),
  CONSTRAINT `quotation_ibfk_5` FOREIGN KEY (`structure`) REFERENCES `structure` (`id`),
  CONSTRAINT `quotation_ibfk_6` FOREIGN KEY (`service`) REFERENCES `service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quotation`
--

LOCK TABLES `quotation` WRITE;
/*!40000 ALTER TABLE `quotation` DISABLE KEYS */;
INSERT INTO `quotation` VALUES (1,1,1,1,1,1,1,1,0,1,'2022-10-01 14:00:00','2022-10-01 22:00:00',1),(2,2,2,2,2,2,2,0,1,0,'2022-11-01 10:00:00','2022-11-01 18:00:00',NULL),(3,3,3,3,3,3,3,1,1,1,'2022-12-01 12:00:00','2022-12-01 20:00:00',NULL);
/*!40000 ALTER TABLE `quotation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-21 16:58:11
