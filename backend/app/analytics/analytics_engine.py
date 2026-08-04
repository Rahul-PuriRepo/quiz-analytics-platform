class AnalyticsEngine:

    def calculate_summary(
        self,
        session,
    ):

        answers = session["answers"]

        total_questions = len(answers)

        correct_answers = sum(
            answer["correct"]
            for answer in answers
        )

        accuracy = 0

        if total_questions > 0:
            accuracy = (
                correct_answers
                / total_questions
            ) * 100

        average_response_time = 0

        if total_questions > 0:
            average_response_time = (
                sum(
                    answer["timeTaken"]
                    for answer in answers
                )
                / total_questions
            )

        return {

            "score": session["score"],

            "questionsAnswered": total_questions,

            "correctAnswers": correct_answers,

            "accuracy": round(
                accuracy,
                2,
            ),

            "averageResponseTime": round(
                average_response_time,
                2,
            ),
        }