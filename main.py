import директория_db
from people import get_jobs
from salary import calculate_salary as cs
import datetime as dt




if __name__ == '__main__':
    db = директория_db.dict_staff()
    ALL = get_jobs(db)
    print(cs(ALL),'\n', dt.date.today())
    
    