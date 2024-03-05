# Display in your browser the pictures in the images subfolder
# idea and code from https://youtu.be/eq0k642zQQ8?si=UtoZcZV1nWUU3X_0
from nicegui import ui, app
from pathlib import Path

folder = Path(__file__).parent.joinpath("images")
files = [f.name for f in folder.glob("*.jpg")]

app.add_static_files("/temp", folder)

ui.label("Current images folder: " + str(folder)).style('color: #6E93D6; font-size: 150%; font-weight: 300')

with ui.row():
    ui.button("100 px", on_click=lambda: show(100))
    ui.button("200 px", on_click=lambda: show(200))
    ui.button("400 px", on_click=lambda: show(400))

images_container = ui.row().classes("full flex items-center")

def show(size):
    # first clear the row
    images_container.clear()
    with images_container:
        for filename in files:
            with ui.card():
                ui.image("temp/" + filename).style("width:" + str(size) + "px")
                ui.label(filename)

# serves only one images
# ui.image("/temp/flower-meadow-8572000_1280.jpg")

show(200)

# NiceGUI accepts emoji as favicon :)
ui.run(title="Image gallery", favicon = "📷")
