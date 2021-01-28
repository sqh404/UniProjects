select fname, minit, lname from employee
where dno = (select dno from employee
	where salary = (select max(salary) from employee))
    
select fname, minit, lname from employee
where superssn IN 
	(select ssn from employee
		where superssn = '888665555')
        
select fname, minit, lname from employee
	where salary > 10000 + (select MIN(salary) from employee)