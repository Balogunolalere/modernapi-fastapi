import fastapi
from pathlib import Path
import uvicorn
from api import weather_api
from views import home
import json
from services import openweather_service

api = fastapi.FastAPI()

def configure():
    configure_routing()
    configure_api_keys()

def configure_api_keys():
    file = Path('settings.json').absolute()
    if not file.exists():
        print(f'warning {file} file not found, please see settings_template.json')
        raise Exception('settings.json not found, see settings_template.json as exampple')

    with open('settings.json') as fin:
        settings = json.load(fin)
        openweather_service.api_key = settings.get('api_key')


def configure_routing():
    api.include_router(home.router)
    api.include_router(weather_api.router)



if __name__ == '__main__':
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
    configure()
