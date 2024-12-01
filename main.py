import os, json
from quart import Quart, Response
from dotenv import load_dotenv
api = Quart(__name__)

load_dotenv()

@api.route('/')
async def hello():
    response_body = json.dumps({
        'status': 'success',
        'code': 200,
        'api_info': {
            'proyecto': 'Quart Benchmark API',
            'descripcion': 'API con tareas intensivas comunes para testear el rendimiento de Quart',
            'version': os.getenv('API_VERSION'),
            'author': 'Daniel Limón',
            'email': 'dani@dlimon.net'
        } 
    })
    return Response(response=response_body,
                    status=200,
                    mimetype='application/json')