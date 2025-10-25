import os
import json
def load_chapters():
    with open(os.path.join("UI","static","chapters.json")) as f:
        chapters = json.loads(f.read())
    return chapters

def load_css():
    with open(os.path.join("UI","static","homepage.css")) as f:
        css = f.read()
    return css