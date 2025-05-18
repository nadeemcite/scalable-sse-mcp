from fastapi import FastAPI, Query, HTTPException
from uuid import uuid4
from typing import Optional
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

app = FastAPI()

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

app.mount("/", mcp.sse_app())

# # Dictionary to keep count per session id
# session_counter = {}

# @app.get("/")
# def get_uuid():
#     random_id = str(uuid4())
#     session_counter[random_id] = 0  # Initialize count
#     return {"id": random_id}

# @app.get("/counter")
# def get_counter(sessionid: Optional[str] = Query(None)):
#     if not sessionid or sessionid not in session_counter:
#         raise HTTPException(status_code=400, detail="Invalid or missing sessionid")
#     session_counter[sessionid] += 1
#     return {"sessionid": sessionid, "count": session_counter[sessionid]}