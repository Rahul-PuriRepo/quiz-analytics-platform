from app.database.connection import db


class QuestionRepository:
    def __init__(self):
        self.collection = db.questions

    def get_all_questions(self):
        return list(
            self.collection.find(
                {},
                {"_id": 0}
            )
        )