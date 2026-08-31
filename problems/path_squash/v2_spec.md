Update: we do want ".." resolved now. A ".." segment is removed together
with the real segment right before it ("a/../b" is just "b"). A ".." at the
start of a relative path has nothing to cancel and stays (so "../a" is
"../a", and so on for stacked ones). Going above the root is clamped: "/.."
squashes to "/".
