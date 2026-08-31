Update: config files in the wild carry comments. A full-line comment is a
line whose FIRST non-whitespace character is `;` or `#` (the line may be
indented) — ignore such lines entirely, even when they contain `=`. But a
`;` or `#` anywhere else is NOT a comment marker: `path = a;b ; keep` stores
the whole value `a;b ; keep`. Nothing else changes.
