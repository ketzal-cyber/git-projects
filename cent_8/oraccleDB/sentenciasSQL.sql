-- CREACION DE USUARIO EN EL GESTOR ORACLEDB
-- 	definición del tablespace para el usuario
-- 	tablespace temporal para administrar un espacio de memoria temporal
-- 	definicion para que pueda ocupar todo el espacio disponible apra trabajar
-- 		en produccion debe ser un valor especifico
create user agentdba identified by dbaora
  2  default tablespace system
  3  temporary tablespace temp
  4  quota unlimited on system;

-- PRIVILEGIOS DE USUARIO
-- 	otorgar privilegios de coneccion
--	creacon de tables dentro de db
-- 	crear vistas
--	crear y configurar procedimientos dentro de db
--	avalitar la creacionde  secuencias
--	privilegios de administrar tablas
grant create session to name_user;
grant create table to name_user;
grant create view to name_user;
grant create procedure to name_user;
grant create sequence to name_user;

grant all on nombreTabla to name_user;

-- REVOCACION DE ADMINISTRACION DE TABLA AL USUARIO
revoke all on nombretabla from name_user;

-- ELIMINACION DE USUARIO
drop user name_user cascade;

-- Creacion DE TABLA
create table usuario(
	idusuario int,
	nombre char(10),
	fecha_nacimiento date,
	telefono char(10),
	salario number(6,2)
);
 create table empleado(
	  2  id_empleado int not null,
	  3  nombre varchar2(20),
	  4  direccion varchar2(40),
	  5  id_documento varchar2(10),
	  6  sueldo number(6,2),
	  7  fecha_nac date
	  8  );

-- INSERT DATOS EN TABLA
insert into empleado values(001,'Ana','Av principal', '12345789',4000.00, to_date('10/02/1998','dd/mm/yyyy'));

-- OPERADORES DE COMPARAACION
-- 	=  !=  >  >= <  <=

-- OPERADORES ARITMETICOS
-- 	+  -   *   %
SELECT titulo, precio, cantidad, precio*cantidad from libros;
select titulo, precio, precio-(precio*0.1) from libros;

-- Concatenacion de registros
select titulo ||'_'|| autor from libros; -- junta los registros en una sola columna

-- ELIMINAR DATOS ESPECIFFICOS O TODOS
delete from empleado;
rollback;	-- recupera los registros borrados por delete
delete from empleado where nombre = 'Ana';	-- registros recuperables
-- vaciar tabla borrando espacio en disco
truncate table articulo;



-- Actualizar registros
update articulos set nombre = 'impresora' where  codigo = 8;


-- ejecutar script desde fichero 
sql> @/home/oracle/directory_services/oracledb/script_tabla.sql

-- Consultas con valores null con sentencia is null,  is not null
select * from medicamento where laboratorio is null -- me trae los registros con laboratorio null
select * from medicamento where precio is not null  -- me trae los registros que no sean null

-- 				FUNCIONES STRING EN ORACLE
select chr(100) from dual; 	-- devuelve la letra d
select ascii('d') from dual;	-- devuelve el valor 100

select concat('lindo','dia') from dual;	-- junta las dos palabras sin la coma

