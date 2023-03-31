import pandas as pd

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


projects = pd.read_csv("projects.tsv", header=0)
html="<ul>\n"
for row, item in projects.iterrows():
    print(item.keys())
    html+='<li>\n<div class="list_item">\n'
    print(item)
    html+='<h3>{}</h3>\n'.format(html_escape(item['name']))
    html+='<div><p class="archive__item-excerpt" itemprop="description">Funding:{}</p></div>\n'.format(html_escape(item.funding))
    html+='<div><p class="archive__item-excerpt" itemprop="description">Duration:{}</p></div>\n'.format(html_escape(item.duration))
    html+='<div><p class="archive__item-excerpt" itemprop="description">Role:{}</p></div>\n'.format(html_escape(item.role))
    html+="</div>\n</li>\n"
html+="</ul>"
with open("../_includes/projects.html", "w", encoding="utf-8") as f:
    f.write(html)