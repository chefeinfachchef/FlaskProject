create database if not exists Reise;
use Reise;

create table if not exists Reiseveranstalter (
	büroId int auto_increment unique key primary key,
	bundesland varchar (120),
	description text,
	telefonnummer integer,
	postleitzahl integer,
    Adresse varchar(120), 
    Büroname text,
    Stadt text);

SELECT name, Reiseveranstalter
FROM Reiseveranstalter, Reise
WHERE büroId = ReiseId


create table if not exists Reise (
	ReiseId int auto_increment unique key primary key,
    Kosten integer,
    Zielort text,
    Land text,
    Dauer time,
    Hotel integer);

SELECT name, Reise
FROM Reiseteilnehmer, Reise
WHERE ReisendeId = ReiseId

create table if not exists Reiseteilnehmer (
	ReisendeId int auto_increment unique key primary key,
    Vorname text,
    Nachname text,
    Adresse varchar(120),
    Bundesland text,
    Telefonnummer text);

create Table if not exists Zwischentabelle(
    ZwischenId int auto_increment unique key primary key);
    


