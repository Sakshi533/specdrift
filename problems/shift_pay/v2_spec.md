Update from payroll: night work now earns a differential. A worked minute
falling in `[1320, 1440)` of its day (22:00–24:00; day `d` covers minutes
`[1440*d, 1440*(d+1))`) earns a +25% bonus on the base rate. The pay is now
three integer terms, each floored exactly once:

    pay            = base + night_bonus + overtime_bonus
    base           = total * rate
    night_bonus    = night_minutes * rate // 4
    overtime_bonus = overtime_minutes * rate // 2

`overtime_minutes = max(0, total - 2400)` as before, and the overtime term is
the same money as before (1.5x = base plus a half-rate bonus). Night and
overtime are classified independently — a minute that is both earns both
bonuses.
