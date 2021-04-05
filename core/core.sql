CREATE DATABASE IF NOT EXISTS pokupka_biletov;
use pokupka_biletov;
DROP TABLE  IF EXISTS билет;
DROP TABLE  IF EXISTS сеанс;
DROP TABLE  IF EXISTS зал;
DROP TABLE  IF EXISTS кинотеатр;
DROP TABLE  IF EXISTS режисер_фильма;
DROP TABLE  IF EXISTS кинодиетели_в_фильме;
DROP TABLE  IF EXISTS кинодиетели;
DROP TABLE  IF EXISTS рецензия;
DROP TABLE  IF EXISTS фильм;
DROP TABLE  IF EXISTS пользователь;




CREATE TABLE IF NOT EXISTS пользователь (
    пароль VARCHAR(20) NOT NULL,
    логин VARCHAR(20) NOT NULL UNIQUE,
    город VARCHAR(20),
    PRIMARY KEY (логин)
);


CREATE TABLE IF NOT EXISTS фильм (
    название VARCHAR(20) NOT NULL UNIQUE,
    дата_выпуска DATE,
    страна VARCHAR(20),
    хронометраж int(10),
    жанр VARCHAR(20),
    imax_flg int(1),
    3d_flg int(1),

    PRIMARY KEY (название)

);

CREATE TABLE IF NOT EXISTS рецензия (
    rec_id int(5) NOT NULL AUTO_INCREMENT,
    название_фильма VARCHAR(20) NOT NULL,
    логин_пользователя VARCHAR(20) NOT NULL,
    текст VARCHAR(600),
    оценка int(2),
    PRIMARY KEY (rec_id),
    FOREIGN KEY (название_фильма)
        REFERENCES фильм (название),
    FOREIGN KEY (логин_пользователя)
        REFERENCES пользователь (логин)
);






CREATE TABLE IF NOT EXISTS кинодиетели(
    kinodeyatel_id int(5) NOT NULL UNIQUE AUTO_INCREMENT,
    ФИО VARCHAR(30) NOT NULL,
    дата_рождения DATE,
    страна VARCHAR(20),
    PRIMARY KEY (kinodeyatel_id)


);


CREATE TABLE IF NOT EXISTS кинодиетели_в_фильме (
    kinodeyatel_filma_id int(5) NOT NULL UNIQUE AUTO_INCREMENT,
    название_фильма VARCHAR(20) NOT NULL,
    kinodeyatel_id int(5) NOT NULL ,
    функция_в_фильме VARCHAR(20),
    PRIMARY KEY (kinodeyatel_filma_id),
    FOREIGN KEY (название_фильма)
        REFERENCES фильм (название),
    FOREIGN KEY (kinodeyatel_id)
        REFERENCES кинодиетели (kinodeyatel_id)
);


CREATE TABLE IF NOT EXISTS режисер_фильма (
    rej_filma_id int(5) NOT NULL UNIQUE AUTO_INCREMENT,
    название_фильма VARCHAR(20) NOT NULL,
    kinodeyatel_id int(5) NOT NULL,
    PRIMARY KEY (rej_filma_id),
    FOREIGN KEY (название_фильма)
        REFERENCES фильм (название),
    FOREIGN KEY (kinodeyatel_id)
        REFERENCES кинодиетели (kinodeyatel_id)
);



CREATE TABLE IF NOT EXISTS кинотеатр (
    название VARCHAR(20) NOT NULL UNIQUE,
    город VARCHAR(20) NOT NULL,
    адрес VARCHAR(50) NOT NULL,
    PRIMARY KEY (название)

);

CREATE TABLE IF NOT EXISTS зал (
    zal_id int(5) NOT NULL AUTO_INCREMENT,
    колличество_рядов int(2) NOT NULL,
    колличество_мест_в_ряде int(2) NOT NULL,
    imax_flg int(1),
    3d_flg int(1),
    название_кинотеатра VARCHAR(20) NOT NULL,
    PRIMARY KEY (zal_id),
    FOREIGN KEY (название_кинотеатра) 
        REFERENCES кинотеатр (название)
);

CREATE TABLE IF NOT EXISTS сеанс (
    seans_id int(5) NOT NULL AUTO_INCREMENT,
    название_фильма VARCHAR(20) NOT NULL,
    zal_id int(5) NOT NULL,
    дата_сеанса DATE NOT NULL,
    imax_flg int(1) NOT NULL,
    3d_flg int(1) NOT NULL,
    цена int(5) NOT NULL,
    PRIMARY KEY (seans_id),
    FOREIGN KEY (название_фильма)
        REFERENCES фильм (название),
    FOREIGN KEY (zal_id)
        REFERENCES зал (zal_id)
    
);

