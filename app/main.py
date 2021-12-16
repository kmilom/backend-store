from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config  import settings
from app.api.api import api_router

app = FastAPI()
app.add_middleware(
   CORSMiddleware,
   allow_origins=["http://localhost:3000","*"],
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/health-check/")
def health_check():
    return "Ok"