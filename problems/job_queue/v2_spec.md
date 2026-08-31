Update: low-priority jobs are starving, so we're adding aging. Count
executed jobs from the start of the run: every 4th slot (the 4th, 8th,
12th, ... job to run) is an aging slot. In an aging slot, if any waiting
job's priority is strictly below the highest priority still waiting, run the
earliest-submitted such job instead of the normal pick. If everything still
waiting sits at a single priority level, the aging slot behaves like a
normal slot. All other slots are completely normal.
