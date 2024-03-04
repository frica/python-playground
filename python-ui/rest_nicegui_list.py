import requests
import json
from nicegui import ui

columns = [
    {'name': 'site', 'label': 'Site', 'field': 'site', 'required': True, 'align': 'left'},
    {'name': 'sports', 'label': 'Sport(s)', 'field': 'sports', 'sortable': True, 'align': 'left'},
]

# REST call
url = "https://data.paris2024.org/api/explore/v2.1/catalog/datasets/paris-2024-sites-de-competition/records?limit=60"
response = requests.get(url, verify=True)
json = json.loads(response.text)

# why does it show twice ???
print("Dataset size :", json["total_count"])

rows = []
sites = json["results"]

for site in sites:
    if site["category_id"] == "venue-olympic":
        rows.append({'site': site["nom_site"], 
                      'sports' : site["sports"]})

ui.link.default_style('color: black; font-weight: bold')

with ui.left_drawer().classes('bg-blue-100') as left_drawer:
    ui.label('Side menu')

with ui.header().classes(replace='row items-center') as header:
    ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
    with ui.row():
        ui.label('⭐ Welcome to my application using').props('inline')
        ui.link('Paris 2024 Data', 'https://data.paris2024.org/').props('inline')

ui.table(title="Olympic sites list", columns=columns, rows=rows, pagination=10)

with ui.footer().classes('bg-blue-60') as footer:
    ui.label('Powered by')
    ui.link('NiceGUI', 'https://github.com/zauberzeug/nicegui')

ui.run(title='JO Paris 2024')
