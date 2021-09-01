-- creates a tables users with certain requirements
-- id, integer, never null, auto increment and primary key
--  email, string (255 characters), never null and unique
--  name, string (255 characters)

CREATE TABLE IF NOT EXISTS `users` (
`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
`email` VARCHAR(255) NOT NULL UNIQUE,
`name` varchar(255)
);
