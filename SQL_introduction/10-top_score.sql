-- Lists all records of the table second_table.
-- Records are ordered by descending score.
CREATE TABLE IF NOT EXISTS `second_table` (
    `id` INT,
    `name` VARCHAR(256),
    `score` INT
);

INSERT INTO `second_table` (`id`, `name`, `score`) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);

SELECT score, name FROM second_table ORDER BY score DESC;