Update: real user input is messy. The argument may contain spaces, hyphens,
dots, and parentheses as separators — strip all of those characters first.
After stripping, if what remains is not exactly 10 digits (too short, too
long, letters, anything else), return `None` instead of a formatted string.
