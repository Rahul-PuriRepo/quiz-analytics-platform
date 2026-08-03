from app.database.connection import db


class QuestionRepository:

    def __init__(self):
        self.collection = db.questions

    def get_all_questions(self):
        return list(self.collection.find())

    def get_question_by_id(self, question_id):
        return self.collection.find_one({"_id": question_id})

    def get_questions_by_chapter(self, chapter_id):
        return list(
            self.collection.find(
                {"chapterId": chapter_id}
            )
        )