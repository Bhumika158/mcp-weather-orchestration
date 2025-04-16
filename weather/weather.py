from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather")

# Constants
OWM_API_BASE = "https://api.openweathermap.org/data/2.5"
API_KEY="23da6a7acc523b4744f14d0b60ce25bf"
USER_AGENT = "india-weather-app/1.0"

async def make_owm_request(url: str) -> dict[str, Any] | None:
    """Make a request to the OWM API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            print(f"Error in OWM request: {e}")
            return None


@mcp.tool()
async def get_current_weather(city: str = "Hyderabad") -> str:
    """Get current weather for an Indian city.

    Args:
        city: Name of the city (default is Hyderabad)
    """
    url = (
        f"{OWM_API_BASE}/weather?q={city},IN&appid={API_KEY}&units=metric"
    )
    data = await make_owm_request(url)

    if not data:
        return f"Unable to fetch current weather for {city}."
    if data.get("cod") == "404":
        return f"City '{city}' not found."
    main = data.get("main", {})
    wind = data.get("wind", {})
    weather = data.get("weather", [{}])[0]

    return f"""
Current Weather in {city}:
Temperature: {main.get('temp', '?')}°C
Feels Like: {main.get('feels_like', '?')}°C
Condition: {weather.get('description', 'Unknown').capitalize()}
Humidity: {main.get('humidity', '?')}%
Wind: {wind.get('speed', '?')} m/s
"""


@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """Get 3-hour interval weather forecast for a location in India."""
    forecast_url = (
        f"{OWM_API_BASE}/forecast?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric"
    )
    forecast_data = await make_owm_request(forecast_url)

    if not forecast_data or "list" not in forecast_data:
        return "Unable to fetch forecast data."

    forecasts = []
    for entry in forecast_data["list"][:5]:  # Get next 5 forecast entries (~15 hours)
        dt_txt = entry["dt_txt"]
        temp = entry["main"]["temp"]
        weather = entry["weather"][0]["description"]
        wind_speed = entry["wind"]["speed"]
        wind_deg = entry["wind"]["deg"]
        forecast = f"""
Time: {dt_txt}
Temperature: {temp}°C
Weather: {weather}
Wind: {wind_speed} m/s at {wind_deg}°
"""
        forecasts.append(forecast)

    return "\n---\n".join(forecasts)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')