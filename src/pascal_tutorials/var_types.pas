program VariablesDemo;
var
  age: Integer;
  price: Real;
  initial: Char;
  name: String;
begin
  age := 25;
  price := 19.99;
  initial := 'A';
  name := 'Alice';

  WriteLn('Age: ', age);
  WriteLn('Price: $', price:0:2);
  WriteLn('Initial: ', initial);
  WriteLn('Name: ', name);
end.
