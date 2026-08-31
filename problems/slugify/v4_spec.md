Update: edge case from production — if the slug comes out empty (empty input,
or input containing no letters or digits at all), return the literal slug
`"n-a"` instead of an empty string.
