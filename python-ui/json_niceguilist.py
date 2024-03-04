import json
import asyncio
from nicegui import ui

async def load():
    n = ui.notification(timeout=None)
    for i in range(5):
        n.message = f'Loading {i/5:.0%}'
        n.spinner = True
        await asyncio.sleep(0.2)
    n.message = 'Done!'
    n.spinner = False
    await asyncio.sleep(1)
    n.dismiss()

columns = [
    {'name': 'site', 'label': 'Site', 'field': 'site', 'required': True, 'align': 'left'},
    {'name': 'sports', 'label': 'Sport(s)', 'field': 'sports', 'sortable': True, 'align': 'left'},
]

link = 'paris-2024-sites-de-competition.json'
# read file
with open(link, 'r') as myfile:
    data = myfile.read()

# parse file
sites = json.loads(data)
rows = []

for site in sites:
    if site["category_id"] == "venue-olympic":
        rows.append({'site': site["nom_du_site"], 
                      'sports' : site["sports"]})

ui.link.default_style('color: black; font-weight: bold')

ui.button('Load data', on_click=load)
ui.separator()

with ui.left_drawer().classes('bg-blue-100') as left_drawer:
    ui.label('Side menu')

with ui.header().classes(replace='row items-center') as header:
    ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
    with ui.row():
        ui.label(' Welcome to my application using'). props('inline')
        ui.link('Paris 2024 Data', 'https://data.paris2024.org/'). props('inline')

ui.table(title="Olympic sites list", columns=columns, rows=rows, pagination=10)

with ui.footer().classes('bg-blue-60') as footer:
    ui.label('Powered by')
    ui.link('NiceGUI', 'https://github.com/zauberzeug/nicegui')

ui.run(title='JO Paris 2024')
