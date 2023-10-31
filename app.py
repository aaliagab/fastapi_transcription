from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.transcription_routes import router_transcription

app = FastAPI(
        title = "My API for Transcriptions",
        description = "A REST API built with FastAPI for Transcription.",
        version = "1.0.0",
    )


# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Set up routes
app.include_router(router_transcription, prefix="/ai/transcriptions", tags=["transcriptions"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)