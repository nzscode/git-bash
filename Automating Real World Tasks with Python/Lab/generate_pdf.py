from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate

# These are the FLOWABLES (chunks/elements) we need to build the pdf
from reportlab.platypus import Paragraph, Spacer, Table, Image

# We need to import the stylesheet to access the styles
from reportlab.lib.styles import getSampleStyleSheet

# To change the style of the table
from reportlab.lib import colors

# Drawing must be imported to generate a pie chart
from reportlab.graphics.shapes import Drawing

# To create a pie chart
from reportlab.graphics.charts.piecharts import Pie


# The report generated will be saved as report.pdf
report = SimpleDocTemplate("report.pdf")

# The styles we want to use for the Flowables
styles = getSampleStyleSheet()

# Using the default sample style for the pdf, the title will be in a paragraph flowable with an H1 style.
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])


fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

# TO generate a table in the pdf, the dictionary must be converted into a two-dimensional-array
table_data = []
for k, v in fruit.items():
  table_data.append([k, v])


# To give the table style, by moving it to the left and adding black border around it
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

# To build a pie chart
report_pie = Pie(width=3*inch, height=3*inch)

# To add data to the pie chart, we need two lists, one for data, one for lables
report_pie.data = []
report_pie.labels = []

for fruit_name in sorted(fruit):
  report_pie.data.append(fruit[fruit_name])
  report_pie.labels.append(fruit_name)

# print(report_pie.data)
# print(report_pie.labels)

# Adding the Pie chart to the pdf, it must be placed inside a FLOWABLE Drawing.
report_chart = Drawing()
report_chart.add(report_pie)

# To build the report
report.build([report_title, report_table, report_chart])