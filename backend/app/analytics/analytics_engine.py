class AnalyticsEngine:

    def calculate_summary(
        self,
        session,
        question_repository,
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

        difficulty_analysis = self.calculate_difficulty_analysis(
                    session,
                    question_repository,
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

            "learningVelocityIndex": learning_velocity,

            "fatigueScore": fatigue_score,

            "difficultyAnalysis": difficulty_analysis,
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


    def calculate_difficulty_analysis(self, session, question_repository):
        analysis = {
            "Easy": {
                "attempted": 0,
                "correct": 0,
            },
            "Medium": {
                "attempted": 0,
                "correct": 0,
            },
            "Hard": {
                "attempted": 0,
                "correct": 0,
            },
        }

        for answer in session["answers"]:
            question = question_repository.get_question_by_id(
                answer["questionId"]
            )

            if question is None:
                continue

            difficulty = question["difficulty"]

            analysis[difficulty]["attempted"] += 1

            if answer["correct"]:
                analysis[difficulty]["correct"] += 1

        return analysis

    def calculate_question_difficulty_index(
            self,
            sessions,
            question_repository,
        ):
        stats = {}
        for session in sessions:
            for answer in session["answers"]:

                question = question_repository.get_question_by_id(
                            answer["questionId"]
                        )

                if question is None:
                    continue

                question_id = answer["questionId"]

                if question_id not in stats:
                    stats[question_id] = {
                        "questionId": question_id,
                        "attempts": 0,
                        "correct": 0,
                        "totalTime": 0,
                    }

                # These lines MUST be inside the answer loop
                stats[question_id]["attempts"] += 1
                stats[question_id]["totalTime"] += answer["timeTaken"]

                if answer["correct"]:
                    stats[question_id]["correct"] += 1
        result = []
        for question in stats.values():
            accuracy = (question["correct"]/question["attempts"]) * 100
            average_time = (question["totalTime"]/question["attempts"])
            difficulty_score = 100 - accuracy
            result.append({
                    "questionId": question["questionId"],
                    "attempts": question["attempts"],
                    "accuracy": round(accuracy,2),
                    "averageResponseTime": round(average_time,2,),
                    "difficultyScore": round(difficulty_score,2,),
                })
        result.sort(
                key=lambda question: question["difficultyScore"],
                reverse=True,
                )
        return result