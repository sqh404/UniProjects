CREATE TABLE dept_locations (
  dnumber     	integer(4),
  dlocation 	varchar(20),
  primary key (dnumber, dlocation)
);

CREATE TABLE dependent (
  essn 				char(9),
  dependent_name    varchar(20) not null, 
  sex 				char,
  bdate				date,
  relationship 		varchar(15),
  primary key (essn, dependent_name)
);