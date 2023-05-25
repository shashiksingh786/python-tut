
import pandas as pd
import pyodbc
from model import DashboardFilterModel

# Function to return the sql results as a dict.
# It also maps the column names and values for the dict
# Returns no results found if there are no records


def mssql_result2dict(cursor):
    try:
        result = []
        columns = [column[0] for column in cursor.description]
        for row in cursor.fetchall():
            result.append(dict(zip(columns, row)))

        # print(result)

        # Check for results
        if len(result) > 0:
            ret = result
        else:
            ret = {"message": "no results found"}
    except pyodbc.Error as e:
        print(e)
        ret = {"message": "Internal Database Query Error"}

    return ret


def fetch_data(con):
    query = 'select top 10 * from [TRADE_TBL_FULLBHAV_DATA_SUMMARISED]'
    try:
        cursor = con.cursor()
        cursor.execute(query)
        ret = mssql_result2dict(cursor)
        con.commit()
    except pyodbc.Error as e:
        print(f'SQL Query Failed: {e}')
        ret = {"message": "system error"}

    return ret


def get_industry_list(con):
    query = 'select distinct industry from [TRADE_TBL_NIFTY_500_LIST]'
    try:
        cursor = con.cursor()
        cursor.execute(query)
        ret = mssql_result2dict(cursor)
        con.commit()
    except pyodbc.Error as e:
        print(f'SQL Query Failed: {e}')
        ret = {"message": "system error"}

    return ret


def get_dashboard_data(con, model:DashboardFilterModel):
    # sql = 'exec TradingTrial.[dbo].[TRADE_USP_WEB_DASHBOARD_SYMBOL](?,?,?,?,?,?,?,?)'
    # values = ('HDFC', '', '', '', '', '', '', '')
    try:
        cursor = con.cursor()
        cursor.execute(
            "{CALL [TRADE_USP_WEB_DASHBOARD_SYMBOL](?,?,?,?,?,?,?,?)}", (model.symbol, '', '', '', '', 0, 0, 0))
        ret = mssql_result2dict(cursor)
        con.commit()
    except pyodbc.Error as e:
        print(f'SQL Query Failed: {e}')
        ret = {"message": f'{e}'}

    return ret
