DROP DATABASE animals_db;

CREATE DATABASE animals_db;

show databases;

USE animals_db;

CREATE TABLE people (
    id INTEGER(11) AUTO_INCREMENT NOT NULL,
    name VARCHAR(30) NOT NULL,
    has_pet BOOLEAN NOT NULL,
    pet_name VARCHAR(30),
    pet_age INTEGER(10),
    PRIMARY KEY (id)
);

INSERT INTO people (name, has_pet, pet_name, pet_age)
VALUES ("Jacob", true, "Misty", 10);

SELECT 
    *
FROM
    people;

-- --------------

DROP DATABASE favorite_db;

CREATE DATABASE favorite_db;

USE favorite_db;

CREATE TABLE favorite_foods (
    id INTEGER(11) AUTO_INCREMENT NOT NULL,
    food VARCHAR(50) NOT NULL,
    score INTEGER(10),
    PRIMARY KEY (id)
);

USE favorite_db;

CREATE TABLE favorite_songs (
    id INTEGER(11) AUTO_INCREMENT NOT NULL,
    song VARCHAR(100) NOT NULL,
    artist VARCHAR(50) NOT NULL,
    score INTEGER(10),
    PRIMARY KEY (id)
);

USE favorite_db;


CREATE TABLE favorite_movies (
    id INTEGER(11) AUTO_INCREMENT NOT NULL,
    film VARCHAR(100) NOT NULL,
    five_times BOOLEAN NOT NULL,
    score INTEGER(10),
    PRIMARY KEY (id)
);

INSERT INTO favorite_foods (food, score)
VALUES ("Pizza Pie!", 10); 

INSERT INTO favorite_foods (food, score)
VALUES("Taco Time!", 11);

INSERT INTO favorite_foods (food, score)
VALUES("Burgers", 7);
