"""
Exercise: Build REST API Client

TODO: Implement client with GET, POST, error handling
"""

import httpx
import asyncio

class RESTClient:
    """Async REST API client."""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
    
    async def get(self, endpoint: str):
        # TODO: Implement GET
        pass
    
    async def post(self, endpoint: str, data: dict):
        # TODO: Implement POST
        pass

if __name__ == "__main__":
    print("TODO: Implement REST client")
