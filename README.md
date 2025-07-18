# Minecraft Chunk & Slime Chunk Formulas (Open Source)

This repository contains pure Python implementations of useful Minecraft formulas, including:
- Chunk coordinate and center calculations
- Slime chunk detection (Bedrock Edition, using Mersenne Twister RNG)
- Nether/Overworld coordinate conversions
- Direction and distance calculations between points

All code is self-contained, easy to use, and free of Discord or database dependencies. Perfect for anyone who wants to use Minecraft math in their own scripts, bots, or data analysis tools.

## What's Included
- `formulas.py`: All the core logic and formulas, with clear comments and docstrings.
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

## License
MIT License. Free to use, modify, and share. 
