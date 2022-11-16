create database if not exists phoneDB;
use phoneDB;
create table if not exists contacts(
    id int not null auto_increment primary key,
    phone varchar(11),
    address varchar(50)
)