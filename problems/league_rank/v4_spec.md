Update: bad feeds keep reaching the ingest job. Harden `table`: any match
with a negative goal count raises `ValueError`; a match where a team plays
itself (`home == away`) raises `ValueError`; an empty `results` list returns
`[]`.
