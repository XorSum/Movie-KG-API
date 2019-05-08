import SPARQLWrapper
from SPARQLWrapper import JSON

from MovieKgAPI.settings import FUSEKI_ENDPOINT_URL


class FusekiClient:

    def __init__(self):
        self.sparql_conn = SPARQLWrapper.SPARQLWrapper(FUSEKI_ENDPOINT_URL)
        self.sparql_conn.setReturnFormat(JSON)

    def query_results(self, statement):
        try:
            self.sparql_conn.setQuery(statement)
            results = self.sparql_conn.query().convert()
            return results
        except:
            return None

    def query_values(self, statement):
        try:
            self.sparql_conn.setQuery(statement)
            results = self.sparql_conn.query().convert()
            values = []
            for result in results["results"]["bindings"]:
                for key in results["head"]["vars"]:
                    values.append(result[key]["value"])
            return values
        except:
            return None

#  用于测试
if __name__ == '__main__':
    statement = """
    PREFIX : <http://editme.top#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT DISTINCT ?x WHERE {
    ?s :personName '周星驰'.
    ?s :hasActedIn ?m.
    ?m :movieTitle ?x
    }
    limit 10
    """
    fuseki_client = FusekiClient()

    results = fuseki_client.query_results(statement)
    print(results)

    values = fuseki_client.query_values(statement)
    print(values)
