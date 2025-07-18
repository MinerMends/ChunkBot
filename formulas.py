"""
formulas.py
------------
This file contains core Minecraft-related formulas and logic for:
- Chunk coordinate calculations
- Slime chunk detection (using Mersenne Twister RNG)
- Direction and distance calculations between points

All code is pure Python, with no dependencies on Discord or external databases.
Each function is documented with clear, practical comments for easy understanding and integration.
"""

import math

# --- Mersenne Twister implementation (for slime chunk detection) ---
# This is a Python port of the MT19937 algorithm, used by Minecraft Bedrock for slime chunk RNG.
# You can use this class directly, or just use the is_slime_chunk() function below.

class MersenneTwister:
    def __init__(self, seed):
        self.w, self.n, self.m, self.r = 32, 624, 397, 31
        self.a = 0x9908B0DF
        self.u, self.d = 11, 0xFFFFFFFF
        self.s, self.b = 7, 0x9D2C5680
        self.t, self.c = 15, 0xEFC60000
        self.l = 18
        self.f = 1812433253
        self.MT = [0] * self.n
        self.index = self.n + 1
        self.lower_mask = 0x7FFFFFFF
        self.upper_mask = 0x80000000
        self.seed_mt(seed)

    def seed_mt(self, seed):
        self.MT[0] = seed
        for i in range(1, self.n):
            temp = self.f * (self.MT[i-1] ^ (self.MT[i-1] >> (self.w-2))) + i
            self.MT[i] = temp & 0xffffffff
        self.index = self.n

    def extract_number(self):
        if self.index >= self.n:
            self.twist()
            self.index = 0
        y = self.MT[self.index]
        y ^= (y >> self.u) & self.d
        y ^= (y << self.s) & self.b
        y ^= (y << self.t) & self.c
        y ^= (y >> self.l)
        self.index += 1
        return y & 0xffffffff

    def twist(self):
        for i in range(self.n):
            x = (self.MT[i] & self.upper_mask) + (self.MT[(i+1) % self.n] & self.lower_mask)
            xA = x >> 1
            if x % 2 != 0:
                xA ^= self.a
            self.MT[i] = self.MT[(i + self.m) % self.n] ^ xA

# --- Utility function for 32-bit multiplication (used in slime chunk RNG) ---
def mul32_lo(a, b):
    """Performs 32-bit multiplication and returns the lower 32 bits of the result."""
    a00 = a & 0xffff
    a16 = a >> 16
    b00 = b & 0xffff
    b16 = b >> 16
    c00 = a00 * b00
    c16 = c00 >> 16
    c16 += a16 * b00
    c16 &= 0xffff
    c16 += a00 * b16
    lo = c00 & 0xffff
    hi = c16 & 0xffff
    return ((hi << 16) | lo) & 0xffffffff

# --- Slime chunk detection (Bedrock Edition) ---
def is_slime_chunk(chunk_x, chunk_z):
    """
    Returns True if the given chunk coordinates are a slime chunk in Minecraft Bedrock Edition.
    This replicates the in-game algorithm.
    """
    # The seed formula is based on chunk coordinates and a constant
    seed = mul32_lo(chunk_x, 0x1f1f1f1f) ^ chunk_z
    mt = MersenneTwister(seed)
    result = mt.extract_number()
    return result % 10 == 0

# --- Chunk coordinate and edge calculations ---
def get_chunk_coords(x, z):
    """
    Returns the chunk coordinates (chunk_x, chunk_z) for a given block position (x, z).
    Each chunk is 16x16 blocks.
    """
    return x // 16, z // 16

def get_chunk_center(x, z):
    """
    Returns the center block coordinates (center_x, center_z) of the chunk containing (x, z).
    The center is defined as the block at (chunk_x * 16 + 7, chunk_z * 16 + 7).
    """
    chunk_x, chunk_z = get_chunk_coords(x, z)
    return chunk_x * 16 + 7, chunk_z * 16 + 7


def get_chunk_corners(x, z):
    """
    Returns the four corner block coordinates of the chunk containing (x, z).
    Corners are returned as a list: [(NW_x, NW_z), (NE_x, NE_z), (SW_x, SW_z), (SE_x, SE_z)]
    """
    chunk_x, chunk_z = get_chunk_coords(x, z)
    nw = (chunk_x * 16, chunk_z * 16)
    ne = (chunk_x * 16 + 15, chunk_z * 16)
    sw = (chunk_x * 16, chunk_z * 16 + 15)
    se = (chunk_x * 16 + 15, chunk_z * 16 + 15)
    return [nw, ne, sw, se]

# --- Nether/Overworld coordinate conversions ---
def overworld_to_nether(x, z):
    """
    Converts Overworld coordinates to Nether coordinates (divide by 8).
    """
    return x // 8, z // 8

def nether_to_overworld(x, z):
    """
    Converts Nether coordinates to Overworld coordinates (multiply by 8).
    """
    return x * 8, z * 8

# --- Direction and distance calculations ---
def calculate_direction(x1, z1, x2, z2):
    """
    Returns a tuple (direction, distance) between two points (x1, z1) and (x2, z2).
    Direction is a string (e.g., 'North', 'Southwest', etc.).
    Distance is the Euclidean distance, rounded to the nearest integer.
    """
    dx = x2 - x1
    dz = z2 - z1
    if dx == 0 and dz == 0:
        direction = "Same location"
    elif dx == 0:
        direction = "North" if dz < 0 else "South"
    elif dz == 0:
        direction = "West" if dx < 0 else "East"
    else:
        if dz < 0:
            direction = "North"
        else:
            direction = "South"
        if dx > 0:
            direction += "east"
        else:
            direction += "west"
    distance = round(math.sqrt(dx ** 2 + dz ** 2))
    return direction, distance

# --- Manhattan distance (block distance) ---
def manhattan_distance(coord1, coord2):
    """
    Returns the Manhattan (block) distance between two (x, z) coordinates.
    """
    x1, z1 = coord1
    x2, z2 = coord2
    return abs(x2 - x1) + abs(z2 - z1) 
