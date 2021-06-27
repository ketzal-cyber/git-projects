/*
Sentencias basicas SQL en oracleDB
 */
DROP TABLE usuario;

CREATE TABLE usuario(
	ID_USUARIO number(30) not null,
	nombre varchar2(150) not null,
	CONSTRAINT primary_usuario PRIMARY KEY(id_usuario)
);
