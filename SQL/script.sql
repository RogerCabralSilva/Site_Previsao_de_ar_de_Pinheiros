CREATE DATABASE projeto;

USE projeto;

CREATE TABLE usuario (
  id int AUTO_INCREMENT PRIMARY KEY;
  nome varchar(100) not null;
  email varchar(100) not null;
  senha varchar(16) not null
)