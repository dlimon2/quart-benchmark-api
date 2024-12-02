
import asyncio, json
from typing import List, Dict, Union

ComplexList = List[Dict[str,
                        Union[int, str, float]]]

class QuartBenchmark:
    """This class performs a variety of intensive common tasks on HTTP APIs.
    The methods are designed to operate independently of Quart imports,
    ensuring a clear separation between API logic and the Quart development flow.
    """

    async def json_serialization(self) -> str:
        """Generate a list with nested dicts that holds int, float and strings,
        then serialize it usin stdlib json module and returns that json string
        """
        data: ComplexList = [{
                             'id': i,
                             'name': f'Name{i}',
                             'value': i*3.14} for i in range(50_000)]
        
        response: str = json.dumps(data)
        return response


    async def cpu_intensive(self,
                            task: str = 'factorize') -> Union[List[int]]:
        """Simulates intensive operations related to cryptography. Calculates
        divisor from a large number. This is ideal for testing intensive math performance.
        """
        if task == 'factorize':
            return await self.__factorize()


    async def multiple_requests(self) -> str:
        """Lightweight operation. Creates a response dictionary, then json-serialize it
        and return the json string.
        """
        response: Dict[str, str] = {
            'message': 'This is a concurrent request test.'
        }
        return json.dumps(response)
        

    async def __factorize(self,
                          number: int = 777**5) -> List[int]:
        """Calculate all factors of a given number.

        Finds all factors of the :number: by interating from 1to the square
        root of :number:. For each divisor found, it  adds both the divisor
        and its complement to the result list, all factor are included.
        The result list is then sorted before returned

        Args:
            :number: (int): The number to find de factors for. Default 777^5

        Returns:
            List[int]: A sorted list of all factors of :number:
        """
        factors: List[int] = []
        for i in range(1, int(number**0.5) +1):
            if number % i == 0:
                factors.append(i)
                if i != number // i:
                    factors.append(number // i)
        return sorted(factors)

                          
