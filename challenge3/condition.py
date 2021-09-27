from operation import Operation


class Condition:

    def __init__(self, column_name: str, first_argument, operation_1: 'Operation',
                 second_argument=None, operation_2: 'Operation' = None):
        """
        This class represents a sql where clause condition
        :param column_name: Name of the column
        :param first_argument: First argument to be express in the condition
        :param operation_1: Filter operator
        :param second_argument: Second (Optional) argument to be express in the condition
        :param operation_2: Second (Optional) Filter operator
        """
        self.column_name = column_name
        self.first_argument = first_argument
        self.second_argument = second_argument
        self.operation_1 = operation_1
        self.operation_2 = operation_2

    def get_condition(self) -> str:
        """
        Return the state of this condition
        :return: A string representation of a where clause condition
        """
        if self.operation_2 is not None and self.second_argument is not None:
            condition = f"{self.first_argument} {self.operation_1.value} {self.column_name} {self.operation_2.value}" \
                        f" {self.second_argument}"
            return condition
        return f"{self.column_name} {self.operation_1.value} {self.first_argument}"
