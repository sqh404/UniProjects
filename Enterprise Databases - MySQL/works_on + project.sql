CREATE TABLE works_on (
  essn      char(9) not null,
  pno      integer(4),
  hours    decimal(5,1),
  primary key (essn, pno)
);

CREATE TABLE project (
  pname    varchar(20) not null, 
  pnumber   integer(4),
  plocation varchar(20),
  dnum 		integer(4),
  primary key (pnumber)
);