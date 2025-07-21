###### MCP Servers: These act as bridges to connect APIs, databases, or code. They expose data sources as tools to the host and can be built using Python or TypeScript SDKs.
###### MCP Clients: These clients use the protocol to interact with MCP servers. Like servers, they can be developed using SDKs in Python or TypeScript.
###### MCP Hosts: These systems manage communication between servers and clients, ensuring smooth data exchange. Popular hosts include Claude Desktop, Zed, and Sourcegraph Cody.

## Setting Up an MCP Server
### Step 1: Install Dependencies
npm install

### Step 2: Write Boilerplate Code
src/index.ts

### Step 3: Define and Add Tools
server.setRequestHandler

### Step 4: Integrate with Claude Desktop
AppData\Roaming\Claude\claude_desktop_config.json

`
{
  "mcpServers": {
    "mcp-server": {
      "command": "node",
      "args": [
        "/Users/YOUR_USER/mcp-server/build/index.js"
      ]
    }
  }
}
`

### Read in more detail here

use claude to run the MCP server sample
https://modelcontextprotocol.io/introduction
https://hackteam.io/blog/build-your-first-mcp-server-with-typescript-in-under-10-minutes/
