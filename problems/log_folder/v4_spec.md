Update: real exports contain junk entries. An empty string `""` in the input
produces NO output line, and it terminates the current fold group: a
continuation line coming right after an empty string stands alone (leading
whitespace stripped) instead of folding into anything. Collapsing still runs
on the resulting output lines, so identical lines separated only by empty
input entries DO collapse. A `None` entry anywhere in the list raises
`ValueError`.
