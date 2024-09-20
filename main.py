import json

qwestion_1={ "q":"1111",
             "a":"1111"
             }


class qwest1():
    def __init__(self, text, diff, cor_answer, points):
        self.text = text
        self.diff = diff
        self.score = points
        self.answer = input(1111)
        self.qwestion_answered = False
        self.alr_ans = False
        self.correct_ans = cor_answer

    def build_qwestion(self):
        json_qwestion1 = json.dumps(qwestion_1)
        qwestion1 = json.loads(json_qwestion1)
        print('diff 1/5')

    def is_correct(self):
        if self.correct_ans == self.answer:
            return True
        else:
            return False

    def points(self):
        if self.is_correct == True:
            return self.diff * 10
        else:
            return self.diff - 1

    def feedback(self):
        if self.is_correct == True:
            return print('correct', self.points())
        else:
            return print('incorect', self.correct_ans)


print(qwest1)









