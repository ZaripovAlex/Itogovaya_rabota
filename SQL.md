## Cоздание таблиц:

CREATE TABLE home_animals ( id INT PRIMARY KEY AUTO_INCREMENT, type VARCHAR(30), name VARCHAR(30), command VARCHAR(30), birthday DATE );

CREATE TABLE farm_animals ( id INT PRIMARY KEY AUTO_INCREMENT, type VARCHAR(30), name VARCHAR(30), command VARCHAR(30), birthday DATE );

## Добавление данных в таблицу home_animals

INSERT INTO home_animals (type, name, command, birthday) VALUES ('Собака', 'Бим', 'Сидеть', 2022.04.03');

INSERT INTO home_animals (type, name, command, birthday) VALUES ('Кошка', 'Мурка', 'Есть', '2023.01.01');

INSERT INTO home_animals (type, name, command, birthday) VALUES > ('Хомяк', 'Хома', 'Бегать в шаре', '2023.01.02');

## Добавление данных в таблицу farm_animals
INSERT INTO farm_animals (type, name, command, birthday) VALUES ('Лошадь', 'Боливар', 'Скакать', '2010.01.01');

INSERT INTO farm_animals (type, name, command, birthday) VALUES ('Верблюд', 'Махмуд', 'Лежать', '2015.01.01');

INSERT INTO farm_animals (type, name, command, birthday) VALUES ('Ослик', 'Иа', 'Терять хвост', '2017.01.01');

## Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой питомник на зимовку.

DELETE FROM farm_animals WHERE type = 'Верблюд';

## Создать новую таблицу “молодые животные” в которую попадут все животные старше 1 года, но младше 3 лет и в отдельном столбце с точностью до месяца подсчитать возраст животных в новой таблице

CREATE TABLE young_animals ( id INT PRIMARY KEY AUTO_INCREMENT, type VARCHAR(30), name VARCHAR(30), command VARCHAR(30), birthday DATE, months INT );

INSERT INTO young_animals (type, name, command, birthday, months) SELECT type, name, command, birthday, TIMESTAMPDIFF(MONTH, birthday, CURDATE()) AS months FROM ( SELECT * FROM home_animals UNION ALL SELECT * FROM farm_animals ) WHERE TIMESTAMPDIFF(YEAR, birthday, CURDATE()) > 1 AND TIMESTAMPDIFF(YEAR, birthday, CURDATE()) < 3;

## Объединить все таблицы в одну, при этом сохраняя поля, указывающие на прошлую принадлежность к старым таблицам.

CREATE TABLE animals ( id INT PRIMARY KEY AUTO_INCREMENT, type VARCHAR(30), name VARCHAR(30), command VARCHAR(30), birthday DATE, months INT, source VARCHAR(30) );

INSERT INTO animals (type, name, nommand, birthday, months, source) SELECT type, name, command, birthday, TIMESTAMPDIFF(MONTH, birthday, CURDATE()), 'home_animals' FROM home_animals UNION ALL SELECT type, name, command, birthday, TIMESTAMPDIFF(MONTH, birthday, CURDATE()), 'farm_animals' FROM farm_animals UNION ALL SELECT type, name, command, birthday, months, 'young_animals' FROM young_animals;
