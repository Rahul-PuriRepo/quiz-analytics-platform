from fastapi import APIRouter

from app.services.quiz_service import QuizService
from app.schemas.answer_schema import AnswerRequest

router = APIRouter(
    prefix="/quiz",
    tags=["Quiz"],
)

service = QuizService()


@router.post("/start")
def start_quiz():
    return service.start_quiz()

@router.post("/{session_id}/answer")
def submit_answer(session_id: str,answer: AnswerRequest):
    return service.submit_answer(session_id, answer)