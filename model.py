from pydantic import BaseModel


class DashboardFilterModel(BaseModel):
    symbol: str | None = None,
    nifty_50: bool | None = None,
    nifty_it: bool | None = None,
    nifty_bank: bool | None = None,
    industry: str | None = None,
    score_filter: float | None = None,
    avg_total_score_filter: float | None = None,
    deliverable_percent_filter: float | None = None
