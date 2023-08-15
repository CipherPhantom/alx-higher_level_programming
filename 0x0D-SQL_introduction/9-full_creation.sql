-- This script creates a table second_table in the database
-- hbtn_0c_0 in your MySQL server and add multiples rows.

-- Creates table.
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

-- Insert values into table.
INSERT INTO second_table VALUES (1, "John", 10);
INSERT INTO second_table VALUES (2, "Alex", 3);
INSERT INTO second_table VALUES (3, "Bob", 14);
INSERT INTO second_table VALUES (4, "George", 8);
