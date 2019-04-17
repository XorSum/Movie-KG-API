
from utils.fuseki import  FusekiClient
from utils.Question2Sparql import Question2Sparql
from KnowGraphAPI import settings

class  AMI :
    """
    Artificial Mentally Retardation
    """
    def __init__(self,external_dict = settings.external_dict):
        self.fuseki =  FusekiClient()
        self.q2s = Question2Sparql(external_dict)

    def query(self,question):
        try:
            my_query = self.q2s.get_sparql(question)
            # print(my_query)
            if my_query != None:
                result = self.fuseki.query_values(my_query)
                if (len(result) == 0):
                    return "I don't know"
                else:
                    return result
            else:
                return "I can't understand"
        except Exception as e:
            print(e)
            return "error"

# 用于测试
if __name__ == '__main__':
    external_dict = ['./external_dict/movie_title.txt', './external_dict/person_name.txt']
    ami = AMI(external_dict)
    print(ami.query("周星驰出演的电影"))
