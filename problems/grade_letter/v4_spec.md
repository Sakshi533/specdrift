Update: garbage has been reaching this function. Any score outside the range
[0, 100] must raise `ValueError`, and so must `None`. Range-checking happens
on the raw input, before the rounding step; in-range scores keep working
exactly as they do now.
