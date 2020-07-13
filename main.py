from wellandcanalbridges import WellandCanalBridges
import asyncio

async def main():
  api_client = WellandCanalBridges()

  success = await api_client.get_bridge_status()

  print(success)

asyncio.run(main())