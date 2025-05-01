program RecordsDemo;
{ pascal's version of objects/structs }
type
  Person = record
    name: String;
    age: Integer;
  end;

var
  p: Person;
begin
  p.name := 'Bob';
  p.age := 42;

  WriteLn(p.name, ' is ', p.age, ' years old.');
end.

