# -*- coding: utf-8 -*-
"""
Created on Thu May 15 14:21:22 2025

@author: gael.kamdem.de.teyou
"""

import random

import requests
from mcp.server.fastmcp import FastMCP
import numpy as np

# Create server
mcp = FastMCP("Echo Server")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print(f"[debug-server] add({a}, {b})")
    return a + b


@mcp.tool()
def get_secret_word() -> str:
    print("[debug-server] get_secret_word()")
    return random.choice(["apple", "banana", "cherry"])


@mcp.tool()
def get_current_weather(city: str) -> str:
    print(f"[debug-server] get_current_weather({city})")

    endpoint = "https://wttr.in"
    response = requests.get(f"{endpoint}/{city}")
    return response.text


@mcp.tool()
async def tierce_racine(i: int) -> float:
    
    """Calculate the tierce racine of a given integer number.

    Args:
        i: The integer we want to calculate the tierce racine.
    """

    return float(10*np.sqrt(i))


@mcp.tool() 
async def bahamisation(i: float) -> int:
    
    """Calculate the bahamisation of a given number.

    Args:
        i: The number we want to calculate the bahamisation.
    """

    return int(10*i)


if __name__ == "__main__":
    mcp.run(transport="sse")
    #mcp.run(transport="stdio")