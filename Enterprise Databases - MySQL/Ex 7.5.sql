select dname, count(sex)
from employee, department
where dno = dnumber
and sex = 'M'
and dno in 
	(select dno from 
		(select avg(salary) as avs, dno
		from employee 
		group by dno) as depavg
		where avs > 30000)
group by dno