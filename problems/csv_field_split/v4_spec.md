Update: the client changed their mind on whitespace. We used to keep
whitespace around unquoted fields — now strip it: spaces and tabs around an
UNQUOTED field's content must be removed. Quoted fields are the opposite:
whatever sits between the quotes is preserved exactly, whitespace included.
Example: ` a ," b ",c` -> `["a", " b ", "c"]`.
