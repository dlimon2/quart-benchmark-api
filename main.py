import os, json
from dotenv import load_dotenv
from quart import Quart, Response

from _code.interfaces.quart_benchmark import QuartBenchmark

api = Quart(__name__)
benchmark = QuartBenchmark()

load_dotenv()

@api.get('/')
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


@api.get('/json-serialization')
async def json_serialization():
    response: str = await benchmark.json_serialization()
    return Response(response, 200, None, 'application/json')