select initcap('linda tarde') from dual;	-- devuelve Linda Tarde solo las letras iniciales
select lower('BUEN DIA') from dual;	-- devuelve buen dia  en minuscula
select upper('buena tarde') from dual;	-- devuelve BUENA TARDE todas en mayusculas
select lpad('oracle',11,'abc') from dual; -- acompleta 11 caraceres con abc del lado izq de oracle
select rpad('oracle',12,'abc') from dual; -- acompleta 12 caraceres con abc del lado derecho de oracle
select ltrim('curso oracle', 'cur') from dual; -- devuelve so oracle
select rtrim('curso oracle', 'cle') from dual; -- devuelve curso ora
select trim('  oracle  ') from dual; -- corta espacios de derecha e izquierda devuelve 'oracle'
select replace('www.oracle.com','w','v' from dual; -- devualve 'vvv.oracle.com' remplaza w por v
select substr('www.oracle.com',1,10) from dual; -- devuelve 'www.oracle' solo los caracteres del 1 al 10
select substr('www.oracle.com',-13) from dual; -- devuelve de derecha a izquierda
select length('www.oracle.com') as cantidad from dual; -- devuelve la cantidad de caracteres 14
select instr('curso de oracle','so') from dual; -- devuelve de donde empieza 4
select translate('CURSO ORACLE','AOE','XYZ') from dual; -- REMPLAZA LOS CARACTERES AOE por XYZ


-- 				FUNCIONES MATEMATICAS EN ORACLE
-- Siempre retornan varoles numericos
select abs(50) from dual;  -- retorna el valor absoluto
select ceil(15.50) from dual;  -- retorna el redondeo hacia arriba
select floor(15.30) from dual;  -- retorna el valor redondeado hacia abajo
select mod(10,3) from dual;  -- retorna el residuo de la divicion
select power(2,3) from dual;  -- retorna exponenede de 2 a la 3
select round(123.456,2) from dual;  -- retorna el redondeo a 2 cifras despues del punto
	select round(123.456,1) from dual; -- 123.5
	select round(123.456) from dual; -- 123
select sing(-100) from dual; -- retorna si es negativo o positivo
select trunc(123.1234,3) from dual;  -- retorna la cifra con 3 valores decimales
select sqrt(9) from dual; -- retorna la raiz cuadrada del valor 9 que es 3
select round(sqrt(27)) from dual; -- retorna la raiz eliminando los decimales  resultado 5


-- 				FUNCIONES DATE EN ORACLE
-- Representa el formato de fechas en siglo, año mes el dia horas, minutos y segndos
select add_months(to_date('10/10/2020','dd/mm/yyyy'),5) from dual; -- suma 5 a 10 en meses
select add_months(to_date('10/10/2020','dd/mm/yyyy'),-5) from dual; -- resta 5 a 10 en meses
select last_day(to_date('10/02/2020','dd/mm/yyyy') from dual; -- retorna el ulimo dia del mes
select months_between(to_date('19/05/2020','dd/mm/yyyy'),to_date('19/08/2020','dd/mm/yyyy')) from dual; -- retorna el total de meses entre 05 y 08 => -3
select next_day(to_date('10/08/2020','dd/mm/yyyy'),'MONDAY') from dual; -- retorna la fecha del dia que se pasa LUNES proximo a la fecha establecida
select current_date from dual; -- retorna la fecha del dia presente
select sysdate from dual; -- retorna la fecha establaecida en el sistema
select current_timestamp from dual; -- retorna la fecha regional de nuestro equipo o sistema
select systimestamp from dual; -- retorna la fecha y hora de nuestro sistema
select to_char('10/10/2020') from dual; -- retorna la convercion de una fecha a tipo char

-- 				CLAUSULA ORDERBY
select * from articulos order by id_ariculos desc -- desc, asc
select * from articulos order by 4 desc  -- 4 = toma como base la columna 4

-- 				clausula AND,  OR,  NOT
select * from peliculas where actor='Tom Cruise' or actor='Richard Gere'; 
select * from peliculas where not actor='Daniel R';
-- 				CLAUSULA BETWEEN
select * from medicamentos where precio between 5 and 15;
-- 				OPERADOR IN
select * from medicamentos where laboratorio in ('Bayer','Bago'); -- incluye 
select * from medicamentos where laboratorio not in ('Bayer','Bago'); --excluye los valores
select * from medicamentos where cantidad in (10,200); -- trae solo registros con esos valores
select * from medicamentos where extract(year from fechavecimiento) in (2019,2020);
select * from medicamentos where extract(month from fechavencimiento) in (12,10);
-- 				OPERACIONES LIKE,  NOT LIKE
select * from empleados where nombre like '%Perez%';
select * from empleados where nombre not like '%Perez%'; -- excluye los Perez
-- 				FUNCION COUNT
select count(laboratorio) as cantidad from medicamentos;
-- 				FUNCIONES MAX, MIN, SUM y AVG
select max(sueldo) as 'Mayor sueldo' from empleado;
select min(sueldo) as 'Menor sueldo' from empleado;
select avg(sueldo) as 'Promedio sueldo' from empleado;
select sum(sueldo) as 'sumatoria de suedos' from empleado;
-- 				FUNCION GROUP BY
-- 				FUNCION HAVING
-- 				CLAUSULA DISTINCT

