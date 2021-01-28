CREATE TABLE department (
  dname    varchar(20) not null, 
  dnumber      integer(4),
  mgr_ssn      char(9) not null,
  mgr_start_date    date,
  primary key (dnumber)
);