from fastapi import FastAPI
from routes import base_routes

app = FastAPI()

# the frontend should have a unique port and backend should have diffrent one
# examle :
# uvicorn on port 8080
# python -m http.server 8000  , allow_origins=["http://localhost:8000"],
# is used to open app in the folder that contains index.html
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000","https://mysqlfastapi.vercel.app/"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(base_routes)
