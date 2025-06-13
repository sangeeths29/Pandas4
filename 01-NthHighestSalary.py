# Problem 1 - Nth Highest Salary (https://leetcode.com/problems/nth-highest-salary/solution/)
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Dropping duplicate salaries from table
    df = employee[['salary']].drop_duplicates()

    # Returning null if N is greater than number of salaries in table or if N is less than or equal to 0
    if N > len(df) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})
    
    # Ordering salaries in descending order and returning the N top ones. The tail function filters out the distinct Nth highest salary
    return df.sort_values('salary', ascending = False).head(N).tail(1)[['salary']].rename(columns = {'salary':f'getNthHighestSalary({N})'})