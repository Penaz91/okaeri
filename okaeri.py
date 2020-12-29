#!/usr/bin/env python3
import sys
from mako.template import Template

def parse_file(filename="links.oka"):
    sections = {}

    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("#"):
                sect_name = line[2:-1]
                sections[sect_name] = []
            elif line != "\n":
                sections[sect_name].append(line[:-1])

        return sections

def create_links(sections):
    links = []
    for key, val in sections.items():
        for s in val:
            s = s.split(' ')
            links.append((key, s[0], s[1]))
    return links


sections = parse_file()
zerudas = create_links(sections)

# Gets theme
if len(sys.argv) == 2:
    theme = sys.argv[1]

else:
    theme = "train" # default

tmpl = Template(filename='./html/template.html', input_encoding='utf-8', output_encoding='utf-8')

# Creates homepage from template
with open("./html/homepage.html", 'wb') as f_out:
    f_out.write(bytes(tmpl.render(zerudas=zerudas, sections=sections, theme=theme)))
