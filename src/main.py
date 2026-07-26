from fastapi import FastAPI

app = FastAPI()

@app.get("/", summary = "Root endpoint", description = "Returns a welcome message")
def root():
    return {"message": "Welcome to Vibe Music Player Service"}

@app.get("/health-check", summary = "Health check endpoint", description = "Checks the health of the service")
def health_check():
    return {"message": "Health check passed"}