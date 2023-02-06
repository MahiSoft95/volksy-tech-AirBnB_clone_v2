-- create db and table in it
-- table id INT, state_id INT
-- id INT unique cant be null and is primary key
-- state_id INT cant be null must be a foreign key that references to id of the states table

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_od_usa.cities(
id INT AUTO_INCREMENT PRIMARY KEY,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id));
