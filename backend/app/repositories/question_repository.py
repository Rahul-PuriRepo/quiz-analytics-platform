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

    def get_question_by_id(self, question_id: int):
        return self.collection.find_one(
            {"questionId": question_id},
            {"_id": 0},
        )