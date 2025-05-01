program ArrayDemo;
var
  nums: array[1..5] of Integer;
  i: Integer;
begin
  for i := 1 to 5 do
    nums[i] := i * 2;

  for i := 1 to 5 do
    WriteLn('Element ', i, ': ', nums[i]);
end.

