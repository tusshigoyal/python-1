declare 
	cursor abc is
	select * from std;
	empl std%rowtype;

begin
	open abc;
	LOOP
	fetch abc into empl;
	EXIT WHEN abc%NOTFOUND;
	dbms_output.put_line(empl.id||'     '|| empl.name||'     '||empl.fname);
	END LOOP;
	close abc;
end;
/