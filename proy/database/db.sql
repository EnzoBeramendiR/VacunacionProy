drop database db_proyecto;

create database db_proyecto;

use db_proyecto;


CREATE TABLE usuario(
id int(5) NOT NULL primary key auto_increment,
nomb varchar(30) NOT NULL,
pass varchar(8) unique,
func char(1) check (func ='P' or func ='D'),
lugar varchar(30) NOT NULL,
distri varchar(50) NOT NULL,
edad varchar(5) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;


insert into usuario(nomb,pass,func,lugar,distri,edad)
values ('Jose Paredes','54595229','D','LugarA','Miraflores','54');

insert into usuario(nomb,pass,func,lugar,distri,edad)
values ('Alberto Campos','21150423','D','LugarB','Surco','45');

insert into usuario(nomb,pass,func,lugar,distri,edad)
values ('Nicolas Gutierrez','39112043','D','LugarC','San Isidro','56');

insert into usuario(nomb,pass,func,lugar,distri,edad)
values ('Jaime Castro','91842478','P','LugarA','La Molina','34');

insert into usuario(nomb,pass,func,lugar,distri,edad)
values ('Gonzalo Quiñonez','50898060','P','LugarA','San Borja','27');

insert into usuario(nomb,pass,func,lugar,distri,edad)
values ('Alejandra Perez','34815361','P','LugarA','Surquillo','34');

insert into usuario(nomb,pass,func,lugar,distri,edad)
values ('Josefa Cervantes','38836580','P','LugarA','Ancon','47');

insert into usuario(nomb,pass,func,lugar,distri,edad)
values ('Arnulfo Osorio','38836580','P','LugarB','Barranco','54');

insert into usuario(nomb,pass,func,lugar,distri,edad)
values ('Bartolome Ponce','14223156','P','LugarB','Ate Vitarte','38');

insert into usuario(nomb,pass,func,lugar,distri,edad)
values ('Lidia Mendez','44332564','P','LugarB','Chorrillos','28');

insert into usuario(nomb,pass,func,lugar,distri,edad)
values ('Violeta Gomez','63576408','P','LugarB','Pueblo Libre','49');

insert into usuario(nomb,pass,func,lugar,distri,edad)
values ('Alvaro Solano','34889914','P','LugarC','San Luis','65');

insert into usuario(nomb,pass,func,lugar,distri,edad)
values ('Gloria Castellano','29651841','P','LugarC','Lurigancho','56');

insert into usuario(nomb,pass,func,lugar,distri,edad)
values ('Esteban Girado','41431451','P','LugarC','Lurin','94');
