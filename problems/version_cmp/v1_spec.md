Write a Python function `cmp(a, b)` that compares two dotted numeric version
strings and returns `-1` if `a` is the older version, `1` if `a` is the newer
version, and `0` if they denote the same version.

Rules:

- A version string is one or more components separated by `.` (e.g. `"1.2.10"`,
  `"3"`). Each component is a base-10 integer; leading zeros are allowed and
  carry no meaning (`"1.02"` equals `"1.2"`).
- Compare component by component, left to right, NUMERICALLY — `"1.10"` is
  newer than `"1.9"`.
- When one version has fewer components, the missing components count as `0`:
  `"1.2"` equals `"1.2.0"`, and `"1.2.10"` is older than `"1.3"`.
- The return value is always exactly `-1`, `0`, or `1`.
