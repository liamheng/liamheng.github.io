#coding:utf-8
import pandas as pd
import os

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)

patents = pd.read_excel("patents.xlsx")
html="<ul>\n"
author_h = "李衡"
for row, item in patents.iterrows():
    html += '<li>\n<div class="list_item">\n'
    authors = item["authors"].split(",")
    author_string=""
    cnt = 0
    for i in range(len(authors)):
        if i == 0:
            if authors[i] == author_h:
                author = "<b>{}</b>".format(authors[i])
            else:
                author = authors[i]
        else:
            if authors[i] == author_h:
                author = ", <b>{}</b>".format(authors[i])
            else:
                author = ", {}".format(authors[i])
        author_string += author
    author_string += "。"
    print(item["name"])
    html+='<p class="archive__item-excerpt" itemprop="description">{}. {}"{}", {}, {}, {}</p>\n'.format(row+1, 
                                                                html_escape(author_string), html_escape(str(item["name"])), 
                                                                html_escape(item.type), html_escape(str(item.status)), 
                                                                html_escape(str(item.id)))
    html+="</div>\n</li>\n"

with open("../_includes/patents.html", "w", encoding="utf-8") as F:
    F.write(html)