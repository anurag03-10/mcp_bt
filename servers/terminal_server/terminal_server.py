import os
import subprocess
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("terminal")

# Determine the workspace path based on whether running in Docker
if os.getenv("DOCKER_CONTAINER") == "true":
    DEFAULT_WORKSPACE = "/root/mcp/workspace"
else:
    DEFAULT_WORKSPACE = os.path.expanduser("/Users/anuragsingh/Krish Naik GenAI/mcp_bt/workspace")



@mcp.tool()
async def run_command(command: str) -> str:
    """Run a terminal command inside the workspace directory.
    If a terminal command is executed, the output will be returned as a string. If an error occurs, the error message will be returned instead.
    
    Args:
    the terminal command to be executed as a string.
    Returns:
        The command output or error message as a string.
    """
    try:
        result = subprocess.run(command, shell = True, cwd = DEFAULT_WORKSPACE, capture_output=True, text=True)
        return result.stdout or result.stderr
    except Exception as e:
        return str(e)
    

if __name__ == "__main__":
    mcp.run(transport='stdio')