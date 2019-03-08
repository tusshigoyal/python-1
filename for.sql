declare 
num number:=4;
begin 
LOOP
	dbms_output.put_line(num);
	EXIT WHEN num>10;
	num := num+1;	
END LOOP;
end;
