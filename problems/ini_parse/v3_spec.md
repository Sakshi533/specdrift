Update: the duplicate-key rule was backwards. The client's tooling treats the
first assignment as authoritative, so we're reversing it: when a key appears
more than once in a section, keep the FIRST value and ignore all later
assignments to that key. (Comment lines still don't count as assignments.)
