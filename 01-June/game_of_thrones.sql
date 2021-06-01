-- Create tables
-- Insert data
-- get data tables

-- Create tables

CREATE TABLE character (
       id integer primary key,
       name text NOT NULL,
       gender varchar(1),
       nickname text,
       aff_id integer references(affiliation.id) -- foreign key
);

-- Insert data

INSERT INTO character(name, gender, aff_id) values ("Eddard Stark", "m", 4);
insert into character(name, gender, aff_id) values ("Jaime", "m", 1);
insert into character(name, gender, aff_id) values ("Cersei", "f", 1);
insert into character(name, gender, nickname, aff_id) values ("Sandor Clegane", "m", "The Hound", 4);
insert into character(name, gender, nickname, aff_id) values ("Petyr Baelish", "m", "Littlefinger", 1);

-- Updating row
update character set name = "cersei" where id=3;


-- Get data from table
select name from character;

create table affiliation (
       id integer primary key,
       name text not null,
       location text not null
);

insert into affiliation(name, location) values ("Stark", "Winterfell");
insert into affiliation(name, location) values ("Lannister", "Kings Landing");
insert into affiliation(name, location) values ("Nights Watch", "Wall");
insert into affiliation(name, location) values ("Targaryen", "Dragonstone");


select c.name, c.gender, a.name  from character c, affiliation a where c.aff_id = a.id and a.location = "Winterfell";

