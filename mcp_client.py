import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server_params = StdioServerParameters(
        command="npx",
        args=[
            "-y",
            "@microsoft/postgres-mcp",
            "run",
        ],
        env=None,
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            print("PostgreSQL MCPに接続しました")

            result = await session.list_tools()

            print(f"利用可能なツール数: {len(result.tools)}")

            for tool in result.tools:
                print(f"- {tool.name}")


if __name__ == "__main__":
    asyncio.run(main())