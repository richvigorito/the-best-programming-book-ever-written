program ControlFlowDemo;
{ if, case, while, for statements }
var
  i: Integer;
begin
  for i := 1 to 5 do
    WriteLn('Iteration: ', i);

  if i > 3 then
    WriteLn('Greater than 3')
  else
    WriteLn('3 or less');
end.

