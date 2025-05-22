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

@app.get("/counter")
def get_counter():
    return {"sessionid": "hello"}

@app.get("/")
def get_counter():
    return {"success": True}

app.mount("/", mcp.sse_app())
