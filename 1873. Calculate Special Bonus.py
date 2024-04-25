import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    condition = (employees['employee_id']%2!=0) & (employees['name'].str[0]!='M')
    employees['bonus'] = employees[condition][['salary']]
    employees.fillna(value = 0,inplace = True)
    employees = employees.sort_values('employee_id')
    return employees[['employee_id','bonus']]