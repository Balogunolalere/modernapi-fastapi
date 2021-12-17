import fastapi

router = fastapi.APIRouter()

@router.get('/')
def index():
    return 'Hello Weather App'

@router.get('/favicon.ico')
def favicon():
    return fastapi.responses.RedirectResponse(url='/image/favicon.ico')