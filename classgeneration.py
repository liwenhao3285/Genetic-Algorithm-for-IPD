class generation:

    def __init__(self, number, generation_dic, score_dic):
        self.number = number
        self.generation_dic = generation_dic
        self.score_dic = score_dic

    def set_number(self, number):
        self.number = number
    
    def set_generation_dic(self, generation_dic):
        self.generation_dic = generation_dic
    
    def set_score_dic(self, score_dic):
        self.score_dic = score_dic

    def get_number(self):
        return self.number

    def get_generation_dic(self):
        return self.generation_dic

    def get_score_dic(self):
        return self.score_dic

    def __str__(self):
        return f'generation_dic: {self.generation_dic}\n' + f'Model: {self.number}\n' + f'score_dic: {self.score_dic}\n'