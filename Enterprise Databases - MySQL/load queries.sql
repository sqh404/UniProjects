LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/employee.dat" 
	INTO TABLE employee FIELDS TERMINATED BY ',' ENCLOSED BY '"';
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/department.dat" 
	INTO TABLE department FIELDS TERMINATED BY ',' ENCLOSED BY '"';    
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/dependent.dat" 
	INTO TABLE dependent FIELDS TERMINATED BY ',' ENCLOSED BY '"';    
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/dloc.dat" 
	INTO TABLE dept_locations FIELDS TERMINATED BY ',' ENCLOSED BY '"';    
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/project.dat" 
	INTO TABLE project FIELDS TERMINATED BY ',' ENCLOSED BY '"';    
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/worksOn.dat" 
	INTO TABLE works_on FIELDS TERMINATED BY ',' ENCLOSED BY '"';