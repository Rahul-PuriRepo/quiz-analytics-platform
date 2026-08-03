from fastapi import APIRouter

from app.services.quiz_service import QuizService

router = APIRouter(
    prefix="/quiz",
    tags=["Quiz"],
)

service = QuizService()


@router.post("/start")
def start_quiz():
    return service.start_quiz()