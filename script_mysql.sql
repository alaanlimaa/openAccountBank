create database banks;

create table contas_bancarias (
n_numconta varchar(10) primary key not null,
c_nometitular varchar(20),
n_numbanco smallint,
c_nomebanco varchar(40),
n_atsaldo decimal(25, 2),
n_atlimite decimal(25, 2),
n_cpftitular varchar(11) not null unique,
n_opendate datetime default current_timestamp);

select * from contas_bancarias;



