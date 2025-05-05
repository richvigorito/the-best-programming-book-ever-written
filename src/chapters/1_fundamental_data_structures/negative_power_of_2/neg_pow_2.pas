program PowerOfTwo;

const 
  n = 10;

type 
  digit = 0..9;

var 
  i, k, r: integer;
  d: array[1..n] of digit;

begin
  (* initialize array with 1.000000... *)
  d[1] := 1;
  for i := 2 to n do
    d[i] := 0;

  writeln('Decimal representation of 2^-k:');
  
  for k := 1 to n do
  begin
    write('.');
    r := 0;
    for i := 1 to n do
    begin
      r := 10 * r + d[i];
      d[i] := r div 2;
      r := r mod 2;
      write(chr(d[i] + ord('0')));
    end;
    writeln;
  end;
end.

