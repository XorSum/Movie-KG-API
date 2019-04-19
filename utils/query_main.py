from utils.fuseki import FusekiClient
from utils.Question2Sparql import Question2Sparql
from KnowGraphAPI import settings
from utils.question_temp import SPARQL_PREXIX

# URL_PREFIX = "http://editme.top#"

class AMI:
    """
    Artificial Mentally Retardation
    """

    def __init__(self, external_dict=settings.external_dict):
        self.fuseki = FusekiClient()
        self.q2s = Question2Sparql(external_dict)

    def query(self, question):
        try:
            my_query = self.q2s.get_sparql(question)
            print(my_query)
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

    def relationTo(self, subject):
        try:
            SPARQL_SELECT_TEM = "{prefix}\n" \
                                "SELECT DISTINCT ?predicate  ?object WHERE {{\n" \
                                "<{subject}>  ?predicate  ?object.\n" \
                                "}}\n"
            sql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX, subject=subject)
            print(sql)
            result = self.fuseki.query_results(sql)
            print(result)
            return result
        except Exception as e:
            print(e)
            return "error"

    def relationFrom(self, object):
        try:
            SPARQL_SELECT_TEM = "{prefix}\n" \
                                "SELECT DISTINCT  ?subject ?predicate  WHERE {{\n" \
                                "?subject  ?predicate  <{object}>.\n" \
                                "}}\n"
            sql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX, object=object)
            print(sql)
            result = self.fuseki.query_results(sql)
            print(result)
            return result
        except Exception as e:
            print(e)
            return "error"

    def getUrl(self, value):
        try:
            SPARQL_SELECT_TEM = "{prefix}\n" \
                                "SELECT DISTINCT  ?subject  WHERE {{\n" \
                                "{{?subject  :personName  '{value}'.}} UNION \n " \
                                "{{?subject  :personEnglishName  '{value}'.}} UNION \n " \
                                "{{?subject  :movieTitle  '{value}'.}} UNION \n " \
                                "{{?subject  :genreName   '{value}'.}}  \n " \
                                "}}\n"
            sql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX, value=value)
            print(sql)
            result = self.fuseki.query_results(sql)
            print(result)
            result = result['results']['bindings'][0]['subject']['value']
            print(result)
            return result
        except Exception as e:
            print(e)
            return "error"

    def getName(self, value):
        try:
            SPARQL_SELECT_TEM = "{prefix}\n" \
                                "SELECT DISTINCT  ?object  WHERE {{\n" \
                                "{{<{value}>  :personName  ?object.}} UNION \n " \
                                "{{<{value}>  :personEnglishName  ?object.}} UNION \n " \
                                "{{<{value}>  :movieTitle  ?object.}} UNION \n " \
                                "{{<{value}>  :genreName   ?object.}}  \n " \
                                "}}\n"
            sql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX, value=value)
            print(sql)
            result = self.fuseki.query_results(sql)
            print(result)
            ans = result['results']['bindings'][0]['object']['value']
            print(ans)
            return ans
        except Exception as e:
            print(e)
            return "error"


# 用于测试
if __name__ == '__main__':
    external_dict = ['./external_dict/movie_title.txt', './external_dict/person_name.txt']
    ami = AMI(external_dict)
    print(ami.query("周星驰出演的电影"))
    print(ami.relationTo("http://editme.top#movie/231017"))
    print(ami.relationFrom("http://editme.top#movie/231017"))
    print(ami.getUrl("周星驰"))
    print(ami.getName("http://editme.top#movie/231017"))
