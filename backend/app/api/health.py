from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["Health"])
def health_check():
    return {
        "message": "Welcome to Quiz Analytics Platform",
        "status": "Running Successfully"
    }