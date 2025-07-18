/*
Formulas.java
-------------
This file contains core Minecraft-related formulas and logic for:
- Chunk coordinate calculations
- Slime chunk detection (using Mersenne Twister RNG)
- Direction and distance calculations between points

All code is pure Java, with no dependencies. Each function is documented with clear, practical comments for easy understanding and integration.
*/

public class Formulas {
    // --- Mersenne Twister implementation (for slime chunk detection) ---
    // This is a Java port of the MT19937 algorithm, used by Minecraft Bedrock for slime chunk RNG.
    public static class MersenneTwister {
        private final int w = 32, n = 624, m = 397, r = 31;
        private final int a = 0x9908B0DF;
        private final int u = 11, d = 0xFFFFFFFF;
        private final int s = 7, b = 0x9D2C5680;
        private final int t = 15, c = 0xEFC60000;
        private final int l = 18;
        private final int f = 1812433253;
        private int[] MT = new int[n];
        private int index = n + 1;
        private final int lower_mask = 0x7FFFFFFF;
        private final int upper_mask = 0x80000000;

        public MersenneTwister(int seed) {
            seed_mt(seed);
        }

        public void seed_mt(int seed) {
            MT[0] = seed;
            for (int i = 1; i < n; i++) {
                long temp = (long)f * (MT[i-1] ^ (MT[i-1] >>> (w-2))) + i;
                MT[i] = (int)(temp & 0xffffffffL);
            }
            index = n;
        }

        public int extract_number() {
            if (index >= n) {
                twist();
                index = 0;
            }
            int y = MT[index];
            y ^= (y >>> u) & d;
            y ^= (y << s) & b;
            y ^= (y << t) & c;
            y ^= (y >>> l);
            index++;
            return y & 0xffffffff;
        }

        private void twist() {
            for (int i = 0; i < n; i++) {
                int x = (MT[i] & upper_mask) + (MT[(i+1) % n] & lower_mask);
                int xA = x >>> 1;
                if ((x % 2) != 0) xA ^= a;
                MT[i] = MT[(i + m) % n] ^ xA;
            }
        }
    }

    // --- Utility function for 32-bit multiplication (used in slime chunk RNG) ---
    public static int mul32_lo(int a, int b) {
        int a00 = a & 0xffff, a16 = a >>> 16;
        int b00 = b & 0xffff, b16 = b >>> 16;
        int c00 = a00 * b00;
        int c16 = c00 >>> 16;
        c16 += a16 * b00;
        c16 &= 0xffff;
        c16 += a00 * b16;
        int lo = c00 & 0xffff;
        int hi = c16 & 0xffff;
        return ((hi << 16) | lo);
    }

    // --- Slime chunk detection (Bedrock Edition) ---
    public static boolean isSlimeChunk(int chunkX, int chunkZ) {
        int seed = mul32_lo(chunkX, 0x1f1f1f1f) ^ chunkZ;
        MersenneTwister mt = new MersenneTwister(seed);
        int result = mt.extract_number();
        return result % 10 == 0;
    }

    // --- Chunk coordinate and edge calculations ---
    public static int[] getChunkCoords(int x, int z) {
        // Returns the chunk coordinates (chunkX, chunkZ) for a given block position (x, z).
        return new int[] { x / 16, z / 16 };
    }

    public static int[] getChunkCenter(int x, int z) {
        // Returns the center block coordinates (centerX, centerZ) of the chunk containing (x, z).
        int[] chunk = getChunkCoords(x, z);
        return new int[] { chunk[0] * 16 + 7, chunk[1] * 16 + 7 };
    }

    public static int[][] getChunkCorners(int x, int z) {
        // Returns the four corner block coordinates of the chunk containing (x, z).
        int[] chunk = getChunkCoords(x, z);
        int[][] corners = new int[4][2];
        corners[0] = new int[] { chunk[0] * 16, chunk[1] * 16 }; // NW
        corners[1] = new int[] { chunk[0] * 16 + 15, chunk[1] * 16 }; // NE
        corners[2] = new int[] { chunk[0] * 16, chunk[1] * 16 + 15 }; // SW
        corners[3] = new int[] { chunk[0] * 16 + 15, chunk[1] * 16 + 15 }; // SE
        return corners;
    }

    // --- Nether/Overworld coordinate conversions ---
    public static int[] overworldToNether(int x, int z) {
        // Converts Overworld coordinates to Nether coordinates (divide by 8).
        return new int[] { x / 8, z / 8 };
    }

    public static int[] netherToOverworld(int x, int z) {
        // Converts Nether coordinates to Overworld coordinates (multiply by 8).
        return new int[] { x * 8, z * 8 };
    }

    // --- Direction and distance calculations ---
    public static String[] calculateDirection(int x1, int z1, int x2, int z2) {
        // Returns a String[2]: [direction, distance] between two points (x1, z1) and (x2, z2).
        int dx = x2 - x1;
        int dz = z2 - z1;
        String direction;
        if (dx == 0 && dz == 0) {
            direction = "Same location";
        } else if (dx == 0) {
            direction = dz < 0 ? "North" : "South";
        } else if (dz == 0) {
            direction = dx < 0 ? "West" : "East";
        } else {
            direction = dz < 0 ? "North" : "South";
            direction += dx > 0 ? "east" : "west";
        }
        int distance = (int)Math.round(Math.sqrt(dx * dx + dz * dz));
        return new String[] { direction, Integer.toString(distance) };
    }

    // --- Manhattan distance (block distance) ---
    public static int manhattanDistance(int[] coord1, int[] coord2) {
        // Returns the Manhattan (block) distance between two (x, z) coordinates.
        return Math.abs(coord2[0] - coord1[0]) + Math.abs(coord2[1] - coord1[1]);
    }
} 
