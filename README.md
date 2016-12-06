# highlite
A python3 based word highlighter

This was a simple word highlighter I knocked out in a few minutes because I wanted something like grep --color=auto, but I wanted it to display the entire contents of the file, highlighting the matching term, rather than just displaying the matching line.

Anyway, syntax is:

highlite.py <search expression> <file name>

Input piping also works:

cat <filename> | highlite.py <search expression>

Far as I know regexps should work fine, though matching across multiple lines might not.  Also, it only accepts a single file right now, so no wildcarding filenames.

A todo:
- Accept multiple files
- Color options
- Searches across multiple lines
- Maybe look at more grep functionality to duplicate
