import uuid
from datetime import datetime, UTC

from app.repositories.quiz_repository import QuizRepository


class QuizService:

    def __init__(self):
        self.repository = QuizRepository()

    def start_quiz(self):
        session = {

            "sessionId": str(uuid.uuid4()),

            "status": "ACTIVE",

            "startedAt": datetime.now(UTC).isoformat(),

            "score": 0,

            "answers": []

        }
        return self.repository.create_session(session)