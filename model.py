from pydantic import BaseModel


class DashboardFilterModel(BaseModel):
    symbol: str | None = None
    
