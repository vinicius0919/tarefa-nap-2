create database fazenda;

use fazenda;

#drop database fazenda;

create table propriedade(
id int auto_increment primary key,
nome varchar(255) not null,
cnpj varchar(255),
endereco varchar(255)
);

#drop table propriedade;

create table bois(
id int auto_increment primary key,
peso float not null,
idPropriedade int not null,
constraint fk_constraint foreign key (idPropriedade) references propriedade(id) on delete cascade
);
#drop table bois;

insert into propriedade(nome) values ("fazenda 01");
insert into bois(peso, idPropriedade) values (400.6, 1);

SELECT * FROM propriedade;
select * from bois;

