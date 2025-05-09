program BubbleSort;

uses crt;

const
  N = 12;
  AInit: array[1..N] of Integer = (5, 99, 101, 100, 2, 90, 9, 1, 2, 22, 5, 6);

var
  A: array[1..N] of Integer;
  i, j, Temp: Integer;

begin
  clrscr;

  for i := 1 to N do
    A[i] := AInit[i];

  for i := 1 to N - 1 do
    for j := 1 to N - i do
      if A[j] > A[j + 1] then
      begin
        (* xor swap *)
        A[j]      := A[j] Xor A[j +1];
        A[j + 1]  := A[j] Xor A[j +1];
        A[j]      := A[j] Xor A[j +1];
      end;

  WriteLn('Sorted array in ascending order:');
  for i := 1 to N do
    Write(A[i], ' ');
    
  ReadLn;
end.

