-- list all cities of california in cureent db 
-- results sorted by cities.id in ascending order
SELECT `id`, `name` FROM `cities` WHERE `state_id` = (SELECT `id` FROM `states` WHERE `name` = "California") ORDER BY `id` ASC;
