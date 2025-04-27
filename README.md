[![MseeP Badge](https://mseep.net/pr/isdaniel-mcp-metal-price-badge.jpg)](https://mseep.ai/app/isdaniel-mcp-metal-price)


[![smithery badge](https://smithery.ai/badge/@isdaniel/mcp-metal-price)](https://smithery.ai/server/@isdaniel/mcp-metal-price)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/mcp-metal-price)](https://pypi.org/project/mcp-metal-price/)
[![PyPI - Version](https://img.shields.io/pypi/v/mcp-metal-price)](https://pypi.org/project/mcp-metal-price/)
[![Verified on MseeP](https://mseep.ai/badge.svg)](https://mseep.ai/app/d60d18a5-d88e-4dea-bc16-00bbf1c0463a)

# Metal Price MCP Server

An MCP server that provides current and historical gold/precious metal prices via the [GoldAPI.io](https://www.goldapi.io/) service.

## Features

- Get current prices for gold (XAU), silver (XAG), platinum (XPT), and palladium (XPD)
- Support for multiple currencies (USD, EUR, etc.)
- Optional historical price lookup by date

## Requirements

- Python 3.7+
- Packages:
  - `mcp>=1.0.0`
  - `requests>=2.31.0`

## Setup

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your GoldAPI.io API key as an environment variable:
   ```bash
   export GOLDAPI_API_KEY="your_api_key_here"
   ```
   (Windows users: use `set` instead of `export`)

## Usage

The server provides one MCP tool:

## Installation

This server is designed to be installed manually by adding its configuration to the `cline_mcp_settings.json` file.

1.  Add the following entry to the `mcpServers` object in your `cline_mcp_settings.json` file:

```json
"mcp_metal_price": {
  "args": [
    "/c",
    "python",
    "-m",
    "mcp_metal_price"
  ],
  "env": {
    "GOLDAPI_API_KEY": "Your GOLDAPI_API_KEY"
  }
}
```

### get_gold_price
Get current or historical metal prices.

**Parameters:**
- `currency` (string, default: "USD"): Currency code (ISO 4217 format)
- `metal` (string, default: "XAU"): Metal symbol (XAU, XAG, XPT, XPD)
- `date` (string, optional): Historical date in YYYYMMDD format

**Example Usage:**
```json
{
  "currency": "EUR",
  "metal": "XAU"
}
```

## Running the Server

Start the server with:
```bash
python src/server.py
```

## Using with MCP Clients

Once the server is running, you can connect to it from MCP clients like Cline or Claude.

### Connecting to the Server
The server runs on stdio by default. In your MCP client, you can connect using:
```bash
cmd /c python src/server.py
```

### Using the get_gold_price Tool
Example tool usage in Cline/Claude:
```xml
<use_mcp_tool>
<server_name>gold-price</server_name>
<tool_name>get_gold_price</tool_name>
<arguments>
{
  "currency": "USD",
  "metal": "XAU"
}
</arguments>
</use_mcp_tool>
```


### Response Format
The server returns price data in JSON format:
```json
{
  "timestamp": 1713600000,
  "metal": "XAU",
  "currency": "USD",
  "price": 2345.67,
  "unit": "per troy ounce"
}
```

## License

This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) file for details.
