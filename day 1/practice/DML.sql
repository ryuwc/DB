CREATE TABLE users (
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

-- 이름과 나이를 조회
SELECT first_name, age FROM users;

-- 전체 데이터를 조회
SELECT * FROM users;

-- rowid와 이름을 조회
SELECT rowid, first_name FROM users;

-- 이름과 나이를 나이가 어린 순으로 조회하기
SELECT first_name, age FROM users
ORDER BY age ASC;

-- 이름과 나이를 나이가 많은 순으로 조회하기
SELECT first_name, age FROM users
ORDER BY age DESC;

-- 이름, 나이, 계좌 잔고를 나이가 어린순으로,
-- 만약 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회하기
SELECT first_name, age, balance FROM users
ORDER BY age ASC, balance DESC;

-- 모든 지역 조회하기
SELECT country FROM users;

-- 중복 없이 모든 지역 조회하기
SELECT DISTINCT country FROM users;

-- 지역 순으로 내림차순 정렬하여 중복없이 모든 지역 조회하기
SELECT DISTINCT country FROM users
ORDER BY country;

-- 이름과 지역이 중복 없이 모든 이름과 지역 조회하기
SELECT DISTINCT first_name, country FROM users;

-- 이름과 지역 중복 없이 지역 순으로 내림차순 정렬하여 모든 이름과 지역 조회하기
SELECT DISTINCT first_name, country FROM users
ORDER BY country DESC;

-- 나이가 30살 이상인 사람들의 이름, 나이, 계좌 조회하기
SELECT first_name, age, balance FROM users
WHERE age >= 30;

-- 나이가 30살 이상이고 계좌 잔고가 50만원 초과인
-- 사람들의 이름, 나이, 계좌 조회하기
SELECT first_name, age, balance FROM users
WHERE age >= 30 AND balance > 500000;

-- 이름에 '호'가 포함되는 사람들의 이름과 성 조회하기
SELECT first_name, last_name FROM users
WHERE first_name LIKE '%호%';

-- 이름이 '준'으로 끝나는 사람들의 이름 조회하기
SELECT first_name, last_name FROM users
WHERE first_name LIKE '%준';

-- 서울 지역 전화번호를 가진 사람들의 이름과 전화번호 조회하기
SELECT first_name, phone FROM users
WHERE phone LIKE '02-%';

-- 나이가 20대인 사람들의 이름과 나이 조회하기
SELECT first_name, age FROM users
WHERE age LIKE '2_';

-- 전화번호 중간 4자리가 51로 시작하는 사람들의 이름과 전화번호 조회하기
SELECT first_name, phone FROM users
WHERE phone LIKE '%-51__-%';

-- 경기도 혹은 강원도에 사는 사람 이름과 지역 조회하기
SELECT first_name, country FROM users
WHERE country IN ('경기도', '강원도');

-- 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회하기
SELECT first_name, country FROM users
WHERE country NOT IN ('경기도', '강원도');

-- 나이가 20살 이상, 30살 이하인 사람들의 이름과 나이 조회하기
SELECT first_name, age FROM users
WHERE age BETWEEN 20 and 30;

-- 위의 반대
SELECT first_name, age FROM users
WHERE age NOT BETWEEN 20 and 30;

-- 첫 번째부터 열 번째 데이터까지 rowid와 이름 조회하기
SELECT rowid, first_name FROM users
LIMIT 10;

-- 계좌 잔고가 가장 많은 10명의 이름과 계좌 잔고 조회하기
SELECT first_name, balance FROM users
ORDER BY balance DESC LIMIT 10;

-- 나이가 가장 어린 5명으 이름과 나이 조회하기
SELECT first_name, age FROM users
ORDER BY age LIMIT 5;

-- 11~20 조회
SELECT rowid, first_name FROM users
LIMIT 10 OFFSET 10;

-- 각 지역별로 몇 명씩 살고 있는지 조회하기
SELECT country, count(*) FROM users
GROUP BY country;

-- users 테이블의 전체 행 수 조회하기
SELECT count(*) users;

-- 나이가 30살 이상인 사람들의 평균 나이 조회하기
SELECT AVG(age) FROM users 
WHERE age >= 30;

-- 각 성씨가 몇 명씩 있는지 조회하기
SELECT last_name, count(*) AS number_of_name FROM users
GROUP BY last_name;

-- create
CREATE TABLE classmates (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

-- 단일 행 삽입하기
INSERT INTO classmates
VALUES ('홍길동', 23, '서울');

-- 여러 행 삽입하기
INSERT INTO classmates
VALUES 
  ('박씨', 13, '서울'),
  ('김씨', 22, '대전');

INSERT INTO classmates
VALUES 
  ('김철수', 23, '경기'),
  ('이영미', 22, '강원'),
  ('박진성', 26, '전라'),
  ('최지수', 12, '충청'),
  ('정요한', 28, '경상');

-- 2번 데이터의 이름을 '김철수한무두루미', 주소를 '제주도'로 수정하기
UPDATE classmates
SET name='김철수한무두루미',
    address='제주도'
WHERE rowid = 2;

-- 5번 데이터 삭제하기
DELETE FROM classmates
WHERE rowid = 5;

SELECT rowid, * FROM classmates;

-- 이름에 '영'이 포함되는 데이터 삭제하기
DELETE FROM classmates
WHERE name LIKE '%영%';

-- 테이블의 모든 데이터 삭제하기
DELETE FROM classmates;