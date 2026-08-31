Update from payroll: legal says the night differential and overtime must NOT
stack after all. Classify the week's worked minutes chronologically — the
first 2400 worked minutes are regular, every worked minute after that is
overtime. A minute that is both night and overtime earns only the LARGER of
the two bonuses (the overtime half-rate), so it drops out of the night term:

    night_bonus    = (night_minutes - night_overtime_minutes) * rate // 4
    overtime_bonus = overtime_minutes * rate // 2   (unchanged, covers ALL overtime minutes)

`base` and everything else are unchanged.
