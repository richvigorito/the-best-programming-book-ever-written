program PascalsTriangle;

var
  triangle: array[1..20, 1..20] of integer;
  i, j, n: integer;

begin
  write('Enter number of rows: ');
  readln(n);

  for i := 1 to n do
  begin
    triangle[i, 1] := 1;
    triangle[i, i] := 1;

    for j := 2 to i - 1 do
      triangle[i, j] := triangle[i - 1, j - 1] + triangle[i - 1, j];
  end;

  writeln('Pascal''s Triangle:');
  for i := 1 to n do
  begin
    for j := 1 to i do
      write(triangle[i, j], ' ');
    writeln;
  end;
end.

