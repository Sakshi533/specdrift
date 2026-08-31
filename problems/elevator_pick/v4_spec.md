Update: hardening before the gateway launch. `pick([], floor)` must return
-1 instead of crashing -- the lobby panel sometimes fires before any car
registers. And any car whose direction isn't exactly "up", "down", or
"idle" must raise ValueError, even if that car would never have been
picked; last week bad telemetry got silently treated as a real car.
Dispatch behavior on valid input is untouched.
