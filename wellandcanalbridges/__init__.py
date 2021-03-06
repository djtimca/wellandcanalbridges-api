import logging
import aiohttp

APIUrl = "https://canalstatus.com/api/v1/bridges/"

_LOGGER = logging.getLogger("wellandcanalbridges")

class WellandCanalBridges:
  def __init__(self):
    """Initialize and test the session"""
    self.retry = 5
    self._session = aiohttp.ClientSession()
  
  async def close(self):
    await self._session.close()

  async def get_bridge_status(self, bridge_id = None):
    # Retrieve Bridge Status JSON
    response = {}

    updateURL = APIUrl
    if not bridge_id is None:
      updateURL = updateURL + str(bridge_id)
    
    async with await self._session.get(updateURL) as resp:
      response = await resp.text()

    return response
