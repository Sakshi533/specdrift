Write a Python function `pick(cars, floor)`.

`cars` is a non-empty list of `(position, direction)` tuples: `position` is
an int floor number and `direction` is one of `"up"`, `"down"`, `"idle"`.
A hall call comes in at int `floor`. Return the index of the car to
dispatch: the car nearest to `floor` by absolute distance; on a distance
tie, the lowest index wins. Direction is carried in the data but plays no
role in the choice for now.
