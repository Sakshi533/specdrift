Update: overflowing lines break our fixed-width display. A word longer than
`width` must no longer overflow — hard-break it into chunks of exactly
`width` characters (the last chunk may be shorter) before wrapping, and then
wrap as before, treating each chunk as a word. So a trailing chunk can share
its line with following words. No line may ever exceed `width` now.
