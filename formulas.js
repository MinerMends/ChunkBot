/*
formulas.js
-----------
This file contains core Minecraft-related formulas and logic for:
- Chunk coordinate calculations
- Slime chunk detection (using Mersenne Twister RNG)
- Direction and distance calculations between points

All code is pure JavaScript, with no dependencies. Each function is documented with clear, practical comments for easy understanding and integration.
*/

// --- Mersenne Twister implementation (for slime chunk detection) ---
// This is a JavaScript port of the MT19937 algorithm, used by Minecraft Bedrock for slime chunk RNG.
class MersenneTwister {
    constructor(seed) {
        this.w = 32; this.n = 624; this.m = 397; this.r = 31;
        this.a = 0x9908B0DF;
        this.u = 11; this.d = 0xFFFFFFFF;
        this.s = 7; this.b = 0x9D2C5680;
        this.t = 15; this.c = 0xEFC60000;
        this.l = 18;
        this.f = 1812433253;
        this.MT = new Array(this.n);
        this.index = this.n + 1;
        this.lower_mask = 0x7FFFFFFF;
        this.upper_mask = 0x80000000;
        this.seed_mt(seed);
    }
    seed_mt(seed) {
        this.MT[0] = seed >>> 0;
        for (let i = 1; i < this.n; i++) {
            let temp = this.f * (this.MT[i-1] ^ (this.MT[i-1] >>> (this.w-2))) + i;
            this.MT[i] = temp >>> 0;
        }
        this.index = this.n;
    }
    extract_number() {
        if (this.index >= this.n) {
            this.twist();
            this.index = 0;
        }
        let y = this.MT[this.index];
        y ^= (y >>> this.u) & this.d;
        y ^= (y << this.s) & this.b;
        y ^= (y << this.t) & this.c;
        y ^= (y >>> this.l);
        this.index++;
        return y >>> 0;
    }
    twist() {
        for (let i = 0; i < this.n; i++) {
            let x = (this.MT[i] & this.upper_mask) + (this.MT[(i+1) % this.n] & this.lower_mask);
            let xA = x >>> 1;
            if (x % 2 !== 0) xA ^= this.a;
            this.MT[i] = this.MT[(i + this.m) % this.n] ^ xA;
        }
    }
}

// --- Utility function for 32-bit multiplication (used in slime chunk RNG) ---
function mul32_lo(a, b) {
    // Performs 32-bit multiplication and returns the lower 32 bits of the result.
    let a00 = a & 0xffff, a16 = a >>> 16;
    let b00 = b & 0xffff, b16 = b >>> 16;
    let c00 = a00 * b00;
    let c16 = c00 >>> 16;
    c16 += a16 * b00;
    c16 &= 0xffff;
    c16 += a00 * b16;
    let lo = c00 & 0xffff;
    let hi = c16 & 0xffff;
    return ((hi << 16) | lo) >>> 0;
}

// --- Slime chunk detection (Bedrock Edition) ---
function isSlimeChunk(chunkX, chunkZ) {
    // Returns true if the given chunk coordinates are a slime chunk in Minecraft Bedrock Edition.
    let seed = mul32_lo(chunkX, 0x1f1f1f1f) ^ chunkZ;
    let mt = new MersenneTwister(seed);
    let result = mt.extract_number();
    return result % 10 === 0;
}

// --- Chunk coordinate and edge calculations ---
function getChunkCoords(x, z) {
    // Returns the chunk coordinates (chunkX, chunkZ) for a given block position (x, z).
    return [Math.floor(x / 16), Math.floor(z / 16)];
}

function getChunkCenter(x, z) {
    // Returns the center block coordinates (centerX, centerZ) of the chunk containing (x, z).
    let [chunkX, chunkZ] = getChunkCoords(x, z);
    return [chunkX * 16 + 7, chunkZ * 16 + 7];
}

function getChunkCorners(x, z) {
    // Returns the four corner block coordinates of the chunk containing (x, z).
    let [chunkX, chunkZ] = getChunkCoords(x, z);
    let nw = [chunkX * 16, chunkZ * 16];
    let ne = [chunkX * 16 + 15, chunkZ * 16];
    let sw = [chunkX * 16, chunkZ * 16 + 15];
    let se = [chunkX * 16 + 15, chunkZ * 16 + 15];
    return [nw, ne, sw, se];
}

// --- Nether/Overworld coordinate conversions ---
function overworldToNether(x, z) {
    // Converts Overworld coordinates to Nether coordinates (divide by 8).
    return [Math.floor(x / 8), Math.floor(z / 8)];
}

function netherToOverworld(x, z) {
    // Converts Nether coordinates to Overworld coordinates (multiply by 8).
    return [x * 8, z * 8];
}

// --- Direction and distance calculations ---
function calculateDirection(x1, z1, x2, z2) {
    // Returns a tuple [direction, distance] between two points (x1, z1) and (x2, z2).
    let dx = x2 - x1;
    let dz = z2 - z1;
    let direction = "";
    if (dx === 0 && dz === 0) {
        direction = "Same location";
    } else if (dx === 0) {
        direction = dz < 0 ? "North" : "South";
    } else if (dz === 0) {
        direction = dx < 0 ? "West" : "East";
    } else {
        direction = dz < 0 ? "North" : "South";
        direction += dx > 0 ? "east" : "west";
    }
    let distance = Math.round(Math.sqrt(dx * dx + dz * dz));
    return [direction, distance];
}

// --- Manhattan distance (block distance) ---
function manhattanDistance(coord1, coord2) {
    // Returns the Manhattan (block) distance between two (x, z) coordinates.
    let [x1, z1] = coord1;
    let [x2, z2] = coord2;
    return Math.abs(x2 - x1) + Math.abs(z2 - z1);
}

// Export functions for Node.js or browser
if (typeof module !== 'undefined' && typeof module.exports !== 'undefined') {
    module.exports = {
        MersenneTwister,
        mul32_lo,
        isSlimeChunk,
        getChunkCoords,
        getChunkCenter,
        getChunkCorners,
        overworldToNether,
        netherToOverworld,
        calculateDirection,
        manhattanDistance
    };
} 
