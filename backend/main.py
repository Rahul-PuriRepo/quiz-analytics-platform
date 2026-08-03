from fastapi import FastAPI

from app.api.health import router as health_router
from app.config.settings import APP_NAME
from app.api.questions import (
    router as question_router,
)


app = FastAPI(
    title=APP_NAME,
    description="""
A full-stack quiz analytics platform built using React, FastAPI and MongoDB.

Features

- Quiz Engine
- Learning Velocity Index
- Fatigue Analysis
- Question Difficulty Index
""",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(question_router)