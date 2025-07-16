"""
Main FastAPI application entry point for JFGlobalExpress courier service.
This file will be implemented in later tasks.
"""

from fastapi import FastAPI

app = FastAPI(
    title="JFGlobalExpress API",
    description="API for JFGlobalExpress courier service with AI bot integration",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {"message": "JFGlobalExpress API - Ready for implementation"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "jfglobalexpress-api"}