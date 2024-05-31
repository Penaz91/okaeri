#!/usr/bin/env python3
"""
This is the rendering system for okaeri.

Requires Mako and a links file
"""
import sys
from mako.template import Template


def parse_file(filename="links.oka"):
    """
    Parses the link file
    """
    sections = {}
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("#"):
                sect_name = line[2:-1]
                sections[sect_name] = []
            elif line != "\n":
                sections[sect_name].append(line[:-1])
        return sections


def create_links(sections):
    """
    Creates a list of links
    """
    links = []
    for key, val in sections.items():
        for s in val:
            s = s.split('  ')
            links.append((key, s[0], s[1]))
    return links


if __name__ == "__main__":
    parsed_sections = parse_file()
    zerudas = create_links(parsed_sections)

    # Gets theme
    theme = "train"  # default
    if len(sys.argv) == 2:
        theme = sys.argv[1]

    tmpl = Template(
        filename='./html/template.html',
        input_encoding='utf-8',
        output_encoding='utf-8'
    )

# Creates homepage from template
    with open("./html/index.html", 'wb') as f_out:
        f_out.write(
            bytes(
                tmpl.render(
                    zerudas=zerudas,
                    sections=parsed_sections,
                    theme=theme)
            )
        )
