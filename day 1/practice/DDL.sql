CREATE TABLE contacts (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  email TEXT NOT NULL UNIQUE
);

-- 테이블 이름 바꾸기
ALTER TABLE contacts RENAME TO new_contacts;

-- 컬럼 이름 바꾸기
ALTER TABLE new_contacts RENAME COLUMN name TO last_name;

-- 새로운 컬럼 추가하기
ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL;

-- 컬럼 삭제하기
ALTER TABLE new_contacts DROP COLUMN address;

-- 테이블 삭제하기
DROP TABLE new_contacts;

