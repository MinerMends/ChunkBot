# ChunkBot [Main Components]

ChunkBot is a Discord bot that helps Minecraft players locate chunks, identify slime chunks, and calculate specific distances within the game. This bot was developed by MinerMends, with contributions from various members of the Minecraft community. This GitHub repository is now open-source, intended to help anyone who needs this information. If you're not a developer, you most likely don't belong here.

Repository contains:
- Chunk coordinate and center calculations
- Slime Chunk Calculation for Bedrock - Mersenne Twister RNG (Converted to Python)
- Nether/Overworld basic conversions
- Direction and distance calculations between points

## What's Included?
- `formulas.py`: Core logic and formulas, with clear comments and docstrings.
- `examples.py`: Practical usage examples, including how to use the formulas in Python scripts and (pseudo-code) Discord slash commands.

## Quickstart

1. **Clone or download this repository.**
2. Use the formulas in your own Python scripts:

```python
import formulas

# Get chunk coordinates for a block position
chunk_x, chunk_z = formulas.get_chunk_coords(123, 456)

# Check if a chunk is a slime chunk (Bedrock Edition)
if formulas.is_slime_chunk(chunk_x, chunk_z):
    print("This is a slime chunk!")
else:
    print("Not a slime chunk.")

# Find the direction and distance between two points
direction, distance = formulas.calculate_direction(100, 200, 120, 180)
print(f"Direction: {direction}, Distance: {distance}")
```

For more examples, see `examples.py`.

## Integrating with Discord Bots

While this code is not Discord-specific, you can easily use these formulas in your own Discord bots. See the pseudo-code in `examples.py` for a template.

## Community & Support
- **Discord:** [Join the Miner Mends Community](https://discord.gg/7B52t6wY2r)
- **YouTube:** [Miner Mends on YouTube](https://youtube.com/minermends)
  
## License
MIT License. Free to use, modify, and share. 
