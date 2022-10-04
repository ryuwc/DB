CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo
VALUES 
  ('dolphin', 'carnivore', 210, NULL, 3),
  ('pig', 'omnivore', 70, 45, 5),
  ('panda', 'herbivore', 80, 90, 2),
  ('dog', 'omnivore', 8, 20, 1),
  ('elephant', 'herbivore', 3800, 280, 10),
  ('tiger', 'carnivore', 220, 280, 10),
  ('gorilla', 'omnivore', 215, 180, 5);
  
INSERT INTO zoo (name, eat, weight, height)
VALUES
  ('rabbit', 'herbivore', 3, 150),
  ('eagle', 'carnivore', 8, 75),
  ('alligator', 'carnivore', 250, 50);

SELECT * FROM zoo;

UPDATE zoo
SET height = 15
WHERE name = 'rabbit';

SELECT name, height FROM zoo
WHERE name LIKE '%rabbit%';

DELETE FROM zoo
WHERE eat like '%omnivore%';

SELECT * FROM zoo;
