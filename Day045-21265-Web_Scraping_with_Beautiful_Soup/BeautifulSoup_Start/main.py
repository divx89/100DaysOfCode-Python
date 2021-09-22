from bs4 import BeautifulSoup

with open(file='website.html', encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# Getting the data within the title tag
print(soup.title.string)

# Printing the html document
print(soup.prettify())

# Getting the first anchor tag in the html document
print(soup.a)

# Getting all tags of a certain type
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

# Getting the actual address from each anchor tag
for anchor_tag in all_anchor_tags:
    print(anchor_tag.get("href"))

# Getting data by id
heading = soup.find(name="h1", id="name")
print(heading.string)

# Getting all data with a certain class
# Note the attribute name is class_
section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))
print(section_heading.string)

# Using CSS Selectors to get a particular tag (type of tag)
company_url = soup.select_one(selector="p a")
print(company_url)

# Using CSS id selector
heading1 = soup.select_one(selector="#name")
print(heading1)

# Using CSS class selector
# Note that select_one gives the first matching element, while select gives all the matching elements
# in a list
other_pages = soup.select(selector=".heading")[1]
print(other_pages)