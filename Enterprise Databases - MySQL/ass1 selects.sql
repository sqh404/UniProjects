select fname, minit, lname 
	from employee 
    inner join works_on on employee.ssn = works_on.essn
	where dno = 5 and hours > 10;
    
select fname, minit, lname 
	from employee e
    inner join dependent d on e.ssn = d.essn
	where d.dependent_name = e.fname;

select fname, minit, lname 
	from employee 
	where superssn = (select ssn from employee 
		where fname = 'Franklin' and lname = 'Wong');
        
update dept_locations 
	set dlocation = 'Cleveland'
    where dnumber = 8 and dlocation = 'Chicago';
commit;    
select * from dept_locations; 

insert into dependent(essn, dependent_name, sex, bdate, relationship)
values((select ssn from employee where fname = 'Franklin' and lname = 'Wong'), 
	'Sarah',
    'F',
    curdate(),
    'daughter');
select * from dependent where dependent_name = 'Sarah';
commit;