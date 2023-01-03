import re


links = []
with open('source.txt', "r") as mf:
    data = mf.readlines()

for s in data:        
    # Use a regular expression to match the link
    link_regex = re.compile(r'\[img\](https://.+?)\[/img\]')
    link_match = link_regex.search(s)

    if link_match:
        # Extract the link from the match
        link = link_match.group(1)
        print('<img src="' + link + '"' + ' height="42px">')


