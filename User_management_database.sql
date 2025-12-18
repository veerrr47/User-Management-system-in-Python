create database user_management;
use user_management;

create table users(
	id int auto_increment primary key,
    name varchar(100) not null,
    username varchar(50) unique not null,
    password varchar(100) not null,
    address varchar(200)
);

describe users;
