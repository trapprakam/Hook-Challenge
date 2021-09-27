from operation import Operation
from condition import Condition


class ConditionBuilder:

    def __init__(self):
        """
        Implements the builder pattern to build an sql where clause condition
        """
        self.__name_of_column = ''
        self.__argument1 = None
        self.__argument2 = None
        self.__operation1 = None
        self.__operation2 = None

    def column_name(self, name: str) -> 'ConditionBuilder':
        """
        Set the column name for the condition
        :param name: Name of the column
        :return: ConditionBuilder object
        """
        self.__name_of_column = name
        return self

    def first_argument(self, arg) -> 'ConditionBuilder':
        """
        Set an argument for the condition
        :param arg: A argument
        :return: ConditionBuilder object
        """
        self.__argument1 = arg
        return self

    def second_argument(self, arg) -> 'ConditionBuilder':
        """
        Set a second argument for the condition
        :param arg: A second argument
        :return: ConditionBuilder object
        """
        self.__argument2 = arg
        return self

    def operation_1(self, operation: 'Operation') -> 'ConditionBuilder':
        """
        Set a operation for the condition
        :param operation: A operation
        :return: ConditionBuilder object
        """
        self.__operation1 = operation
        return self

    def operation_2(self, operation: 'Operation') -> 'ConditionBuilder':
        """
        Set a second operation for the condition
        :param operation: A second operation
        :return: ConditionBuilder object
        """
        self.__operation2 = operation
        return self

    def build(self) -> 'Condition':
        """
        Build and return a Condition object
        :return: Condition object
        """
        return Condition(column_name=self.__name_of_column,
                         first_argument=self.__argument1,
                         second_argument=self.__argument2,
                         operation_1=self.__operation1,
                         operation_2=self.__operation2)
