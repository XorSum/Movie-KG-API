
from utils import  question_temp
from utils import word_tagger


class Question2Sparql:
    def __init__(self, dict_paths):
        self.wordtagger = word_tagger.Tagger(dict_paths)
        self.rules = question_temp.rules

    def get_sparql(self, question):
        """
        进行语义解析，找到匹配的模板，返回对应的SPARQL查询语句
        如果有多个语句，返回匹配数量最多的语句
        :param question: str
        :return: sparql
        """
        word_objects = self.wordtagger.get_word_objects(question)
        match_num = 0
        query_ = None

        for rule in self.rules:
            query, num = rule.apply(word_objects)
            # print(query,num)
            if query is not None:
                if num > match_num:
                    query_ = query
                    match_num = num

        return query_
