procedure insertionSort(var A: array of integer; N: integer);
var
  i, j, key: integer;
begin
  for i := 1 to N - 1 do
  begin
    key := A[i];
    j := i - 1;
    while (j >= 0) and (A[j] > key) do
    begin
      A[j + 1] := A[j];
      j := j - 1;
    end;
    A[j + 1] := key;
  end;
end;
