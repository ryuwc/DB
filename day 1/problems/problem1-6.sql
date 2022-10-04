CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

-- 1) 
-- INSERT INTO zoo VALUES 
-- (5, 180, 210, 'gorilla', 'omnivore');

-- 1) sol 
-- 데이터를 저장할 때 순서가 꼬였다.
INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 5, 180, 210);


-- 2)
-- INSERT INTO zoo (rowid, name, eat, weight, age) VALUES
-- (10,'dolphin', 'carnivore', 210, 3),
-- (10, 'alligator', 'carnivore', 250, 50);

-- 2) sol
-- rowid는 고유의 값을 갖는다, 중복으로 넣었다.


-- 3)
-- INSERT INTO zoo (name, eat, age) VALUES
-- ('dolphin', 'carnivore', 3);

-- 3) sol
-- weight는 필수 값인데 넣지 않았다.
