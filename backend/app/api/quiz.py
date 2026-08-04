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

@router.post("/{session_id}/finish")
def finish_quiz(session_id: str):
    return service.finish_quiz(session_id)

@router.get("/{session_id}/analytics")
def get_summary(
    session_id: str,
):
    return service.get_summary(
        session_id,
    )