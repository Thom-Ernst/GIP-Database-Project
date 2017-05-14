# GIP-Database-Project
A webapp quiz using Mysql, Python 2.7 and Flask

- - -

# Dependencies

## To get the code to work, follow these steps to ensure nothing is missing...

### Packages:

- python
- python-flask
- flaskext-mysql

### SQL Code:

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

### Paste these in your stored procedures:

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

### You will also require the user `imma` with admin privileges, the following python extract should give you enough information:

```python
app.config['MYSQL_DATABASE_USER'] = 'imma'
app.config['MYSQL_DATABASE_PASSWORD'] = 'imma'
app.config['MYSQL_DATABASE_DB'] = 'GIP-Schema'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
```

*Please note that in a real application, this code would never be published.*

### Finaly:
You will have to host the flask server... The most reliable way to do this, is navigate to the project directory with a terminal and type the following commands:

```bash
python -m fexport FLASK_APP=app.py
python -m flask run
```

- - -

# Oof!

## Now that we've got that over with, what's this app even about?

Glad you ask, this is the accumulation of me teaching python to myself, and our combined educational efforts at my school. The app uses Flask to run a server on which we can interact with the static html to play a little music quiz.
The website itself uses bootstrap, font-awesome and some custom css. It interacts with Jquery and Ajax, which in turn interacts with Python, which in turn interacts with the MySQL database.

I use a simple 1 to 1 database relation to make sessions on the app permanent. One table is to store the user's name so that it can be used in-game. The other is a scoreboard, which permanently keeps track of all previous contestants and their scores.
Feel free to take a look at my Entity Relation Diagram and my usecases:

![Insert image here](#)

![Insert image here](#)

I intend to play the music files using html5, but that will only happen after i've made all code compatible with the Flask framework.


*shoutouts to Bert Anthonissen and the Stackoverflow Community to help me in my dire times of need.*

All the code in the project was written by me, no code was literally copied over from any website.