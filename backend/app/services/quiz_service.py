import uuid
from datetime import datetime, UTC

from app.repositories.quiz_repository import QuizRepository

from fastapi import HTTPException

from app.repositories.question_repository import QuestionRepository
from app.schemas.answer_schema import AnswerRequest
from app.config.constants import POINTS_PER_QUESTION
from app.analytics.analytics_engine import AnalyticsEngine

class QuizService:
    
    def __init__(self):
        self.repository = QuizRepository()
        self.question_repository = QuestionRepository()
        self.analytics_engine = AnalyticsEngine()

    def start_quiz(self):
        session = {

            "sessionId": str(uuid.uuid4()),

            "status": "ACTIVE",

            "startedAt": datetime.now(UTC).isoformat(),

            "score": 0,

            "answers": []

        }
        return self.repository.create_session(session)

    def submit_answer(
        self,
        session_id: str,
        answer_request: AnswerRequest,
    ):
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

        score = session["score"]

        if is_correct:
            score += POINTS_PER_QUESTION

        answer = {
            "questionId": answer_request.questionId,
            "selectedOption": answer_request.selectedOption,
            "correct": is_correct,
            "timeTaken": answer_request.timeTaken,
        }

        self.repository.save_answer(
            session_id,
            answer,
        )

        self.repository.update_score(
            session_id,
            score,
        )

        return {
            **answer,
            "score": score,
        }

    def finish_quiz(self, session_id: str):
        session = self.repository.get_session(session_id)

        if session is None:
            raise HTTPException(
                status_code=404,
                detail="Session not found",
            )

        if session["status"] == "COMPLETED":
            raise HTTPException(
                status_code=400,
                detail="Quiz already completed",
            )

        finished_at = datetime.now(UTC)

        started_at = datetime.fromisoformat(session["startedAt"])

        duration = (finished_at - started_at).total_seconds()

        session= self.repository.finish_session(
                session_id,
                finished_at.isoformat(),
                duration,
            )
        summary = self.analytics_engine.calculate_summary(
                session,
                self.question_repository,
            )

        return summary

    def get_question_difficulty_index(self):
        sessions = self.repository.get_all_sessions()
        return self.analytics_engine.calculate_question_difficulty_index(
                                sessions,
                                self.question_repository,
                            )


    def get_summary(self, session_id: str):
        session = self.repository.get_session(session_id)
        if session is None:
            raise HTTPException(
                status_code=404,
                detail="Session not found",
            )
        return self.analytics_engine.calculate_summary(
                        session,
                        self.question_repository,
                    )

    