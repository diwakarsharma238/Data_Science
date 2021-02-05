CREATE DATABASE exercise;

USE exrecise;

# 1. Write a SQL statement to create a simple table countries including columns country_id,country_name and region_id.

CREATE TABLE countries (
	country_id varchar(4),
    country_name varchar(50),
    region_id varchar(4));
DESC countries;

# 2. Write a SQL statement to create a simple table countries including columns country_id,country_name and region_id which is already exists.
    
DROP TABLE countries;
CREATE TABLE IF NOT EXISTS countries (
	country_id varchar(4),
    country_name varchar(50),
    region_id varchar(4)); 
    
    DESC countries;

# 3. Write a SQL statement to create the structure of a table dup_countries similar to countries.

 
 CREATE TABLE dup_countries LIKE countries;   
 DESC dup_countries;
 
# 4. Write a SQL statement to create a duplicate copy of countries table including structure and data by name dup_countries.
DROP TABLE dup_countries;

CREATE TABLE dup_countries SELECT * FROM countries;
DESC dup_countries;

# 5. Write a SQL statement to create a table countries set a constraint NULL.

DROP TABLE countries;
CREATE TABLE IF NOT EXISTS countries (
	country_id varchar(4) NOT NULL,
    country_name varchar(50),
    region_id varchar(4));
    
DESC countries;

# 6. Write a SQL statement to create a table named jobs including columns job_id, job_title, min_salary, max_salary and check whether the max_salary amount exceeding the upper limit 25000.
CREATE TABLE jobs (
job_id int,
job_title varchar(50),
min_salary int,
max_salary int check(max_salary<25000));
DESC jobs;

#7. Write a SQL statement to create a table named countries including columns country_id, country_name and region_id and make sure that no countries except Italy, India and China will be entered in the table.

DROP TABLE countries;
CREATE TABLE IF NOT EXISTS countries (
	country_id varchar(4),
    country_name varchar(50) CHECK(country_name IN('Italy','India','China')),
    region_id varchar(4));
    
    DESC countries;

# 8. Write a SQL statement to create a table named job_histry including columns employee_id, start_date, end_date, job_id and department_id and make sure that the value against column end_date will be entered at the time of insertion to the format like '--/--/----'.
DROP TABLE if exists job_history;   
CREATE TABLE job_history (
employee_id varchar(4),
start_date Date,
end_date Date check(end_date LIKE('--/--/----')),
job_id int,
department_id int);

SHOW CREATE TABLE job_history ;
desc job_history;


# 9. Write a SQL statement to create a table named countries including columns country_id,country_name and region_id and make sure that no duplicate data against column country_id will be allowed at the time of insertion.
DROP TABLE IF EXISTS countries;
CREATE TABLE countries (
	country_id varchar(4),
    country_name varchar(50),
    region_is varchar(4),
UNIQUE KEY (country_id));
    
SHOW CREATE TABLE countries; 

# 10. Write a SQL statement to create a table named jobs including columns job_id, job_title, min_salary and max_salary, and make sure that, the default value for job_title is blank and min_salary is 8000 and max_salary is NULL will be entered automatically at the time of insertion if no value assigned for the specified columns.

DROP TABLE IF EXISTS jobs;
CREATE TABLE jobs (
	job_id varchar(4),
    job_title varchar(50) DEFAULT '',
    min_salary int DEFAULT 8000,
    max_salary int DEFAULT NULL);
    
DESC jobs;

# 11. Write a SQL statement to create a table named countries including columns country_id, country_name and region_id and make sure that the country_id column will be a key field which will not contain any duplicate data at the time of insertion.

DROP TABLE IF EXISTS countries;
CREATE TABLE countries (
	country_id varchar(4),
    country_name varchar(50),
    region_id varchar(4),
    PRIMARY KEY (country_id)
    );
    
    desc countries;
    
# 12. Write a SQL statement to create a table countries including columns country_id, country_name and region_id and make sure that the column country_id will be unique and store an auto incremented value.

DROP TABLE IF EXISTS countries;
CREATE TABLE countries (
	country_id int auto_increment,
    country_name varchar(50),
    region_id varchar(4),
    UNIQUE KEY (country_id)
    );
    desc countries; 
    
# 13. Write a SQL statement to create a table countries including columns country_id, country_name and region_id and make sure that the combination of columns country_id and region_id will be unique.
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
	country_id int,
    country_name varchar(50),
    region_id varchar(4),
    PRIMARY KEY (country_id,region_id)
    );
    
# 14. Write a SQL statement to create a table job_history including columns employee_id, start_date, end_date, job_id and department_id and make sure that, the employee_id column does not contain any duplicate value at the time of insertion and the foreign key column job_id contain only those values which are exists in the jobs table.
DROP TABLE if exists job_history;   
DROP TABLE IF EXISTS jobs;

CREATE TABLE jobs (
	job_id int(4),
    job_title varchar(50) DEFAULT '',
    min_salary int DEFAULT 8000,
    max_salary int DEFAULT NULL,
    PRIMARY KEY (job_id)
    );
CREATE TABLE job_history (
employee_id varchar(4),
start_date Date,
end_date Date,
job_id int,
department_id int,
FOREIGN KEY (job_id) REFERENCES jobs (job_id)
);
DESC job_history;

# 15. Write a SQL statement to create a table employees including columns employee_id, first_name, last_name, email, phone_number hire_date, job_id, salary, commission, manager_id and department_id and make sure that, the employee_id column does not contain any duplicate value at the time of insertion and the foreign key columns combined by department_id and manager_id columns contain only those unique combination values, which combinations are exists in the departments table.

