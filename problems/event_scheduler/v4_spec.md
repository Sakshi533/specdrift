Update: the request form sometimes sends garbage. If the requested slot itself
is invalid — `start >= end`, or a negative `start` or `end` — return `False`.
Never raise an exception for an invalid request.
