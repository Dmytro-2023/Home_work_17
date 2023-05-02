CREATE DATABASE my_database_2;


USE my_database_2;

CREATE TABLE employee (
  employee_id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  job_title VARCHAR(50),
  department_id INT,
  salary INT,
  city VARCHAR(50),
  PRIMARY KEY (employee_id)
);

INSERT INTO employee (first_name, last_name, job_title, department_id, salary, city)
VALUES
('John', 'Doe', 'Manager', 90, 100000, 'London'),
('Jane', 'Doe', 'Software Engineer', 90, 80000, 'New York'),
('Bob', 'Smith', 'Software Engineer', 60, 75000, 'London'),
('Alice', 'Johnson', 'QA Engineer', 60, 70000, 'San Francisco'),
('Tom', 'Williams', 'QA Engineer', 60, 65000, 'New York'),
('Sarah', 'Lee', 'Business Analyst', 30, 90000, 'San Francisco'),
('David', 'Brown', 'Business Analyst', 30, 85000, 'New York'),
('Emily', 'Davis', 'Marketing Manager', 20, 110000, 'London'),
('Kevin', 'Taylor', 'Marketing Specialist', 20, 70000, 'San Francisco'),
('Olivia', 'Wilson', 'Sales Manager', 10, 120000, 'New York'),
('Michael', 'Anderson', 'Sales Representative', 10, 60000, 'San Francisco');

SELECT COUNT(*) AS vacancies_available
FROM employee
WHERE department_id IS NULL;

SELECT COUNT(*) AS employees_count, AVG(salary) AS average_salary
FROM employee
WHERE department_id = 90;

SELECT job_title, COUNT(*) AS employees_count
FROM employee
GROUP BY job_title;

SELECT first_name, last_name, department_id
FROM employee;

SELECT first_name, last_name, job_title, department_id
FROM employee
WHERE city = 'London';