CREATE TABLE departments(
department_id decimal(4,0),
department_name varchar(30),
manager_id decimal(6,0),
location_id decimal(4,0),
PRIMARY KEY (department_id,manager_id)
);
desc departments;

DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
employee_id int UNIQUE,
first_name varchar(50),
last_name varchar(50),
email varchar(50),
phone_number varchar(50),
hire_date date,
job_id int,
salary int,
commission int,
manager_id decimal(6,0),
department_id decimal(4,0),
FOREIGN KEY (department_id,manager_id) REFERENCES departments (department_id,manager_id)
);

# 16. Write a SQL statement to create a table employees including columns employee_id, first_name, last_name, email, phone_number hire_date, job_id, salary, commission, manager_id and department_id and make sure that, the employee_id column does not contain any duplicate value at the time of insertion, and the foreign key column department_id, reference by the column department_id of departments table, can contain only those values which are exists in the departments table and another foreign key column job_id, referenced by the column job_id of jobs table, can contain only those values which are exists in the jobs table. The InnoDB Engine have been used to create the tables.
DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
employee_id int PRIMARY KEY,
first_name varchar(50),
last_name varchar(50),
email varchar(50),
phone_number varchar(50),
hire_date date,
job_id int,
salary int,
commission int,
manager_id decimal(6,0),
department_id decimal(4,0),
FOREIGN KEY (department_id) REFERENCES departments (department_id),
FOREIGN KEY (job_id) REFERENCES jobs (job_id)
) Engine =InnoDB;

desc employees;

# 17. Write a SQL statement to create a table employees including columns employee_id, first_name, last_name, job_id, salary and make sure that, the employee_id column does not contain any duplicate value at the time of insertion, and the foreign key column job_id, referenced by the column job_id of jobs table, can contain only those values which are exists in the jobs table. The InnoDB Engine have been used to create the tables. The specialty of the statement is that, The ON UPDATE CASCADE action allows you to perform cross-table update and ON DELETE RESTRICT action reject the deletion. The default action is ON DELETE RESTRICT.

DROP TABLE IF EXISTS jobs;
CREATE TABLE IF NOT EXISTS jobs ( 
JOB_ID integer NOT NULL UNIQUE PRIMARY KEY, 
JOB_TITLE varchar(35) NOT NULL DEFAULT ' ', 
MIN_SALARY decimal(6,0) DEFAULT 8000, 
MAX_SALARY decimal(6,0) DEFAULT NULL
)ENGINE=InnoDB;

DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
employee_id int PRIMARY KEY,
first_name varchar(50),
last_name varchar(50),
job_id int,
salary int,
FOREIGN KEY (job_id) REFERENCES jobs (job_id)
) Engine =InnoDB;

desc employees;

#18. Write a SQL statement to create a table employees including columns employee_id, first_name, last_name, job_id, salary and make sure that, the employee_id column does not contain any duplicate value at the time of insertion, and the foreign key column job_id, referenced by the column job_id of jobs table, can contain only those values which are exists in the jobs table. The InnoDB Engine have been used to create the tables. The specialty of the statement is that, The ON DELETE CASCADE that lets you allow to delete records in the employees(child) table that refer to a record in the jobs(parent) table when the record in the parent table is deleted and the ON UPDATE RESTRICT actions reject any updates.

DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
employee_id int PRIMARY KEY,
first_name varchar(50),
last_name varchar(50),
job_id int,
salary int,
FOREIGN KEY (job_id) REFERENCES jobs (job_id) ON DELETE CASCADE ON UPDATE RESTRICT
) Engine =InnoDB;

desc employees;


# 19. Write a SQL statement to create a table employees including columns employee_id, first_name, last_name, job_id, salary and make sure that, the employee_id column does not contain any duplicate value at the time of insertion, and the foreign key column job_id, referenced by the column job_id of jobs table, can contain only those values which are exists in the jobs table. The InnoDB Engine have been used to create the tables. The specialty of the statement is that, The ON DELETE SET NULL action will set the foreign key column values in the child table(employees) to NULL when the record in the parent table(jobs) is deleted, with a condition that the foreign key column in the child table must accept NULL values and the ON UPDATE SET NULL action resets the values in the rows in the child table(employees) to NULL values when the rows in the parent table(jobs) are updated.
DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
employee_id int PRIMARY KEY,
first_name varchar(50),
last_name varchar(50),
job_id int,
salary int,
FOREIGN KEY (job_id) REFERENCES jobs (job_id) ON DELETE set NULL  ON UPDATE set NULL
) Engine =InnoDB;

desc employees;

#20. Write a SQL statement to create a table employees including columns employee_id, first_name, last_name, job_id, salary and make sure that, the employee_id column does not contain any duplicate value at the time of insertion, and the foreign key column job_id, referenced by the column job_id of jobs table, can contain only those values which are exists in the jobs table. The InnoDB Engine have been used to create the tables. The specialty of the statement is that, The ON DELETE NO ACTION and the ON UPDATE NO ACTION actions will reject the deletion and any updates.

DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
employee_id int PRIMARY KEY,
first_name varchar(50),
last_name varchar(50),
job_id int,
salary int,
FOREIGN KEY (job_id) REFERENCES jobs (job_id) ON DELETE NO ACTION  ON UPDATE NO ACTION
) Engine =InnoDB;

desc employees;
