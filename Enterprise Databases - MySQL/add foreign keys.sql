ALTER TABLE employee ADD foreign key(dno) references department(dnumber);
ALTER TABLE department ADD foreign key(mgr_ssn) references employee(ssn);
ALTER TABLE dept_locations ADD foreign key(dnumber) references department(dnumber);
ALTER TABLE project ADD foreign key(dnum) references department(dnumber);
ALTER TABLE works_on ADD foreign key(pno) references project(pnumber);
ALTER TABLE works_on ADD foreign key(essn) references employee(ssn);
ALTER TABLE dependent ADD foreign key(essn) references employee(ssn);