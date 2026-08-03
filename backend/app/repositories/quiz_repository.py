from app.database.connection import db


class QuizRepository:

    def create_session(self, session):
        db.quiz_sessions.insert_one(session)
        session.pop("_id", None)

        return {
            "sessionId": session["sessionId"],
            "status": session["status"],
            "startedAt": session["startedAt"],
            "score": session["score"],
            "answers": session["answers"],
        }

    def get_session(self, session_id):
        return db.quiz_sessions.find_one(
            {"sessionId": session_id}
        )

    def save_answer(self, session_id, answer):
        db.quiz_sessions.update_one(
            {"sessionId": session_id},
            {
                "$push": {
                    "answers": answer
                }
            }
        )

    def update_score(self, session_id: str, score: int):
        db.quiz_sessions.update_one(
            {"sessionId": session_id},
            {
                "$set": {
                    "score": score
                }
            }
        )

    def get_session(self, session_id: str):
        return db.quiz_sessions.find_one(
            {"sessionId": session_id}
        )