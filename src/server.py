from collections.abc import Sequence
from mcp.server import Server
from mcp.types import Tool, TextContent
from typing import Any
import requests
import json
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-gold")
app = Server("mcp-gold")
api_key = os.getenv("GOLDAPI_API_KEY")

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name = "get_gold_price",
            description="Get current gold price in specified currency",
            inputSchema={
                "type": "object",
                "properties": {
                    "currency": {
                        "type": "string",
                        "description": "Currency code (ISO 4217 format e.g. USD, EUR)",
                        "default": "USD"
                    },
                    "metal": {
                        "type": "string",
                        "description": "Metal symbol (XAU, XAG, XPT, XPD)",
                        "default": "XAU"
                    },
                    "date": {
                        "type": "string",
                        "description": "Historical date (YYYYMMDD format, optional)",
                        "default": ""
                    }
                },
                "required": ["currency","metal"]
            }
        )
        ]

@app.call_tool()
def call_tool(name: str, arguments: Any) -> Sequence[TextContent]:
    if not isinstance(arguments, dict):
        raise RuntimeError("arguments must be dictionary")

    if name != "get_gold_price":
        raise RuntimeError(f"Unknown tool: {name}")

    currency = arguments.get("currency", "USD")
    metal = arguments.get("metal", "XAU")
    date = arguments.get("date", "")

    base_url = f"https://www.goldapi.io/api/{metal}/{currency}"
    url = f"{base_url}/{date}" if date else base_url
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return {
            "content": [{
                "type": "text",
                "text": json.dumps(response.json(), indent=2)
            }]
        }
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Gold API error: {str(e)}")

async def main():
    if not api_key:
        raise RuntimeError("Server not properly initialized - GOLDAPI_API_KEY missing, the variable is required")

    from mcp.server.stdio import stdio_server

    try:
        async with stdio_server() as (read_stream, write_stream):
            await app.run(
                read_stream,
                write_stream,
                app.create_initialization_options()
            )
    except KeyboardInterrupt:
        logging.info("Received KeyboardInterrupt, shutting down...")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
