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
-- Table `spoverwaltung`.`examtype`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `spoverwaltung`.`examtype` ;

CREATE TABLE IF NOT EXISTS `spoverwaltung`.`examtype` (
  `id` INT NOT NULL,
  `creationdate` DATETIME NOT NULL,
  `createdby` BIGINT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `title` VARCHAR(45) NOT NULL,
  `examtype_hash` BIGINT NOT NULL,
  PRIMARY KEY (`examtype_hash`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


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
  `outcome` VARCHAR(2000) NOT NULL,
  `ects` INT NOT NULL,
  `edvnr` INT NOT NULL,
  `workload` VARCHAR(2000) NOT NULL,
  `module_hash` BIGINT NOT NULL,
  `moduletype_hash` BIGINT NOT NULL,
  `examtype_hash` BIGINT NOT NULL,
  `instructor_hash` BIGINT NOT NULL,
  PRIMARY KEY (`module_hash`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


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
  `edvnr` INT NOT NULL,
  `workload` VARCHAR(2000) NOT NULL,
  `modulepart_hash` BIGINT NOT NULL,
  `professor_hash` BIGINT NOT NULL,
  `module_hash` BIGINT NOT NULL,
  PRIMARY KEY (`modulepart_hash`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `spoverwaltung`.`moduletype`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `spoverwaltung`.`moduletype` ;

CREATE TABLE IF NOT EXISTS `spoverwaltung`.`moduletype` (
  `id` INT NOT NULL,
  `creationdate` DATETIME NOT NULL,
  `createdby` BIGINT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `title` VARCHAR(45) NOT NULL,
  `moduletype_hash` BIGINT NOT NULL,
  PRIMARY KEY (`moduletype_hash`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


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
  `examtype_hash` BIGINT NOT NULL,
  PRIMARY KEY (`examtype_hash`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `spoverwaltung`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `spoverwaltung`.`user` ;

CREATE TABLE IF NOT EXISTS `spoverwaltung`.`user` (
  `id` INT NOT NULL,
  `creationdate` DATETIME NOT NULL,
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
