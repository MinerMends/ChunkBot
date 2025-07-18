<p align="center">
  <img width="200" height="200" alt="image" src="https://github.com/user-attachments/assets/6eb371d6-eea3-4b7c-bdcc-038a043587bb" />
</p>

ChunkBot [Main Components]

ChunkBot is a Discord bot that helps Minecraft players locate chunks, identify slime chunks, and calculate specific distances within the game. This bot was developed by MinerMends, with contributions from various members of the Minecraft community. This GitHub repository is now open-source, intended to help anyone who needs this information. If you're not a developer, you most likely don't belong here.

Repository contains:
- Chunk coordinate and center calculations
- Slime Chunk Calculation for Bedrock - Mersenne Twister RNG (Converted to Python)
- Nether/Overworld basic conversions
- Direction and distance calculations between points

## ChunkBot Examples
### Website
[<img width="739" height="891" alt="ChunkBot Calculator" src="https://github.com/user-attachments/assets/dae00065-9047-4b33-b294-19419dac4e02"/>](https://minermends.com/chunkbots/)
ChunkBot Calculator: [https://minermends.com/chunkbots/](https://minermends.com/chunkbots/)

### Discord Bot
[<img width="505" height="644" alt="Discord Bot" src="https://github.com/user-attachments/assets/7a0ed3d1-754d-4142-a478-2f0ef5161814"/>](https://discord.com/oauth2/authorize?client_id=1094929282196848721&permissions=2147483648&scope=applications.commands%20bot)
Discord Bot: [Invite Link](https://discord.bots.gg/bots/1094929282196848721)

## What's Included?
- `formulas.py`: Core logic and formulas, with clear comments and docstrings (Python).
- `formulas.js`: JavaScript version of the core formulas, ready for Node.js or browser use.
- `Formulas.java`: Java version of the core formulas, ready for any Java project.
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
- **Discord:** [Community](https://discord.gg/7B52t6wY2r)
- **YouTube:** [Miner Mends](https://youtube.com/minermends)
  
## License
MIT License. Free to use, modify, and share. 
