Update: we ship pre-releases now. A version may carry an optional pre-release
suffix `-<tag>` after the numeric part (e.g. `"1.2.0-beta"`); the tag starts
at the FIRST `-` in the string. The numeric parts are still compared exactly
as before, and only when they are equal does the tag matter: a pre-release
sorts BEFORE its release (`"1.2.0-beta"` is older than `"1.2.0"`), and two
pre-releases of the same numeric version compare by tag LEXICOGRAPHICALLY
(plain string comparison; equal tags mean equal versions). Missing numeric
components still count as 0, so `"2.0-rc"` equals `"2.0.0-rc"`.
