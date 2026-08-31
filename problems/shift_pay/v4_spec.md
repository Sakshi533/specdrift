Update: finance wants the breakdown, not one opaque number. `pay` must now
return a dict `{"total": int, "base": int, "night_bonus": int,
"overtime_bonus": int}` — the same three terms as today, with
`total = base + night_bonus + overtime_bonus`. No pay math changes.
