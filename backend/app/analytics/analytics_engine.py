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

        learning_velocity = self.calculate_learning_velocity(
                accuracy,
                average_response_time,
            )
        fatigue_score = self.calculate_fatigue_score(answers)

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

            "learningVelocityIndex": learning_velocity,

            "fatigueScore": fatigue_score,
        }

    def calculate_learning_velocity(self, accuracy, average_response_time):
        velocity = accuracy - (average_response_time / 2)

        if velocity < 0:
            velocity = 0

        return round(velocity, 2)

    def calculate_fatigue_score(self, answers):
        if len(answers) < 2:
            return 0

        first = answers[0]["timeTaken"]
        last = answers[-1]["timeTaken"]

        return max(0, last - first)