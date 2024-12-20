import os, json
from dotenv import load_dotenv
from quart import Quart, Response, request
from typing import List

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


@api.get('/cpu-intensive')
async def cpu_intensive():
    if not request.args:
        task: str = 'factorize'
    else:
        task: str = request.args.get('task')
    result: List[int] = await benchmark.cpu_intensive(task)
    response: str = json.dumps({ 'factors': result })
    return Response(response, 200, None, 'application/json')


@api.get('/multiple-requests')
async def multiple_requests():
    """This endpoint must be tested with tools like wrk or locust
    to generate thousands of concurrent requests."""
    response = await benchmark.multiple_requests()
    return Response(response, 200, None, 'application/json')


@api.post('/data-transformation')
async def data_transformation():
    """This endpoint must be tested with a large JSON payload on
    POST request.
    JSON List body:
        List[Dict[str, int]] (key values must be called 'value'):
            -value (int): A number between 0 and 200
    Returns:
        Response: JSON response with filtered values.
    """
    json_data: str = await request.get_data(as_text=True)
    response = await benchmark.data_transformation(json_data)
    return response 