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
-- Table `spoverwaltung`.`person`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `spoverwaltung`.`person` ;

CREATE TABLE IF NOT EXISTS `spoverwaltung`.`person` (
  `id` INT NOT NULL,
  `creationdate` DATETIME NOT NULL,
  `firstname` VARCHAR(45) NOT NULL,
  `lastname` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `person_hash` BIGINT NOT NULL,
  PRIMARY KEY (`id`, `person_hash`))
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
  `outcome` VARCHAR(200) NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  `ects` INT NOT NULL,
  `edvnr` VARCHAR(45) NOT NULL,
  `workload` VARCHAR(200) NOT NULL,
  `module_hash` BIGINT NOT NULL,
  `instructor_id` INT NOT NULL,
  `instructor_hash` BIGINT NOT NULL,
  PRIMARY KEY (`id`, `module_hash`),
  INDEX `fk_module_person1_idx` (`instructor_id` ASC, `instructor_hash` ASC) VISIBLE,
  CONSTRAINT `fk_module_person1`
    FOREIGN KEY (`instructor_id` , `instructor_hash`)
    REFERENCES `spoverwaltung`.`person` (`id` , `person_hash`))
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
  `description` VARCHAR(600) NOT NULL,
  `sws` INT NOT NULL,
  `ects` INT NOT NULL,
  `edvnr` VARCHAR(45) NOT NULL,
  `workload` VARCHAR(600) NOT NULL,
  `modulepart_hash` BIGINT NOT NULL,
  `professor_id` INT NOT NULL,
  `professor_hash` BIGINT NOT NULL,
  `module_id` INT NOT NULL,
  `module_hash` BIGINT NOT NULL,
  PRIMARY KEY (`id`, `modulepart_hash`, `professor_id`, `professor_hash`, `module_id`, `module_hash`),
  INDEX `fk_modulepart_person1_idx` (`professor_id` ASC, `professor_hash` ASC) VISIBLE,
  INDEX `fk_modulepart_module1_idx` (`module_id` ASC, `module_hash` ASC) VISIBLE,
  CONSTRAINT `fk_modulepart_module1`
    FOREIGN KEY (`module_id` , `module_hash`)
    REFERENCES `spoverwaltung`.`module` (`id` , `module_hash`),
  CONSTRAINT `fk_modulepart_person1`
    FOREIGN KEY (`professor_id` , `professor_hash`)
    REFERENCES `spoverwaltung`.`person` (`id` , `person_hash`))
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
  `semester_hash` BIGINT NOT NULL,
  PRIMARY KEY (`id`, `semester_hash`))
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
  `studycourse_hash` BIGINT NOT NULL,
  PRIMARY KEY (`id`, `studycourse_hash`))
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
  `spo_hash` BIGINT NOT NULL,
  `studycourse_id` INT NOT NULL,
  `studycourse_hash` BIGINT NOT NULL,
  PRIMARY KEY (`id`, `spo_hash`, `studycourse_id`, `studycourse_hash`),
  INDEX `fk_spo_studycourse1_idx` (`studycourse_id` ASC, `studycourse_hash` ASC) VISIBLE,
  CONSTRAINT `fk_spo_studycourse1`
    FOREIGN KEY (`studycourse_id` , `studycourse_hash`)
    REFERENCES `spoverwaltung`.`studycourse` (`id` , `studycourse_hash`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `spoverwaltung`.`spocomposition`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `spoverwaltung`.`spocomposition` ;

CREATE TABLE IF NOT EXISTS `spoverwaltung`.`spocomposition` (
  `id` INT NOT NULL,
  `module_id` INT NOT NULL,
  `module_hash` BIGINT NOT NULL,
  `spo_id` INT NOT NULL,
  `spo_hash` BIGINT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_module_has_spo_spo1_idx` (`spo_id` ASC, `spo_hash` ASC) VISIBLE,
  INDEX `fk_module_has_spo_module1_idx` (`module_id` ASC, `module_hash` ASC) VISIBLE,
  CONSTRAINT `fk_module_has_spo_module1`
    FOREIGN KEY (`module_id` , `module_hash`)
    REFERENCES `spoverwaltung`.`module` (`id` , `module_hash`),
  CONSTRAINT `fk_module_has_spo_spo1`
    FOREIGN KEY (`spo_id` , `spo_hash`)
    REFERENCES `spoverwaltung`.`spo` (`id` , `spo_hash`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `spoverwaltung`.`spovalidity`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `spoverwaltung`.`spovalidity` ;

CREATE TABLE IF NOT EXISTS `spoverwaltung`.`spovalidity` (
  `spo_id` INT NOT NULL,
  `spo_hash` BIGINT NOT NULL,
  `semester_id` INT NOT NULL,
  `semester_hash` BIGINT NOT NULL,
  `startsem` TINYINT(1) NOT NULL,
  `endsem` TINYINT(1) NOT NULL,
  PRIMARY KEY (`spo_id`, `spo_hash`, `semester_id`, `semester_hash`),
  INDEX `fk_spo_has_semester_semester1_idx` (`semester_id` ASC, `semester_hash` ASC) VISIBLE,
  INDEX `fk_spo_has_semester_spo1_idx` (`spo_id` ASC, `spo_hash` ASC) VISIBLE,
  CONSTRAINT `fk_spo_has_semester_semester1`
    FOREIGN KEY (`semester_id` , `semester_hash`)
    REFERENCES `spoverwaltung`.`semester` (`id` , `semester_hash`),
  CONSTRAINT `fk_spo_has_semester_spo1`
    FOREIGN KEY (`spo_id` , `spo_hash`)
    REFERENCES `spoverwaltung`.`spo` (`id` , `spo_hash`))
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
  PRIMARY KEY (`id`, `user_hash`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
