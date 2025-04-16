# 🌦️ MCP-Style Weather Assistant (Clause + Tool Routing)

This is a simple example demonstrating how to simulate **Model Context Protocol (MCP)**-style orchestration using natural language queries and semantically selected tools — with **Claude desktop** acting as the LLM interface.

Instead of hardcoding which function to call in the prompt, the client (Clause or custom) **understands user intent** and automatically selects the appropriate tool from the available options.

---

## 🧠 What It Does

When a user types:

> “Is it raining in Mumbai right now?”

The client routes the request to:
```python
current_weather(location="Mumbai")
```

For a different query like:

> “Will it rain tomorrow in Delhi?”

It routes to:
```python
get_forecast(location="Delhi")
```

All without needing the user (or the prompt) to explicitly mention which function to call.

---

## 📦 Tools Available

| Tool Name           | Description                            |
|---------------------|----------------------------------------|
| `current_weather`   | Returns current weather for a location |
| `get_forecast`      | Returns forecasted weather             |

Each tool is defined as a function with a schema (input format + description).

---

## 🖥️ How It Works

### Option 1: 🧠 Using [Claude Desktop](https://github.com/johnlindquist/claude-desktop)
1. Launch Claude desktop
2. Load the `tools.json` schema (included)
3. Ask your question in natural language

Claude will pick the right tool to call based on its understanding of the goal.

---

### Option 2: 🧰 Use Your Own Client (Python)

If you don't use Claude, you can run the included script to simulate the same routing behavior locally:

```bash
uv run mcp-client/client.py weather/weather.py
```

This script uses a mock LLM decision logic to choose the correct tool and print the simulated response.

---

## 📁 Files Included

| File                      | Purpose                                          |
|---------------------------|--------------------------------------------------|
| `weather/tools.json`      | Tool/MCP Servers definitions                     |
| `mcp-client/client.py`    | Simple client to simulate routing                |
| `weather/weather_tools.py`| Mock implementation of tool functions            |
| `demo.mp4`                | Short screen recording of Clause in action       |

---

## 💡 What This Demonstrates

✅ Natural language queries → correct tool calls  
✅ Zero hardcoded logic inside the prompt  
✅ Modularity — tools can evolve independently  
✅ Foundation for real **MCP-style orchestration**

---

## 📚 Inspired By

- [Anthropic's tool use examples](https://docs.anthropic.com/)
- The concept of **Model Context Protocol (MCP)** for agent orchestration
- Clause Desktop as a low-code interface for fast prototyping

> Weather data/tools adapted for India 🌏

---

## 🚀 What's Next?

- Plug into real APIs (e.g., OpenWeatherMap)
- Expand tools (e.g., air quality, alerts)
- Add memory/context tracking
- Deploy via Streamlit or API

---

## 🤝 Contributions

Open to suggestions, extensions, or adaptations for other domains (banking, finance, travel, etc.)

---

## 📜 License

MIT License
