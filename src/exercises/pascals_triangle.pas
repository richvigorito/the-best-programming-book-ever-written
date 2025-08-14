program PascalsTriangle;

var
  triangle: array[1..20, 1..20] of integer;
  i, j, n: integer;

begin
  write('Enter number of rows: ');
  readln(n);

  (* Fill in code to build pascal triangle of N rows *)

  writeln('Pascal''s Triangle:');
  for i := 1 to n do
  begin
    for j := 1 to i do
      write(triangle[i, j], ' ');
    writeln;
  end;
end.

