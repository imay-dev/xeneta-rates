from fastapi import APIRouter
from typing import Union, List
from pydantic import BaseModel
from databases import Database
from datetime import date


router = APIRouter()

class Item(BaseModel):
    day: date
    average_price: Union[int, None] = None


@router.get("/")
async def get(
    date_from:      date,
    date_to:        date,
    origin:         str,
    destination:    str
) -> List[Item] :
    
    database = Database('postgresql://postgres:postgres@rates_db:5432/postgres')
    await database.connect()
        
    query: str = """
        SELECT
            day,
            (CASE WHEN COUNT(price) >= 3 THEN ROUND(AVG(price)) ELSE null END) average_price
        FROM prices pr
            JOIN ports p ON
                pr.orig_code  = p.code
                OR pr.dest_code = p.code 
            JOIN regions r ON
                p.parent_slug = r.slug
        WHERE (
                pr.orig_code = '{0}'
                OR p.parent_slug = '{0}'
                OR r.parent_slug = '{0}'
            ) AND (
                pr.dest_code = '{1}'
                OR p.parent_slug = '{1}'
                OR r.parent_slug = '{1}'
            )
            AND day >= '{2}'
            AND day <= '{3}'
        GROUP BY day
        ORDER BY day;
    """.format(origin, destination, date_from, date_to)

    return await database.fetch_all(query = query)
    
