# Python: Variables and Simple Data Types

## Reference

Chapter 2 from Python Crash Course

### Basic String Manipulation

Simple concepts in this section:

`Personal Message`: Use variable to represent strings, then print the variable. You can concatenate things such as a greeting message by making a variable such as `name` and another such as `message` and use them to shorthand repeat message formats.

*Methods:* 

`upper()` & `lower()` to change the case of a string, `title()` to capitalize first letters.

`full_name = f"{first_name} {last_name}"` here the letter `f` creates `f-strings` (f is for format)

`\n` creates a new line, `\t` adds a tab to the text

`rstrip()` `lstrip()` removes the "white space" of a string on the right & left sides of the string respectively. `strip()` does both sides.

`removeprefix()` and `removesuffix()` remove.. prefixes and suffixes, oddly enough. Define the "ix" within the parentheses. `simple_url = nostarch_url.removeprefix('https://')` this line keeps `nostarch_url` in its original form while creating a new variable `simple_url` that has the prefix removed.

### Numbers

Integers: You can add (+), subtract (-), multiply (*), and divide (/) integers in Python. 

`**` = exponent representation

`Integers` whole numbers (in case you forgot... geeze go to summer school)
`Floats` numbers with a decimal point

mixing the two creates a float

Long numbers: `universe_age = 14_000_000_000` as `,` have other responsibilities and are much to busy for calculations.

Psych.. 

Multiple Assignment `x, y, z = 0, 0, 0`

`Constants` are variables whos value stays the same throughout the life of a program. In Python they are denoted by naming the variable in all capital letters. `MAX_CONNECTIONS = 5000`