program FunctionsDemo;
{ functions return values,  functions do not }
procedure Greet(name: String);
begin
  WriteLn('Hello, ', name);
end;

function Square(x: Integer): Integer;
begin
  Square := x * x;
end;

begin
  Greet('Pascal');
  WriteLn('4 squared is ', Square(4));
end.

