"""
examples.py
-----------
This file demonstrates how to use the core Minecraft formulas from formulas.py.
You'll find examples for:
- Chunk coordinate and center calculations
- Slime chunk detection
- Direction and distance calculations
- How to integrate these formulas into a Discord slash command (pseudo-code)
- How to use them in other Python scripts

All examples are written for clarity and practical use.
"""

import formulas

# --- Example 1: Chunk coordinate and center calculation ---
# Suppose you have a block position (x, z) in your Minecraft world:
x, z = 123, 456
chunk_x, chunk_z = formulas.get_chunk_coords(x, z)
print(f"Block ({x}, {z}) is in chunk ({chunk_x}, {chunk_z})")

center_x, center_z = formulas.get_chunk_center(x, z)
print(f"The center of this chunk is at block ({center_x}, {center_z})")

corners = formulas.get_chunk_corners(x, z)
print("Chunk corners (NW, NE, SW, SE):", corners)

# --- Example 2: Slime chunk detection (Bedrock Edition) ---
# To check if a chunk is a slime chunk:
if formulas.is_slime_chunk(chunk_x, chunk_z):
    print(f"Chunk ({chunk_x}, {chunk_z}) is a slime chunk!")
else:
    print(f"Chunk ({chunk_x}, {chunk_z}) is NOT a slime chunk.")

# --- Example 3: Nether/Overworld coordinate conversions ---
over_x, over_z = 128, 256
nether_x, nether_z = formulas.overworld_to_nether(over_x, over_z)
print(f"Overworld ({over_x}, {over_z}) -> Nether ({nether_x}, {nether_z})")

back_to_over_x, back_to_over_z = formulas.nether_to_overworld(nether_x, nether_z)
print(f"Nether ({nether_x}, {nether_z}) -> Overworld ({back_to_over_x}, {back_to_over_z})")

# --- Example 4: Direction and distance between two points ---
x1, z1 = 100, 200
x2, z2 = 120, 180
direction, distance = formulas.calculate_direction(x1, z1, x2, z2)
print(f"Direction from ({x1}, {z1}) to ({x2}, {z2}): {direction}, Distance: {distance}")

manhattan = formulas.manhattan_distance((x1, z1), (x2, z2))
print(f"Manhattan (block) distance: {manhattan}")

# --- Example 5: Using these formulas in a Discord slash command (pseudo-code) ---
"""
# This is a pseudo-code example for integrating the formulas into a Discord bot using discord.py
# (This is not a working bot, just a template for how you might use the formulas)

from formulas import get_chunk_coords, is_slime_chunk

@bot.slash_command(name="slime")
async def slime(ctx, x: int, z: int):
    chunk_x, chunk_z = get_chunk_coords(x, z)
    if is_slime_chunk(chunk_x, chunk_z):
        await ctx.respond(f"Chunk ({chunk_x}, {chunk_z}) is a slime chunk!")
    else:
        await ctx.respond(f"Chunk ({chunk_x}, {chunk_z}) is NOT a slime chunk.")
"""

# --- Example 6: Using these formulas in a regular Python script ---
# You can import and use any function from formulas.py in your own scripts, automation, or data analysis tools.
# Just import formulas and call the functions as shown above. 
