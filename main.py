from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from rules import choisir_architecture

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context= {"request": request}
    )

@app.post("/result", response_class=HTMLResponse)
def result(
    request: Request,
    taille: str = Form(...),
    scalabilite: str = Form(...),
    complexite: str = Form(...),
    utilisateurs: str = Form(...),
    temps_reel: str = Form(...),
    budget: str = Form(...)
):
    data = {
        "taille": taille,
        "scalabilite": scalabilite,
        "complexite": complexite,
        "utilisateurs": utilisateurs,
        "temps_reel": temps_reel,
        "budget": budget
    }

    architecture, score, explication = choisir_architecture(data)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
       context= {
        "request": request,
        "result": architecture,
        "score": score,
        "explication":explication
    })