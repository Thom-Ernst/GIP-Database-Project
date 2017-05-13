# GIP-Database-Project
A quiz for html with a MySQL server and python-flask

## SQL Code:

```mysql
-- -----------------------------------------------------
-- Table `GIP-Schema`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `GIP-Schema`.`user` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `lastname` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;
-- -----------------------------------------------------
-- Table `GIP-Schema`.`comment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `GIP-Schema`.`scoreboard` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `score` INT(11) NOT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

```

## Paste these in your stored procedures:

```mysql
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    IN p_name VARCHAR(45),
    IN p_lastname VARCHAR(45)
)
BEGIN
        insert into user
        (
            name,
            lastname
        )
        values
        (
            p_name,
            p_lastname
        );
END;
```

and

```mysql
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createScoreEntry`(
    IN p_score INT(11),
    IN p_user_id INT(11)
)
BEGIN
        insert into scoreboard
        (
            score,
            user_id
        )
        values
        (
            p_score,
            p_user_id
        );
END;
```