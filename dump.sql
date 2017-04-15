-- MySQL dump 10.13  Distrib 5.7.17, for Linux (x86_64)
--
-- Host: localhost    Database: DBMS_Project
-- ------------------------------------------------------
-- Server version	5.7.17-0ubuntu0.16.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Cargo`
--

DROP TABLE IF EXISTS `Cargo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Cargo` (
  `Category` varchar(45) NOT NULL,
  `Weight` int(11) NOT NULL,
  `Volume` int(11) NOT NULL,
  `Manufacturer` varchar(45) NOT NULL,
  `Packaging` varchar(45) NOT NULL,
  KEY `idManufacturer _idx` (`Manufacturer`),
  CONSTRAINT `fk_manufacturer_cargo` FOREIGN KEY (`Manufacturer`) REFERENCES `Manufacturer` (`idManufacturer`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cargo`
--

LOCK TABLES `Cargo` WRITE;
/*!40000 ALTER TABLE `Cargo` DISABLE KEYS */;
INSERT INTO `Cargo` VALUES ('Electric ',5,3,'USHA','Carton'),('Health',9,9,'Reckitt ','Soft Wool '),('Medicines',4,4,'Reckitt ','Soft Wool ');
/*!40000 ALTER TABLE `Cargo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Facility_Type`
--

DROP TABLE IF EXISTS `Facility_Type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Facility_Type` (
  `Type` varchar(45) NOT NULL,
  `location` varchar(45) NOT NULL,
  `Distance` int(11) NOT NULL,
  `Manufacturer` varchar(45) NOT NULL,
  KEY `idManufacturer _idx` (`Manufacturer`),
  CONSTRAINT `fk_manufacturer_facility` FOREIGN KEY (`Manufacturer`) REFERENCES `Manufacturer` (`idManufacturer`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Facility_Type`
--

LOCK TABLES `Facility_Type` WRITE;
/*!40000 ALTER TABLE `Facility_Type` DISABLE KEYS */;
INSERT INTO `Facility_Type` VALUES ('Factory','Sitarganj',48,'Reckitt '),('Wharehouse','Bilaspur',83,'USHA '),('Factory','Mohan',48,'Apollo International'),('Factory','Oakhla',49,'Apollo International'),('Factory','Factory',34,'Apollo International');
/*!40000 ALTER TABLE `Facility_Type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Manufacturer`
--

DROP TABLE IF EXISTS `Manufacturer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Manufacturer` (
  `idManufacturer` varchar(45) NOT NULL,
  `Transport` varchar(45) NOT NULL,
  `Tracking` varchar(45) NOT NULL,
  `Loading` varchar(45) NOT NULL,
  `Delivery_Days` int(11) NOT NULL,
  `Packaging` varchar(45) NOT NULL,
  PRIMARY KEY (`idManufacturer`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Manufacturer`
--

LOCK TABLES `Manufacturer` WRITE;
/*!40000 ALTER TABLE `Manufacturer` DISABLE KEYS */;
INSERT INTO `Manufacturer` VALUES ('Apollo International','Truck','No','Manual',2,'Carton Boxes'),('Reckitt ','Truck','Yes','Overhaul Crane ',6,'Pallet '),('USHA ','Truck ','Yes','Forklift',8,'Boxes');
/*!40000 ALTER TABLE `Manufacturer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Rating`
--

DROP TABLE IF EXISTS `Rating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Rating` (
  `Rating` int(11) NOT NULL,
  `Transporter` varchar(45) NOT NULL,
  `Manufacturer` varchar(45) NOT NULL,
  KEY `idTransporter _idx` (`Transporter`),
  CONSTRAINT `fk_transporter_rating` FOREIGN KEY (`Transporter`) REFERENCES `Transporter` (`idTransporter`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Rating`
--

LOCK TABLES `Rating` WRITE;
/*!40000 ALTER TABLE `Rating` DISABLE KEYS */;
/*!40000 ALTER TABLE `Rating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Shipment_Details`
--

DROP TABLE IF EXISTS `Shipment_Details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Shipment_Details` (
  `Transporter` varchar(45) NOT NULL,
  `Cargo_Weight` int(11) NOT NULL,
  `Freight` int(11) NOT NULL,
  `Loading_Type` varchar(45) NOT NULL,
  `Cargo_Details` varchar(45) NOT NULL,
  `Dispatch_Month` int(11) NOT NULL,
  KEY `idTransporter_idx` (`Transporter`),
  CONSTRAINT `fk_transporter_shipment` FOREIGN KEY (`Transporter`) REFERENCES `Transporter` (`idTransporter`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Shipment_Details`
--

LOCK TABLES `Shipment_Details` WRITE;
/*!40000 ALTER TABLE `Shipment_Details` DISABLE KEYS */;
INSERT INTO `Shipment_Details` VALUES ('Om Logistic',34,28,'Manual ','Electronic',250),('Om Logistic',56,45,'ForkLift','Electronic Goods ',300),('Om Logistic',30,23,'Drive In','Healtcare',400),('TCI XPS',37,27,'Manual ','Medicine ',500),('Varuna',50,44,'Forklift','Electronic',350),('Varuna',60,44,'Forklift','Electronic',500);
/*!40000 ALTER TABLE `Shipment_Details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Transporter`
--

DROP TABLE IF EXISTS `Transporter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Transporter` (
  `idTransporter` varchar(45) NOT NULL,
  `Theft` int(11) NOT NULL,
  `Delay` int(11) NOT NULL,
  `Damages` int(11) NOT NULL,
  PRIMARY KEY (`idTransporter`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transporter`
--

LOCK TABLES `Transporter` WRITE;
/*!40000 ALTER TABLE `Transporter` DISABLE KEYS */;
INSERT INTO `Transporter` VALUES ('Om Logistic',1,1,3),('TCI XPS',2,2,2),('Varuna',2,2,1),('VRL',1,1,1);
/*!40000 ALTER TABLE `Transporter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Truck`
--

DROP TABLE IF EXISTS `Truck`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Truck` (
  `Manufacturer` varchar(45) NOT NULL,
  `Type` varchar(45) NOT NULL,
  `Dimension` int(11) NOT NULL,
  `Freigth_Cost` int(11) NOT NULL,
  KEY `idManufacturer _idx` (`Manufacturer`),
  CONSTRAINT `fk_manufacturer_truck` FOREIGN KEY (`Manufacturer`) REFERENCES `Manufacturer` (`idManufacturer`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Truck`
--

LOCK TABLES `Truck` WRITE;
/*!40000 ALTER TABLE `Truck` DISABLE KEYS */;
INSERT INTO `Truck` VALUES ('USHA','24',23,46200),('USHA','43',34,45666),('Reckitt','45',32,343455);
/*!40000 ALTER TABLE `Truck` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-15 16:46:03
