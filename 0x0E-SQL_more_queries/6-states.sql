-- This script creates the database hbtn_0d_usa and
-- the table states (in the database hbtn_0d_usa) on your MySQL server.

-- Creates database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use database
USE hbtn_0d_usa;

-- Creates table
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
