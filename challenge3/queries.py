from operation import Operation
from conditionbuilder import ConditionBuilder
from sqlquerybuilder import SQLQueryBuilder

# Query: 2 < rating < 9
query = SQLQueryBuilder()\
                       .select('rating')\
                       .from_table('test_table')\
                       .where(ConditionBuilder()
                              .first_argument(2)
                              .operation_1(Operation.LESS_THAN)
                              .column_name('rating')
                              .operation_2(Operation.LESS_THAN)
                              .second_argument(9)
                              .build())\
       .build().get_query()

print(f"Query for ratings greater than 2 and less than 9: {query}")

# Query: id in list
query = SQLQueryBuilder()\
                       .select('id')\
                       .from_table('test_table')\
                       .where(ConditionBuilder()
                              .column_name('id')
                              .operation_1(Operation.IN)
                              .first_argument(['1234', '5678', '9'])
                              .build())\
       .build().get_query()

print(f"Query for id in list: {query}")


# Query: date > 1 Jan 2016
query = SQLQueryBuilder()\
                       .select('date')\
                       .from_table('test_table')\
                       .where(ConditionBuilder()
                              .column_name('date')
                              .operation_1(Operation.GREATER_THAN)
                              .first_argument('1 Jan 2016')
                              .build())\
       .build().get_query()

print(f"Query for date > 1 Jan 2016: {query}")
