from app.database.connection import db


class QuizRepository:

    def create_session(self, session):
        db.quiz_sessions.insert_one(session)

        # Remove MongoDB's injected ObjectId if present
        session.pop("_id", None)

        return {
            "sessionId": session["sessionId"],
            "status": session["status"],
            "startedAt": session["startedAt"],
            "score": session["score"],
            "answers": session["answers"],
        }