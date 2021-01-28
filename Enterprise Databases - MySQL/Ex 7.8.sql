create view research_employees as
select CONCAT(e1.fname,' ', e1.lname) as employee_name,
	CONCAT(e2.fname,' ', e2.lname) as supervisor_name,
    e1.salary as employee_salary
	from employee e1, employee e2, department d
    where e1.superssn = e2.ssn
    and e1.dno = d.dnumber
    and dname = 'Research'
    
create view dept_managers as
select dname as dept_name, CONCAT(fname,' ', lname) as manager_name, salary
from department, employee
where mgr_ssn = ssn

create view team_projects as
select * 
from (select p.pname as project_name,
	d.dname as dept_name,
    count(e.ssn) as num_employees,
    sum(w.hours) as total_hours
from project p, department d, employee e, works_on w
where p.dnum = d.dnumber
and p.pnumber = w.pno
and e.ssn = w.essn
group by p.pnumber) as proj_details
where num_employees > 1