
import asyncio, json

class QuartBenchmark:
    """This class performs a variety of intensive common tasks on HTTP APIs.
    The methods are designed to operate independently of Quart imports,
    ensuring a clear separation between API logic and the Quart development flow.
    """

    async def json_serialization(self) -> str:
        """Generate a list with nested dicts that holds numbers, strings and booleans,
        then serialize it usin stdlib json module and returns that json string
        """
        data: list[dict] = [{'id': i,
                             'name': f'Name{i}',
                             'value': i*3.14} for i in range(50_000)]
        
        response: str = json.dumps(data)
        return response