CREATE TABLE IF NOT EXISTS билет (
    num int(5) NOT NULL AUTO_INCREMENT,
    seans_id int(5) NOT NULL,
    ряд int(3) not null,
    место int(3) not null,
    цена int(5) NOT NULL,
    логин_пользователя VARCHAR(20),
    PRIMARY KEY (num),
    FOREIGN KEY (seans_id)
        REFERENCES сеанс (seans_id),
    FOREIGN KEY (логин_пользователя)
        REFERENCES пользователь (логин)
    
);

select * from сеанс;





INSERT INTO пользователь VALUES
('000001', "Валерий", "Чита"),
('000010', "Ольга", "Москва"),
('000004', "Valera123", "Москва"),
('000009', "Олег", "Москва"),
('000007', "Варвара", "Москва"),
('000007', "Максим", "Чита"),
('000002', "Антон", "Чита"),
('000003', "Александр", "Чита"),
('000008', "Анна", "Москва"),
('000001',"Влад","Москва"),
('000006', "Елисей", "Москва");



INSERT INTO фильм VALUES
('Мстители', '2014-10-21', 'Америка', 100, 'Фантастика', 0, 0),
('Мстители1', '2015-08-19', 'Америка', 120, 'Фантастика', 0, 0),
('Мстители2', '2016-12-02', 'Америка', 130, 'Фантастика', 1, 0),
('Мстители3', '2017-11-23', 'Америка', 140, 'Фантастика', 1, 1),
('Мстители4', '2018-08-12', 'Америка', 150, 'Фантастика', 1, 1),
('Большой куш', '2000-05-28', 'Великобритания', 100, 'Боевик', 0, 0),
('Однажды в… Голливуде', '2019-04-05', 'Россия', 154, 'Комедия', 1, 1),
('Игра на понижение', '2015-01-22', 'Великобритания', 124, 'Драма', 1, 0);


INSERT INTO рецензия VALUES
(1, "Игра на понижение", "Елисей", 'Фильм очень хороший', 10),
(2, "Мстители4", "Влад", 'Фильм мне не понравился', 2),
(3, "Однажды в… Голливуде", "Анна", 'Огонь!!!', 10),
(4, "Мстители4", "Максим", 'Ничего так', 5), 
(5, 'Большой куш', "Максим", 'Отличный фильм', 10),
(6, 'Большой куш', "Антон", 'Неплохо', 8);




INSERT INTO кинодиетели VALUES
(1, "Гай Ричи", '1968-09-10', 'Великобритания'),
(2, 'Джосс Уидон', '1964-07-23', 'США'),
(3, 'Квентин Тарантино', '1963-03-27', 'США'),
(4, 'Адам Маккей', '1968-04-17', 'Великобритания'),
(5, 'Кристиан Бэйл', '1974-01-30', 'Великобритания'),
(6, 'Брэд Питт', '1963-12-18', 'Россия'),
(7, 'Марго Робби', '1990-09-02', 'Австралия');




INSERT INTO кинодиетели_в_фильме VALUES
(1, 'Большой куш', 1, 'Режисер'),
(2, "Мстители", 2, 'Режисер'),
(3, "Мстители2", 2, 'Режисер'),
(4, "Мстители3", 2, 'Режисер'),
(5, "Мстители4", 2, 'Режисер'),
(6, "Однажды в… Голливуде", 3, 'Режисер'),
(7, "Однажды в… Голливуде", 6, 'Актер'),
(8, "Однажды в… Голливуде", 7, 'Актер'),
(9, 'Игра на понижение',  4, 'Режисер'),
(10, "Игра на понижение", 6, 'Актер'),
(11, "Игра на понижение", 7, 'Актер');






INSERT INTO режисер_фильма VALUES
(1, 'Большой куш', 1),
(2, "Мстители", 2),
(3, "Мстители2", 2),
(4, "Мстители3", 2),
(5, "Мстители4", 2),
(6, "Однажды в… Голливуде", 3),
(7, 'Игра на понижение',  4);




INSERT INTO кинотеатр VALUES
("Центавр", "Чита", "Лермонтова, 48"),
("Аврора", "Москва", "Лермонтова, 48"),
("Каро", "Москва", "Лермонтова, 48"); 




INSERT INTO зал VALUES 
(1, 10, 10, 1, 1, 'Каро'),
(2, 20, 10, 1, 1, 'Каро'),
(3, 10, 8, 1, 0, 'Аврора'),
(4, 10, 10, 0, 1, 'Аврора'),
(5, 10, 10, 0, 0, 'Центавр'),
(6, 10, 10, 1, 1, 'Центавр');


select * from билет;