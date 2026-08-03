from fastapi import APIRouter

from app.services.question_service import QuestionService

router = APIRouter(prefix="/questions", tags=["Questions"])

service = QuestionService()


@router.get("/")
def get_questions():
    return service.get_questions()

@router.get("/{question_id}")
def get_question(question_id: str):
    return service.get_question(question_id)