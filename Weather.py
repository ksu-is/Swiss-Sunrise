import pyfiglet,python_weather,platform
import asyncio,os
if platform.system() == "Windows":
    def clear(): os.system("cls")
else:
    def clear(): os.system("clear")
async def getweather():
    Celsius = 0
    y = input("Select the metric system:\n1)Celsius\n2)Farenheit\n")
    if y == "1":
        Celsius += 1
    clear()
    ascii_banner = pyfiglet.figlet_format("Weather")
    print(ascii_banner)
    print("By Kirito071008")
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
      x = input("Enter the city name: ")
      weather = await client.get(f'{x}')
      z = (weather.current.temperature-32)*(5/9)
      z1 = (weather.current.temperature)
      if Celsius == 1:
        print(f"Temperature: {round(z)}°C")
      else:
         print(f"Temperature: {z1}°F")
asyncio.run(getweather())
