from condition import Condition


class SQLQuery:

    def __init__(self, select_statement: str, table: str, condition: 'Condition'):
        """
        This class represents a sql query
        :param select_statement: A sql select statement
        :param table: The table to be query
        :param condition: A where clause condition
        """
        self.select_statement = select_statement
        self.table = table
        self.condition = condition

    def get_query(self) -> str:
        """
        Returns a sql query
        :return: A sql query
        """
        query = f"select {self.select_statement} " \
                f"from {self.table} " \
                f"where {self.condition.get_condition()}"
        return query
