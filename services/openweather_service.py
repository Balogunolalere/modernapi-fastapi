
from typing import Optional
import httpx

api_key: Optional[str] = None

async def get_report_async(city: str, state: Optional[str], country: str, units: str) -> dict:
    if state:
        q = f'{city},{state},{country}'
    else:
        q = f'{city},{country}'
    # perform  get request on opeweatherapi
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}'
    
    async with httpx.AsyncClient() as Client:
        resp = await Client.get(url)
        resp.raise_for_status()

    data = resp.json()
    #forecast = data['main']
    return data

