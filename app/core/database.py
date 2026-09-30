from neo4j import GraphDatabase
from app.core.config import settings

class Neo4jDatabase:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            settings.NEO4J_URI,
            auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
        )

    def verify_connection(self):
        self.driver.verify_connectivity()

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters):
        records,summary, keys = self.driver.execute_query(query, parameters)
        return [record.data() for record in records]

neo4j_db = Neo4jDatabase()