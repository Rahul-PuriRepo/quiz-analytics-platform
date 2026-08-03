import uuid
from datetime import datetime, UTC

from app.repositories.quiz_repository import QuizRepository

from fastapi import HTTPException

from app.repositories.question_repository import QuestionRepository


class QuizService:

    def __init__(self):
        self.repository = QuizRepository()
        self.question_repository = QuestionRepository()

    def start_quiz(self):
        session = {

            "sessionId": str(uuid.uuid4()),

            "status": "ACTIVE",

            "startedAt": datetime.now(UTC).isoformat(),

            "score": 0,

            "answers": []

        }
        return self.repository.create_session(session)

    def submit_answer(self, session_id, answer_request,):
        session = self.repository.get_session(session_id)

        if session is None:
            raise HTTPException(
                status_code=404,
                detail="Session not found"
            )

        question = self.question_repository.get_question_by_id(answer_request.questionId)

        if question is None:
            raise HTTPException(
                status_code=404,
                detail="Question not found"
            )

        correct_option = question["options"][question["correctOption"]]

        is_correct = (answer_request.selectedOption == correct_option)

        session = self.repository.get_session(session_id)

        score = session["score"]

        if is_correct:
            score += 10

        self.repository.update_score(session_id,score)

        answer = {
            "questionId": answer_request.questionId,
            "selectedOption": answer_request.selectedOption,
            "correct": is_correct,
            "timeTaken": answer_request.timeTaken,
        }

        self.repository.save_answer(session_id,answer)
        return answer