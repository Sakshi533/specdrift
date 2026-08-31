Update: the intake form has been letting junk through. Any size string that
isn't legal must raise ValueError -- legal vehicle sizes are `"XS"`, `"S"`,
`"M"`, `"L"`; legal spot sizes are `"S"`, `"M"`, `"L"` (there is no such
thing as an XS spot). Validate both lists up front: bad data anywhere
raises before anyone parks. Also: an empty `spots` list must not crash --
every vehicle just gets -1 -- and an empty `cars` list returns `[]`.
