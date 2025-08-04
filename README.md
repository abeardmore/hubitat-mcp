# Hubitat MCP Server

This project exposes **Hubitat Maker API devices** to an MCP (Model Context Protocol) server so AI assistants like Claude Desktop can control your smart home.

It uses the [Hubitat Maker API](https://docs.hubitat.com/index.php?title=Maker_API) for device access and integrates with the [mcp-proxy](https://github.com/sparfenyuk/mcp-proxy) project.

---

## Features
- Lists Hubitat devices and their attributes
- Sends on/off and custom commands to devices
- Works with MCP-compatible assistants
- Lightweight, Python-based server

---

## Prerequisites
1. **Hubitat Hub** with [Maker API app](https://docs.hubitat.com/index.php?title=Maker_API) installed.
2. A [Hubitat Cloud Access Token](https://docs.hubitat.com/index.php?title=Maker_API#Cloud_Endpoint) and App ID.
3. Python 3.10+ installed.
4. MCP Proxy installed — [mcp-proxy GitHub repo](https://github.com/sparfenyuk/mcp-proxy).

---

## Installation
```bash
# Clone this repo
git clone https://github.com/abeardmore/hubitat-mcp.git
cd hubitat-mcp

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file with:
```bash
HUBITAT_BASE_URL=https://cloud.hubitat.com/api/<CLOUD_ID>/apps/<APP_ID>/devices
HUBITAT_TOKEN=<YOUR_ACCESS_TOKEN>
```

---

## Running the Server
```bash
python hubitat_mcp_server.py
```

The server will start on port `5005`. You can test:
```bash
curl http://localhost:5005/devices
```

---

## Connecting to MCP Proxy
Follow the [mcp-proxy setup instructions](https://github.com/sparfenyuk/mcp-proxy#readme) to point it to:
```
http://localhost:5005
```

Once configured, your MCP-enabled assistant should see Hubitat devices.

---

## License
MIT
