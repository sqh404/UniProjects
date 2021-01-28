delete from works_on
    where pno = (select pnumber from project where pname = 'Computerization');
delete from project
	where pname = 'Computerization';
    
select * from project p
	inner join works_on w on p.pnumber = w.pno;