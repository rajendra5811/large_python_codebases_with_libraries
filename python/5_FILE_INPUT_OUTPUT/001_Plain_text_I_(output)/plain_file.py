import pathlib
here = pathlib.Path('.')
print(here)                                  #"UDACITY"
here.absolute()
here/"customers"
here.parents
here.parent
here = here.resolve() 
"""with open(filepath, mode) as f:
    # Use the file-like object `f`
    try:
    f = open(filepath, mode)
    # Use the file-like object `f`
    ...
finally:
    f.close()"""
# (1) Extract data from the `queries.txt` file into Python.
with open('queries.txt', 'r') as infile:
    contents = infile.read()  # Read one big string - the contents of this file.
print(contents)

# (2) Transform the data within Python.
queries = contents.split('\n')  # Split the string into a list by line breaks.
normalized = [query.strip().lower() for query in queries[::2]]  # Normalize each query with the stripped, lowercased version of every other line.

# (3) Write the normalized queries out to a file.
with open('normalized-queries.txt', 'w') as outfile:
    for query in normalized:
        outfile.write(query + '\n')  # It might be better to use outfile.writelines here, but let's practice `.write`-ing strings.
