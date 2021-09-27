from typing import Union, List
from condition import Condition
from sqlquery import SQLQuery


class SQLQueryBuilder:

    def __init__(self):
        """
        Implements the builder pattern to build a sql query
        """
        self.__to_select = ''
        self.__table_name = ''
        self.__condition = None

    def select(self, args: Union[str, List[str]]) -> 'SQLQueryBuilder':
        """
        Set the select statement for the query
        :param args: A select statement
        :return: A SQLQueryBuilder
        """
        if isinstance(args, list):
            self.__to_select = ', '.join(args).lower()
        self.__to_select = args.lower()
        return self

    def from_table(self, table_name: str) -> 'SQLQueryBuilder':
        """
        Set the table name for the query
        :param table_name: The name of the table
        :return: A SQLQueryBuilder
        """
        self.__table_name = table_name.lower()
        return self

    def where(self, condition: 'Condition') -> 'SQLQueryBuilder':
        """
        Set the where clause condition for the query
        :param condition: A where clause condition
        :return: A SQLQueryBuilder
        """
        self.__condition = condition
        return self

    def and_where(self, condition: 'Condition') -> 'SQLQueryBuilder':
        """
        This function is only here to showcase what could be added
        :param condition:
        :return:
        """
        pass
        # Below is code I will not leave in a final work
        # this is to indicate that sql builder could be expanded to
        # add where and operator
        # self.__conditions.append(condition)
        # return self

    def or_where(self, condition: 'Condition') -> 'SQLQueryBuilder':
        """
        This function is only here to showcase what could be added
        :param condition:
        :return:
        """
        pass
        # Below is code I will not leave in a final work
        # this is to indicate that sql builder could be expanded to
        # add where and operator
        # self.__conditions.append(condition)
        # return self

    def not_where(self, condition: 'Condition') -> 'SQLQueryBuilder':
        """
        This function is only here to showcase what could be added
        :param condition:
        :return:
        """
        pass
        # Below is code I will not leave in a final work
        # this is to indicate that sql builder could be expanded to
        # add where and operator
        # self.__conditions.append(condition)
        # return self

    def build(self) -> 'SQLQuery':
        """
        Build and return a SQLQuery object
        :return: SQLQuery object
        """
        return SQLQuery(select_statement=self.__to_select,
                        table=self.__table_name,
                        condition=self.__condition)

