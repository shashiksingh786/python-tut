import uvicorn
from fastapi import FastAPI
from fastapi.params import Body
from fastapi.middleware.cors import CORSMiddleware
from model import DashboardFilterModel
import trades
import pyodbc


app = FastAPI(title="Fast API - Trading Trial",
              description="TradingTrial API",
              version="1.0")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

con_str = ("Driver={SQL Server Native Client 11.0};"
           "Server=SHASHI-DELL5620;"
           "Database=TradingTrial;"
           "Trusted_Connection=yes;")

try:
    conn = pyodbc.connect(con_str)
except pyodbc.Error as e:
    print(e)
    exit()

 
@app.get("/")
def root():
    return {"message": "welcome to my first python api"}


@app.get("/gettoplist")
async def get_data():
    return trades.fetch_data(conn)


@app.get("/getIndustryList")
async def get_industry_list():
    return trades.get_industry_list(conn)


@app.post("/dashboard")
async def get_dashboard_data(model: DashboardFilterModel):
    return trades.get_dashboard_data(conn, model)


@app.post("/symboldetails")
async def get_dashboard_data(modal: DashboardFilterModel):
    return trades.get_symbol_data(conn, modal.symbol)


# @app.get("/createpost") = Body(..., embed=True)
# def create_post(payload: dict = Body(...)):
#     return {"message": "welcome to my first python api"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port="8080")
