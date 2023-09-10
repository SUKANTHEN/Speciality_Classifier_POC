"""
main.py
-------
FastAPI code to 
"""
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from routers import classification_api

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
"""
Include routers
"""
app.include_router(classification_api.router)
