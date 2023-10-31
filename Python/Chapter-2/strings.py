# Simple variable declaration and printing
name = "mcfiggins barelyfoot"
print(name.title())

# String Case Change
print(name.upper())
print(name.lower())

# String Concatenation
first_name = "mcfiggins"
last_name = "barelyfoot"
full_name = f"{first_name} {last_name}"
print(full_name)

# Notice that the `title()` method Capitalizes the first letter of each word
print(f"Hello, {full_name.title()}!")

# rather than printing the string, we can store it in a variable
message = f"Hello, {full_name.title()}!"
print(message)

# Adding Whitespace to Strings with Tabs or Newlines
# \t adds a tab, \n adds a newline
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")

# Stripping Whitespace with `rstrip()`, `lstrip()`, and `strip()`
# `rstrip()` strips whitespace from the right side of a string
# `lstrip()` strips whitespace from the left side of a string
# `strip()` strips whitespace from both sides of a string
favorite_language = "python "
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

# Remove Prefixes with removeprefix() method
# Remove Suffixes with removesuffix() method
github_url = 'https://github.com'
github_url.removeprefix('https://')
print(github_url)
github_url.removesuffix('.com')
print(github_url)

