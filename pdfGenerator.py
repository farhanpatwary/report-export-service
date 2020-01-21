from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("./templates/reportTemplate.html")
items = ['hello','world']
template_vars = {
    "title" : "Sales Funnel Report - National",
    "items": items
}

html_out = template.render(template_vars)

HTML(string=html_out).write_pdf("report.pdf")