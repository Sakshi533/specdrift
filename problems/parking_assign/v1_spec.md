Write a Python function `assign(spots, cars)`.

`spots` is a list of spot sizes (`"S"`, `"M"`, or `"L"`); `cars` is a list
of car sizes (same three). Process cars in order. A car takes the FIRST
free spot of its exact size; if none is free, the first free spot exactly
one size larger (S -> M, M -> L; L has nothing larger). A car that finds no
spot gets -1 and takes nothing. Return the list of assigned spot indices,
one per car, in order. An assigned spot stays taken for the rest of the run.
