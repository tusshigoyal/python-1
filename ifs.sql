declare
num number:=5;
begin
loop
	dbms_output.put_line(num);
	if num>12
	then
		exit;
	end if;
	num:= num+1;
end loop;
end;
