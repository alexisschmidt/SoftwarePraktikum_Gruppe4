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

-- -----------------------------------------------------
-- Schema spoverwaltung
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `spoverwaltung` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `spoverwaltung` ;

-- -----------------------------------------------------
-- Table `spoverwaltung`.`person`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `spoverwaltung`.`person` ;

CREATE TABLE IF NOT EXISTS `spoverwaltung`.`person` (
  `id` INT NOT NULL,
  `creationdate` DATETIME NOT NULL,
  `firstname` VARCHAR(45) NOT NULL,
  `lastname` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `person_hash` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
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
  `name` VARCHAR(45) NOT NULL,
  `title` VARCHAR(45) NOT NULL,
  `requirement` VARCHAR(45) NULL DEFAULT NULL,
  `examtype` VARCHAR(45) NOT NULL,
  `instructor` INT NOT NULL,
  `outcome` VARCHAR(45) NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  `ects` INT NOT NULL,
  `edvnr` VARCHAR(45) NOT NULL,
  `workload` VARCHAR(45) NOT NULL,
  `module_hash` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `instructor_idx` (`instructor` ASC) VISIBLE,
  CONSTRAINT `instructor`
    FOREIGN KEY (`instructor`)
    REFERENCES `spoverwaltung`.`person` (`id`))
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
  `name` VARCHAR(45) NOT NULL,
  `title` VARCHAR(45) NOT NULL,
  `language` VARCHAR(45) NOT NULL,
  `literature` VARCHAR(45) NULL DEFAULT NULL,
  `semester` INT NOT NULL,
  `sources` VARCHAR(45) NULL DEFAULT NULL,
  `connection` VARCHAR(600) NOT NULL,
  `description` VARCHAR(45) NOT NULL,
  `sws` VARCHAR(45) NOT NULL,
  `professor` INT NOT NULL,
  `module_id` INT NOT NULL,
  `ects` VARCHAR(45) NOT NULL,
  `edvnr` VARCHAR(45) NOT NULL,
  `workload` VARCHAR(45) NOT NULL,
  `modulepart_hash` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `professor_idx` (`professor` ASC) VISIBLE,
  INDEX `module_id_idx` (`module_id` ASC) VISIBLE,
  CONSTRAINT `module_id`
    FOREIGN KEY (`module_id`)
    REFERENCES `spoverwaltung`.`module` (`id`),
  CONSTRAINT `professor`
    FOREIGN KEY (`professor`)
    REFERENCES `spoverwaltung`.`person` (`id`))
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
  `name` VARCHAR(45) NOT NULL,
  `title` VARCHAR(45) NOT NULL,
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
  `name` VARCHAR(45) NOT NULL,
  `title` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
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
  `name` VARCHAR(45) NOT NULL,
  `title` VARCHAR(45) NOT NULL,
  `start_semester` INT NOT NULL,
  `end_semester` INT NULL DEFAULT NULL,
  `studycourse` INT NOT NULL,
  `spo_hash` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `studycourse_idx1` (`studycourse` ASC) VISIBLE,
  CONSTRAINT `studycourse`
    FOREIGN KEY (`studycourse`)
    REFERENCES `spoverwaltung`.`studycourse` (`id`))
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
  `user_hash` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
