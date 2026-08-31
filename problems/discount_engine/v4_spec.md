Update: the checkout UI needs a breakdown, not just a number. Change the
return value to a dict:

    {"final": <int final price>,
     "total_discount": <int, base minus final>,
     "steps": <list of ints: the running price after EACH rule, in order>}

All discount semantics stay exactly as they are.
