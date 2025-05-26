-- Step 1: Create database
CREATE DATABASE IF NOT EXISTS employee_management;
USE employee_management;

-- Step 2: Create Departments table
CREATE TABLE IF NOT EXISTS departments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100)
);

-- Step 3: Create Employees table
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    position VARCHAR(50),
    department_id INT,
    hire_date DATE,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

-- Step 4: Create Salaries table
CREATE TABLE IF NOT EXISTS salaries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    amount DECIMAL(10,2),
    pay_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- Step 5: Insert departments
INSERT INTO departments (name, location) VALUES
('Human Resources', 'New York'),
('Engineering', 'San Francisco'),
('Finance', 'Chicago'),
('Marketing', 'Boston');

-- Step 6: Insert employees
INSERT INTO employees (name, email, position, department_id, hire_date) VALUES
('Alice Johnson', 'alice.johnson@example.com', 'HR Manager', 1, '2021-03-01'),
('Bob Smith', 'bob.smith@example.com', 'Software Engineer', 2, '2022-01-10'),
('Carol Lee', 'carol.lee@example.com', 'Accountant', 3, '2020-07-15'),
('David Kim', 'david.kim@example.com', 'Marketing Lead', 4, '2019-11-20'),
('Eve Turner', 'eve.turner@example.com', 'DevOps Engineer', 2, '2023-02-05');

-- Step 7: Insert salaries
INSERT INTO salaries (employee_id, amount, pay_date) VALUES
(1, 75000.00, '2024-12-01'),
(2, 95000.00, '2024-12-01'),
(3, 60000.00, '2024-12-01'),
(4, 70000.00, '2024-12-01'),
(5, 92000.00, '2024-12-01');
