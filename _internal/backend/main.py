import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from routers import clients, payments, reports, reservations, services, workers 


app = FastAPI()


# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins temporarily
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(clients.router)
app.include_router(services.router)
app.include_router(reservations.router)
app.include_router(payments.router)
app.include_router(reports.router) 
app.include_router(workers.router)

# Sirviendo archivos estáticos desde "web"
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "../web")), name="static")

# Directorio de plantillas (HTML dinámico)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, "web")

templates = Jinja2Templates(directory=TEMPLATES_DIR)

@app.get("/")
async def read_index(request: Request):
    # Puedes pasar datos dinámicos al template
    return templates.TemplateResponse("index3.html", {"request": request, "message": "Bienvenido a Spa Sentirse Bien"})
@app.get("/login")
async def read_index(request: Request):
    # Puedes pasar datos dinámicos al template
    return templates.TemplateResponse("login.html", {"request": request, "message": "Bienvenido a Spa Sentirse Bien"})
@app.get("/cliente")
async def read_index(request: Request):
    # Puedes pasar datos dinámicos al template
    return templates.TemplateResponse("cliente.html", {"request": request, "message": "Bienvenido a Spa Sentirse Bien"})
def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()