-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema swizzle_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `swizzle_schema` ;

-- -----------------------------------------------------
-- Schema swizzle_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `swizzle_schema` DEFAULT CHARACTER SET utf8 ;
USE `swizzle_schema` ;

-- -----------------------------------------------------
-- Table `swizzle_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `swizzle_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(60) NULL,
  `email` VARCHAR(60) NULL,
  `password` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `swizzle_schema`.`saved_drinks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `swizzle_schema`.`saved_drinks` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `drink_name` VARCHAR(60) NULL,
  `instructions` MULTILINESTRING NULL,
  `ingredient1` VARCHAR(45) NULL,
  `ingredient2` VARCHAR(45) NULL,
  `ingredient3` VARCHAR(45) NULL,
  `ingredient4` VARCHAR(45) NULL,
  `ingredient5` VARCHAR(45) NULL,
  `measurement1` VARCHAR(45) NULL,
  `measurement2` VARCHAR(45) NULL,
  `measurement3` VARCHAR(45) NULL,
  `measurement4` VARCHAR(45) NULL,
  `measurement5` VARCHAR(45) NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_saved_drinks_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_saved_drinks_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `swizzle_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
