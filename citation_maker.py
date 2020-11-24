import html # For escaping titles and names

def esc_input(prompt = None):
    return html.escape(input(prompt))

def is_positive_integer(inp):
    """Tests if string inp is a positive integer."""
    if type(inp) != str:
        return False
    try:
        inp = int(inp)
        return inp > 0
    except ValueError:
        return False

print("Note: you probably can create the citation faster using the handbook.")
print("")
num_of_authors = input("How many authors does your work have? ")
if not is_positive_integer(num_of_authors):
    print("Not a valid number of authors.")
    exit()
# Number of authors is now valid
num_of_authors = int(num_of_authors)
authors = esc_input("What is the name of the first author? ")
if num_of_authors == 2:
    authors = authors + " and " + esc_input("What is the name of the second author? ")
if num_of_authors > 2:
    authors = authors + " et al."
# Getting Title
length_of_medium = input("Is the work large(\"l\") or small(\"s\")? ")
length_of_medium = length_of_medium.strip().lower()
title = esc_input("What is the title of the work? ")
if length_of_medium == "l":
    title = "<i>%s</i>" % title
elif length_of_medium == "s":
    title = "&quot;%s&quot;" % title
else:
    print("Not a valid input.")
    exit()
# Getting Locator
type_of_medium = input("Is your medium on the Web(\"w\"), a book(\"b\"), or other(\"o\")? ")
if type_of_medium == "w":
    locator = esc_input("What is the full URL of the work? ")
    locator = "<a href=\"%s\">%s</a>" % (locator,locator)
elif type_of_medium == "b":
    locator = esc_input("What is the ISBN of the book? ")
    locator = "ISBN "+locator
elif type_of_medium == "o":
    locator = ""
else:
    print("Not a valid input.")
    exit()

if locator != "":
    locator = ", "+locator
citation = "<p>"+authors+", "+title+locator

# Simple Extended Citations
extended = input("Do you want to use Simple Extended Citations yes (\"y\") or no (\"n\")? ")
if extended.lower() == "y":
    date = input("What date was the work published on? ")
    container = input("What is the name of the container (e.g. journal, book, larger website) is the work in? ")
    container = "<i>%s</i>" % container
    if container == "<i></i>" or container == title:
        end = "" # No comma if no container
    else:
        end = ", "+container
    citation = citation+", "+date+end

# Writing the citation
citation = citation + "</p>"
filename = input("What file do you want the citation saved to? ")
if not filename.endswith(".html"):
    filename = filename + ".html"
with open(filename, "w") as f:
    f.write(citation)
