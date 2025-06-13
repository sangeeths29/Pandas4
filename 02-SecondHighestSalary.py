# Problem 2 - Second Highest Salary ( https://leetcode.com/problems/second-highest-salary/ )
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Dropping duplicate salary values
    df = employee[['salary']].drop_duplicates()
    # Returning None if number of salaries is less than 2
    if len(df) < 2:
        return pd.DataFrame({'SecondHighestSalary' : [None]})
    # Returning 2nd Highest Salary
    return df.sort_values('salary', ascending = False).head(2).tail(1)[['salary']].rename(columns = {'salary':'SecondHighestSalary'})
