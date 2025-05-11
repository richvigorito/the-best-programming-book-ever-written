program QuickSortHardCoded;

uses crt;

const
  N = 10;
  AInit: array[1..N] of Integer = (34, 7, 23, 32, 5, 62, 32, 4, 1, 19);

var
  A: array[1..N] of Integer;

procedure QuickSort(var A: array of Integer; Low, High: Integer);
var
  i, j, Pivot, Temp: Integer;
begin
  i := Low;
  j := High;
  Pivot := A[(Low + High) div 2];

  repeat
    while A[i] < Pivot do Inc(i);
    while A[j] > Pivot do Dec(j);

    if i <= j then
    begin
      Temp := A[i];
      A[i] := A[j];
      A[j] := Temp;
      Inc(i);
      Dec(j);
    end;
  until i > j;

  if Low < j then QuickSort(A, Low, j);
  if i < High then QuickSort(A, i, High);
end;

var
  i: Integer;

begin
  clrscr;

  // Copy hard-coded values
  for i := 1 to N do
    A[i] := AInit[i];

  QuickSort(A, 1, N);

  WriteLn('Sorted array in ascending order:');
  for i := 1 to N do
    Write(A[i], ' ');

  ReadLn;
end.
