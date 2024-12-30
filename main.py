from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from backend.one_to_ten import get_phrase
from backend.bewerbung import get_bewerbung
from backend.gericht import get_gericht

# Create the FastAPI app
app = FastAPI()

# Serve static files (for CSS or images, if needed) and set up templates folder
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Homepage route
@app.get("/", response_class=HTMLResponse)
async def get_homepage(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})


# Subpage 1
@app.get("/one_to_ten", response_class=HTMLResponse)
async def subpage1(request: Request):
    phrase = get_phrase()
    return templates.TemplateResponse("one_to_ten.html",
                                      {"request": request,
                                       "page_title": "One To Ten",
                                       "phrase": phrase["phrase"],
                                       "from": phrase["from"],
                                       "to": phrase["to"]})


# Subpage 2
@app.get("/bewerbung", response_class=HTMLResponse)
async def subpage2(request: Request):
    return templates.TemplateResponse("spontane_bewerbung.html",
                                      {"request": request,
                                       "page_title": "Sponantes Bewerbungsgespräch",
                                       "job": get_bewerbung()})


# Subpage 3
@app.get("/gericht", response_class=HTMLResponse)
async def subpage3(request: Request):
    return templates.TemplateResponse("spontane_gericht.html",
                                      {"request": request,
                                       "page_title": "Sponante Gerichtsverhandlung",
                                       "crime": get_gericht()})


# Subpage 4
# @app.get("/subpage4", response_class=HTMLResponse)
# async def subpage4(request: Request):
#     return templates.TemplateResponse("subpage4.html", {"request": request, "page_title": "Subpage 4"})
