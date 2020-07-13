import logging
import aiohttp

APIUrl = "https://canalstatus.com/api/v1/bridges/"

_LOGGER = logging.getLogger("wellandcanalbridges")

class WellandCanalBridges:
  def __init__(self):
    self._session = aiohttp.ClientSession()
    self.retry = 5

  async def get_bridge_status(self):
    # Retrieve Bridge Status JSON
    response = {}
    
    async with self._session.get(APIUrl) as resp:
      response = await resp.text()

    await self._session.close()

    return response
