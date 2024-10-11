import yaml
import json
import numpy as np
from argparse import ArgumentParser

# USAGE GUIDE:
# Download the spoiler log from the seed page and put it in the same directory as the script.
# Name the downloaded log 'spoiler.yaml' (or something else, and specify the name with -f [NAME])
# If you want your output to be named anything other than 'output.json', specify this with -o [NAME]
# Run the script in Terminal/Command Prompt/whatever. The script should output 'Conversion complete.' in the shell on success.
# Your output file will be located in the same directory as the script.

# If you think some name I created sucks, feel free to modify the values of the corresponding dict. 
# It should 'Just Work" as long as you leave the keys the same (as these are used to detect which location is which in the original log).

item_conversion_table = {
    # keys are item names (e.g. Twenty Rupees) in the original spoiler
    # values are the names we want to change the corresponding item to (e.g. TwentyRupees)

    # zelda

    "Piece of Heart": "PieceOfHeart",
    "Heart Container": "BossHeartContainer",
    "Sanctuary Heart Container": "SanctuaryHeartContainer",
    "One Rupee": "OneRupee",
    "Five Rupees": "FiveRupees",
    "Twenty Rupees": "TwentyRupees",
    "Fifty Rupees": "FiftyRupees",
    "One Hundred Rupees": "OneHundredRupees",
    "Three Hundred Rupees": "ThreeHundredRupees",
    "Three Bombs": "ThreeBombs",
    "Ten Bombs": "TenBombs",
    "+5 Bomb Capacity": "FiveBombCapacity",
    "Ten Arrows": "TenArrows",
    "+5 Arrow Capacity": "FiveArrowCapacity",
    "Bow": "Bow",
    "Silver Arrows": "SilverArrows",
    "Blue Boomerang": "Boomerang",
    "Red Boomerang": "RedBoomerang",
    "Hookshot": "Hookshot",
    "Mushroom": "Mushroom",
    "Magic Powder": "Powder",
    "Fire Rod": "FireRod",
    "Ice Rod": "IceRod",
    "Bombos": "Bombos",
    "Ether": "Ether",
    "Quake": "Quake",
    "Lamp": "Lamp", # polarb8Lamp
    "Hammer": "Hammer",
    "Flute": "OcarinaInactive",
    "Shovel": "Shovel",
    "Bug Catching Net": "BugCatchingNet",
    "Book of Mudora": "BookOfMudora",
    "Bottle": "Bottle",
    # will need to add cases for bottles if someday total adds random bottles
    "Cane of Somaria": "CaneOfSomaria",
    "Cane of Byrna": "CaneOfByrna",
    "Magic Cape": "Cape",
    "Magic Mirror": "MagicMirror",
    "Pegasus Boots": "PegasusBoots",
    "Progressive Glove": "ProgressiveGlove",
    "Zora's Flippers": "Flippers",
    "Moon Pearl": "MoonPearl",
    "Progressive Sword": "ProgressiveSword",
    "Progressive Mail": "ProgressiveArmor",
    "Progressive Shield": "ProgressiveShield",
    "Half Magic": "HalfMagic",

    # sm

    "Energy Tank": "EnergyTank",
    "Reserve Tank": "ReserveTank",
    "Missile": "Missile",
    "Super Missile": "SuperMissile",
    "Power Bomb": "PowerBomb",
    "Charge Beam": "ChargeBeam",
    "Ice Beam": "IceBeam",
    "Wave Beam": "WaveBeam",
    "Spazer": "Spazer",
    "Plasma Beam": "PlasmaBeam",
    "Varia Suit": "VariaSuit",
    "Gravity Suit": "GravitySuit",
    "Morph Ball": "MorphBall",
    "Morph Bombs": "MorphBallBombs",
    "Spring Ball": "SpringBall",
    "Screw Attack": "ScrewAttack",
    "Hi-Jump Boots": "HiJumpBoots",
    "Speed Booster": "SpeedBooster",
    "Space Jump": "SpaceJump",
    "Grappling Beam": "GrappleBeam", # NOBODY CALLS IT GRAPPLING BEAM HASHTAGFUCKVANILLA
    "X-Ray Scope": "XRayScope",

    # keys

    "Hyrule Castle Map": "MapH2-HyruleCastle",
    "Sewer Key": "KeyH2-HyruleCastle",
    "Eastern Palace Map": "MapP1-EasternPalace",
    "Eastern Palace Compass": "CompassP1-EasternPalace",
    "Eastern Palace Key": "KeyP1-EasternPalace",
    "Eastern Palace Big Key": "BigKeyP1-EasternPalace",
    "Desert Palace Map": "MapP2-DesertPalace",
    "Desert Palace Compass": "CompassP2-DesertPalace",
    "Desert Palace Key": "KeyP2-DesertPalace",
    "Desert Palace Big Key": "BigKeyP2-DesertPalace",
    "Tower of Hera Map": "MapP3-TowerOfHera",
    "Tower of Hera Compass": "CompassP3-TowerOfHera",
    "Tower of Hera Key": "KeyP3-TowerOfHera",
    "Tower of Hera Big Key": "BigKeyP3-TowerOfHera",
    "Castle Tower Map": "MapA1-CastleTower",
    "Castle Tower Compass": "CompassA1-CastleTower",
    "Castle Tower Key": "KeyA1-CastleTower",
    "Castle Tower Big Key": "BigKeyA1-CastleTower",
    "Palace of Darkness Map": "MapD1-PalaceOfDarkness",
    "Palace of Darkness Compass": "CompassD1-PalaceOfDarkness",
    "Palace of Darkness Key": "KeyD1-PalaceOfDarkness",
    "Palace of Darkness Big Key": "BigKeyD1-PalaceOfDarkness",
    "Swamp Palace Map": "MapD2-SwampPalace",
    "Swamp Palace Compass": "CompassD2-SwampPalace",
    "Swamp Palace Key": "KeyD2-SwampPalace",
    "Swamp Palace Big Key": "BigKeyD2-SwampPalace",
    "Skull Woods Map": "MapD3-SkullWoods",
    "Skull Woods Compass": "CompassD3-SkullWoods",
    "Skull Woods Key": "KeyD3-SkullWoods",
    "Skull Woods Big Key": "BigKeyD3-SkullWoods",
    "Thieves Town Map": "MapP1-ThievesTown",
    "Thieves Town Compass": "CompassP1-ThievesTown",
    "Thieves Town Key": "KeyP1-ThievesTown",
    "Thieves Town Big Key": "BigKeyP1-ThievesTown",
    "Ice Palace Map": "MapD5-IcePalace",
    "Ice Palace Compass": "CompassD5-IcePalace",
    "Ice Palace Key": "KeyD5-IcePalace",
    "Ice Palace Big Key": "BigKeyD5-IcePalace",
    "Misery Mire Map": "MapD6-MiseryMire",
    "Misery Mire Compass": "CompassD6-MiseryMire",
    "Misery Mire Key": "KeyD6-MiseryMire",
    "Misery Mire Big Key": "BigKeyD6-MiseryMire",
    "Turtle Rock Map": "MapD7-TurtleRock",
    "Turtle Rock Compass": "CompassD7-TurtleRock",
    "Turtle Rock Key": "KeyD7-TurtleRock",
    "Turtle Rock Big Key": "BigKeyD7-TurtleRock",
    "Ganons Tower Map": "MapA2-GanonsTower",
    "Ganons Tower Compass": "CompassA2-GanonsTower",
    "Ganons Tower Key": "KeyA2-GanonsTower",
    "Ganons Tower Big Key": "BigKeyA2-GanonsTower",
    
    # prizes (included here because This Is How The Program Works)
    "Blue Crystal": "RegularCrystal",
    "Red Crystal": "FiveSixCrystal",
    "Green Pendant": "PendantOfCourage",
    "Blue/Red Pendant": "RegularPendant",
    "Kraid Boss Token": "MetroidTokenK",
    "Phantoon Boss Token": "MetroidTokenP",
    "Draygon Boss Token": "MetroidTokenD",
    "Ridley Boss Token": "MetroidTokenR",
}

location_conversion_table = {
    # keys are location names (e.g. Eastern Palace - Armos Knights) in the original spoiler
    # values are the names we want to change the corresponding location to (e.g. Eastern Palace - Boss)

    "Eastern Palace - Armos Knights": "Eastern Palace - Boss",
    "Desert Palace - Lanmolas": "Desert Palace - Boss",
    "Tower of Hera - Moldorm": "Tower of Hera - Boss",
    "Castle Tower - Foyer": "Castle Tower - Room 03",
    "Palace of Darkness - Helmasaur King": "Palace of Darkness - Boss",
    "Swamp Palace - Arrghus": "Swamp Palace - Boss",
    "Skull Woods - Mothula": "Skull Woods - Boss",
    "Thieves' Town - Blind": "Thieves' Town - Boss",
    "Ice Palace - Kholdstare": "Ice Palace - Boss",
    "Misery Mire - Vitreous": "Misery Mire - Boss",
    "Turtle Rock - Trinexx": "Turtle Rock - Boss",
    "South of Grove": "Cave 45",

    "Energy Tank, Terminator": "Terminator E-Tank",
    "Energy Tank, Gauntlet": "Gauntlet E-Tank",
    "Missile (Crateria gauntlet right)": "Back of Gauntlet - Right",
    "Missile (Crateria gauntlet left)": "Back of Gauntlet - Left",
    "Power Bomb (Crateria surface)": "Crateria Power Bomb",
    "Missile (Crateria middle)": "230 Missile",
    "Missile (Crateria bottom)": "Old Mother Brain Missile",
    "Super Missile (Crateria)": "Climb Super",
    "Bombs": "Bomb Torizo",
    "Missile (outside Wrecked Ship bottom)": "Ocean Missile",
    "Missile (outside Wrecked Ship top)": "Sky Missile",
    "Missile (outside Wrecked Ship middle)": "Maze Missile",
    "Missile (Crateria moat)": "Moat Missile",
    "Power Bomb (green Brinstar bottom)": "Etecoons Power Bomb",
    "Missile (green Brinstar below super missile)": "Early Super Bridge Missile",
    "Super Missile (green Brinstar top)": "Early Super",
    "Reserve Tank, Brinstar": "Brinstar Reserve",
    "Missile (green Brinstar behind missile)": "Brinstar Reserve Front Missile",
    "Missile (green Brinstar behind reserve tank)": "Brinstar Reserve Back Missile",
    "Energy Tank, Etecoons": "Etecoons E-Tank",
    "Super Missile (green Brinstar bottom)": "Etecoons Super",
    "Super Missile (pink Brinstar)": "Spore Spawn Super",
    "Missile (pink Brinstar top)": "Mission Impossible Missile",
    "Missile (pink Brinstar bottom)": "Charge Missile",
    "Charge Beam": "Charge Beam",
    "Power Bomb (pink Brinstar)": "Mission Impossible Power Bomb",
    "Missile (green Brinstar pipe)": "Pipe Missile",
    "Energy Tank, Waterway": "Waterway E-Tank",
    "Energy Tank, Brinstar Gate": "Wave Gate E-Tank",
    "Morphing Ball": "Morph Ball Pedestal",
    "Power Bomb (blue Brinstar)": "Behind Morph Power Bomb",
    "Missile (blue Brinstar middle)": "Beta Missile",
    "Energy Tank, Brinstar Ceiling": "Blue Brinstar Ceiling E-Tank",
    "Missile (blue Brinstar bottom)": "Alpha Missile",
    "Missile (blue Brinstar top)": "Billy Mays Front Missile",
    "Missile (blue Brinstar behind missile)": "Billy Mays Hidden Missile",
    "X-Ray Scope": "X-Ray Scope",
    "Power Bomb (red Brinstar sidehopper room)": "Beta Power Bomb",
    "Power Bomb (red Brinstar spike room)": "Alpha Power Bomb",
    "Missile (red Brinstar spike room)": "Alpha Power Bomb Missile",
    "Spazer": "Spazer",
    "Energy Tank, Kraid": "Kraid E-Tank",
    "Varia Suit": "Varia Suit",
    "Missile (Kraid)": "Kraid Missile",
    "Missile (Wrecked Ship middle)": "Spooky Missile",
    "Reserve Tank, Wrecked Ship": "Wrecked Ship Reserve",
    "Missile (Gravity Suit)": "Bowling Missile",
    "Missile (Wrecked Ship top)": "Attic Missile",
    "Energy Tank, Wrecked Ship": "Wrecked Ship E-Tank",
    "Super Missile (Wrecked Ship left)": "Wrecked Ship Left Supers",
    "Right Super, Wrecked Ship": "Wrecked Ship Right Supers",
    "Gravity Suit": "Gravity Suit",
    "Missile (green Maridia shinespark)": "Main Street Missile",
    "Super Missile (green Maridia)": "Crab Super",
    "Energy Tank, Mama turtle": "Mama Turtle E-Tank",
    "Missile (green Maridia tatori)": "Mama Turtle Missile",
    "Super Missile (yellow Maridia)": "Watering Hole - Left",
    "Missile (yellow Maridia super missile)": "Watering Hole - Right",
    "Missile (yellow Maridia false wall)": "Beach Missile",
    "Plasma Beam": "Plasma Beam",
    "Missile (left Maridia sand pit room)": "Left Sand Pit Missile",
    "Reserve Tank, Maridia": "Maridia Reserve",
    "Missile (right Maridia sand pit room)": "Right Sand Pit Missile",
    "Power Bomb (right Maridia sand pit room)": "Right Sand Pit Power Bomb",
    "Missile (pink Maridia)": "Aqueduct Missile",
    "Super Missile (pink Maridia)": "Aqueduct Super",
    "Spring Ball": "Spring Ball",
    "Missile (Draygon)": "Precious Missile",
    "Energy Tank, Botwoon": "Botwoon E-Tank",
    "Space Jump": "Space Jump",
    "Missile (lava room)": "Cathedral Missile",
    "Ice Beam": "Ice Beam",
    "Missile (below Ice Beam)": "Crumble Shaft Missile",
    "Hi-Jump Boots": "Hi-Jump Boots",
    "Missile (Hi-Jump Boots)": "Hi-Jump Boots Missile",
    "Energy Tank (Hi-Jump Boots)": "Hi-Jump Boots E-Tank",
    "Reserve Tank, Norfair": "Norfair Reserve",
    "Missile (Norfair Reserve Tank)": "Norfair Reserve Hidden Missile",
    "Missile (bubble Norfair green door)": "Norfair Reserve Front Missile",
    "Missile (bubble Norfair)": "Bubble Mountain Corner Missile",
    "Missile (Speed Booster)": "Speed Missile",
    "Speed Booster": "Speed Booster",
    "Missile (Wave Beam)": "Wave Missile",
    "Wave Beam": "Wave Beam",
    "Energy Tank, Crocomire": "Crocomire E-Tank",
    "Missile (above Crocomire)": "Croc Escape Missile",
    "Power Bomb (Crocomire)": "Croc Power Bomb",
    "Missile (below Crocomire)": "Cosine Missile",
    "Missile (Grappling Beam)": "Indiana Jones Missile",
    "Grappling Beam": "Grapple Beam",
    "Missile (Gold Torizo)": "Gold Torizo Missile",
    "Super Missile (Gold Torizo)": "Gold Torizo Super",
    "Screw Attack": "Screw Attack",
    "Missile (Mickey Mouse room)": "Mickey Mouse Missile",
    "Missile (lower Norfair above fire flea room)": "Hotarubi Missile",
    "Power Bomb (lower Norfair above fire flea room)": "Jail Power Bomb",
    "Power Bomb (Power Bombs of shame)": "Power Bombs of Shame",
    "Missile (lower Norfair near Wave Beam)": "FrankerZ Missile",
    "Energy Tank, Ridley": "Ridley E-Tank",
    "Energy Tank, Firefleas": "Firefleas E-Tank",

    "Norfair Lower": "Lower Norfair"
}

index_table = {
    "Eastern Palace": 0,
    "Desert Palace": 1,
    "Tower of Hera": 2,
    "Dark Palace": 3,
    "Swamp Palace": 4,
    "Skull Woods": 5,
    "Thieves' Town": 6,
    "Ice Palace": 7,
    "Misery Mire": 8,
    "Turtle Rock": 9,
    "Brinstar": 10,
    "Wrecked Ship": 11,
    "Maridia": 12,
    "Lower Norfair": 13,
    "Misery Mire Medallion": 14,
    "Turtle Rock Medallion": 15,
    "Sanctuary": 16,
    "Sewers - Secret Room - Left": 17,
    "Sewers - Secret Room - Middle": 18,
    "Sewers - Secret Room - Right": 19,
    "Sewers - Dark Cross": 20,
    "Hyrule Castle - Map Chest": 21,
    "Hyrule Castle - Boomerang Chest": 22,
    "Hyrule Castle - Zelda's Cell": 23,
    "Link's Uncle": 24,
    "Secret Passage": 25,
    "Eastern Palace - Cannonball Chest": 26,
    "Eastern Palace - Map Chest": 27,
    "Eastern Palace - Compass Chest": 28,
    "Eastern Palace - Big Chest": 29,
    "Eastern Palace - Big Key Chest": 30,
    "Eastern Palace - Boss": 31,
    "Desert Palace - Big Chest": 36,
    "Desert Palace - Torch": 32,
    "Desert Palace - Map Chest": 33,
    "Desert Palace - Big Key Chest": 35,
    "Desert Palace - Compass Chest": 34,
    "Desert Palace - Boss": 37,
    "Tower of Hera - Basement Cage": 38,
    "Tower of Hera - Map Chest": 39,
    "Tower of Hera - Big Key Chest": 40,
    "Tower of Hera - Compass Chest": 41,
    "Tower of Hera - Big Chest": 42,
    "Tower of Hera - Boss": 43,
    "Castle Tower - Room 03": 44,
    "Castle Tower - Dark Maze": 45,
    "Palace of Darkness - Shooter Room": 46,
    "Palace of Darkness - Big Key Chest": 47,
    "Palace of Darkness - Stalfos Basement": 48,
    "Palace of Darkness - The Arena - Bridge": 49,
    "Palace of Darkness - The Arena - Ledge": 50,
    "Palace of Darkness - Map Chest": 51,
    "Palace of Darkness - Compass Chest": 52,
    "Palace of Darkness - Harmless Hellway": 53,
    "Palace of Darkness - Dark Basement - Left": 54,
    "Palace of Darkness - Dark Basement - Right": 55,
    "Palace of Darkness - Dark Maze - Top": 56,
    "Palace of Darkness - Dark Maze - Bottom": 57,
    "Palace of Darkness - Big Chest": 58,
    "Palace of Darkness - Boss": 59,
    "Swamp Palace - Entrance": 60,
    "Swamp Palace - Map Chest": 61,
    "Swamp Palace - Big Chest": 62,
    "Swamp Palace - Compass Chest": 63,
    "Swamp Palace - West Chest": 64,
    "Swamp Palace - Big Key Chest": 65,
    "Swamp Palace - Flooded Room - Left": 66,
    "Swamp Palace - Flooded Room - Right": 67,
    "Swamp Palace - Waterfall Room": 68,
    "Swamp Palace - Boss": 69,
    "Skull Woods - Pot Prison": 72, 
    "Skull Woods - Compass Chest": 73,
    "Skull Woods - Big Chest": 70,
    "Skull Woods - Map Chest": 75,
    "Skull Woods - Pinball Room": 74,
    "Skull Woods - Big Key Chest": 71,
    "Skull Woods - Bridge Room": 76,
    "Skull Woods - Boss": 77,
    "Thieves' Town - Map Chest": 78,
    "Thieves' Town - Ambush Chest": 79,
    "Thieves' Town - Compass Chest": 80,
    "Thieves' Town - Big Key Chest": 81,
    "Thieves' Town - Attic": 82,
    "Thieves' Town - Blind's Cell": 83,
    "Thieves' Town - Big Chest": 84,
    "Thieves' Town - Boss": 85,
    "Ice Palace - Compass Chest": 86,
    "Ice Palace - Spike Room": 88,
    "Ice Palace - Map Chest": 88,
    "Ice Palace - Big Key Chest": 87,
    "Ice Palace - Iced T Room": 92,
    "Ice Palace - Freezor Chest": 90,
    "Ice Palace - Big Chest": 91,
    "Ice Palace - Boss": 93,
    "Misery Mire - Main Lobby": 98,
    "Misery Mire - Map Chest": 99,
    "Misery Mire - Bridge Chest": 94,
    "Misery Mire - Spike Chest": 95,
    "Misery Mire - Compass Chest": 96,
    "Misery Mire - Big Key Chest": 97,
    "Misery Mire - Big Chest": 100,
    "Misery Mire - Boss": 101,
    "Turtle Rock - Compass Chest": 102,
    "Turtle Rock - Roller Room - Left": 103,
    "Turtle Rock - Roller Room - Right": 104,
    "Turtle Rock - Chain Chomps": 105,
    "Turtle Rock - Big Key Chest": 106,
    "Turtle Rock - Big Chest": 107,
    "Turtle Rock - Crystaroller Room": 108,
    "Turtle Rock - Eye Bridge - Top Right": 109,
    "Turtle Rock - Eye Bridge - Top Left": 110,
    "Turtle Rock - Eye Bridge - Bottom Right": 111,
    "Turtle Rock - Eye Bridge - Bottom Left": 112,
    "Turtle Rock - Boss": 113,
    "Ganon's Tower - Bob's Torch": 114,
    "Ganon's Tower - DMs Room - Top Left": 115,
    "Ganon's Tower - DMs Room - Top Right": 116,
    "Ganon's Tower - DMs Room - Bottom Left": 117,
    "Ganon's Tower - DMs Room - Bottom Right": 118,
    "Ganon's Tower - Map Chest": 119,
    "Ganon's Tower - Firesnake Room": 120,
    "Ganon's Tower - Randomizer Room - Top Left": 121,
    "Ganon's Tower - Randomizer Room - Top Right": 122,
    "Ganon's Tower - Randomizer Room - Bottom Left": 123,
    "Ganon's Tower - Randomizer Room - Bottom Right": 124,
    "Ganon's Tower - Hope Room - Left": 125,
    "Ganon's Tower - Hope Room - Right": 126,
    "Ganon's Tower - Tile Room": 127,
    "Ganon's Tower - Compass Room - Top Left": 128,
    "Ganon's Tower - Compass Room - Top Right": 129,
    "Ganon's Tower - Compass Room - Bottom Left": 130,
    "Ganon's Tower - Compass Room - Bottom Right": 131,
    "Ganon's Tower - Bob's Chest": 132,
    "Ganon's Tower - Big Chest": 133,
    "Ganon's Tower - Big Key Chest": 134,
    "Ganon's Tower - Big Key Room - Left": 135,
    "Ganon's Tower - Big Key Room - Right": 136,
    "Ganon's Tower - Mini Helmasaur Room - Left": 137,
    "Ganon's Tower - Mini Helmasaur Room - Right": 138,
    "Ganon's Tower - Pre-Moldorm Chest": 139,
    "Ganon's Tower - Moldorm Chest": 140, 
    "Sahasrahla's Hut - Left": 141,
    "Sahasrahla's Hut - Middle": 142,
    "Sahasrahla's Hut - Right": 143,
    "Sahasrahla": 144,
    "Potion Shop": 145,
    "King Zora": 146,
    "Zora's Ledge": 147,
    "Waterfall Fairy - Left": 148,
    "Waterfall Fairy - Right": 149,
    "Master Sword Pedestal": 150,
    "Lumberjack Tree": 151,
    "Pegasus Rocks": 152,
    "Graveyard Ledge": 153,
    "King's Tomb": 154,
    "Mushroom": 155,
    "Lost Woods Hideout": 156,
    "Blind's Hideout - Top": 157,
    "Blind's Hideout - Far Left": 158,
    "Blind's Hideout - Left": 159,
    "Blind's Hideout - Right": 160,
    "Blind's Hideout - Far Right": 161,
    "Kakariko Well - Top": 162,
    "Kakariko Well - Left": 163,
    "Kakariko Well - Middle": 164,
    "Kakariko Well - Right": 165,
    "Kakariko Well - Bottom": 166,
    "Bottle Merchant": 167,
    "Chicken House": 168,
    "Sick Kid": 169,
    "Kakariko Tavern": 170,
    "Magic Bat": 171,
    "Library": 172,
    "Maze Race": 173,
    "Flute Spot": 174,
    "Cave 45": 175,
    "Bombos Tablet": 176,
    "Aginah's Cave": 177,
    "Desert Ledge": 178,
    "Checkerboard Cave": 179,
    "Link's House": 180,
    "Floodgate Chest": 181,
    "Sunken Treasure": 182,
    "Mini Moldorm Cave - Far Left": 183,
    "Mini Moldorm Cave - Left": 184,
    "Mini Moldorm Cave - NPC": 185,
    "Mini Moldorm Cave - Right": 186,
    "Mini Moldorm Cave - Far Right": 187,
    "Lake Hylia Island": 188,
    "Hobo": 189,
    "Ice Rod Cave": 190, # dm is 191 to 204
    "Old Man": 191,
    "Spectacle Rock": 192,
    "Spectacle Rock Cave": 193,
    "Ether Tablet": 194, 
    "Spiral Cave": 195,
    "Paradox Cave Upper - Left": 196,
    "Paradox Cave Upper - Right": 197,
    "Paradox Cave Lower - Far Left": 198,
    "Paradox Cave Lower - Left": 199,
    "Paradox Cave Lower - Middle": 200,
    "Paradox Cave Lower - Right": 201,
    "Paradox Cave Lower - Far Right": 202,
    "Floating Island": 203,
    "Mimic Cave": 204,
    "Superbunny Cave - Top": 205,
    "Superbunny Cave - Bottom": 206,
    "Hookshot Cave - Top Right": 207,
    "Hookshot Cave - Top Left": 208,
    "Hookshot Cave - Bottom Left": 209,
    "Hookshot Cave - Bottom Right": 210,
    "Spike Cave": 211,
    "Catfish": 212,
    "Pyramid": 213,
    "Pyramid Fairy - Left": 214,
    "Pyramid Fairy - Right": 215,
    "Bumper Cave": 216,
    "Chest Game": 217,
    "C-Shaped House": 218,
    "Brewery": 219,
    "Hammer Pegs": 220,
    "Blacksmith": 221,
    "Purple Chest": 222,
    "Hype Cave - Top": 223,
    "Hype Cave - Middle Right": 224,
    "Hype Cave - Middle Left": 225,
    "Hype Cave - Bottom": 226,
    "Hype Cave - NPC": 227,
    "Digging Game": 228,
    "Stumpy": 229,
    "Mire Shed - Left": 230,
    "Mire Shed - Right": 231,
    "Gauntlet E-Tank": 232,
    "Back of Gauntlet - Right": 233,
    "Back of Gauntlet - Left": 234,
    "Terminator E-Tank": 235,
    "Crateria Power Bomb": 236,
    "Bomb Torizo": 237,
    "230 Missile": 238,
    "Climb Super": 239,
    "Old Mother Brain Missile": 240,
    "Moat Missile": 241,
    "Sky Missile": 242,
    "Maze Missile": 243,
    "Ocean Missile": 244,
    "Early Super Bridge Missile": 245,
    "Brinstar Reserve": 246,
    "Brinstar Reserve Front Missile": 247,
    "Brinstar Reserve Back Missile": 248,
    "Early Super": 249,
    "Etecoons E-Tank": 250,
    "Etecoons Super": 251,
    "Etecoons Power Bomb": 252,
    "Mission Impossible Missile": 253,
    "Mission Impossible Power Bomb": 254,
    "Wave Gate E-Tank": 255,
    "Spore Spawn Super": 256,
    "Charge Missile": 257,
    "Charge Beam": 258,
    "Waterway E-Tank": 259,
    "Pipe Missile": 260,
    "Behind Morph Power Bomb": 261,
    "Morph Ball Pedestal": 262,
    "Alpha Missile": 263,
    "Blue Brinstar Ceiling E-Tank": 264,
    "Beta Missile": 265,
    "Billy Mays Front Missile": 266,
    "Billy Mays Hidden Missile": 267,
    "Alpha Power Bomb": 268,
    "Alpha Power Bomb Missile": 269,
    "Beta Power Bomb": 270,
    "X-Ray Scope": 271,
    "Spazer": 272,
    "Kraid Missile": 273,
    "Varia Suit": 274,
    "Kraid E-Tank": 275,
    "Spooky Missile": 276,
    "Wrecked Ship Left Supers": 277,
    "Wrecked Ship Right Supers": 278,
    "Wrecked Ship E-Tank": 279,
    "Attic Missile": 280,
    "Bowling Missile": 281,
    "Wrecked Ship Reserve": 282,
    "Gravity Suit": 283,
    "Main Street Missile": 284,
    "Crab Super": 285,
    "Mama Turtle E-Tank": 286,
    "Mama Turtle Missile": 287,
    "Beach Missile": 288,
    "Watering Hole - Left": 289,
    "Watering Hole - Right": 290,
    "Left Sand Pit Missile": 291,
    "Maridia Reserve": 292,
    "Right Sand Pit Missile": 293,
    "Right Sand Pit Power Bomb": 294,
    "Aqueduct Missile": 295,
    "Aqueduct Super": 296,
    "Botwoon E-Tank": 297,
    "Precious Missile": 298,
    "Space Jump": 299,
    "Plasma Beam": 300,
    "Spring Ball": 301,
    "Hi-Jump Boots E-Tank": 302,
    "Hi-Jump Boots": 303,
    "Hi-Jump Boots Missile": 304,
    "Ice Beam": 305,
    "Crumble Shaft Missile": 306,
    "Cathedral Missile": 307,
    "Bubble Mountain Corner Missile": 308,
    "Norfair Reserve Front Missile": 309,
    "Norfair Reserve Hidden Missile": 310,
    "Norfair Reserve": 311,
    "Speed Missile": 312,
    "Speed Booster": 313,
    "Wave Missile": 314,
    "Wave Beam": 315,
    "Crocomire E-Tank": 316,
    "Croc Power Bomb": 317,
    "Cosine Missile": 318,
    "Indiana Jones Missile": 319,
    "Grapple Beam": 320,
    "Croc Escape Missile": 321,
    "Gold Torizo Missile": 322,
    "Gold Torizo Super": 323,
    "Screw Attack": 324,
    "Mickey Mouse Missile": 325,
    "Firefleas E-Tank": 326,
    "Hotarubi Missile": 327,
    "Jail Power Bomb": 328,
    "FrankerZ Missile": 329,
    "Power Bombs of Shame": 330,
    "Ridley E-Tank": 331
}

tree_pull_conversion_table = {
    "Bomb1": "BombRefill1",
    "Bomb4": "BombRefill4",
    "Bomb8": "BombRefill8",
    "Arrow5": "ArrowRefill5",
    "Arrow10": "ArrowRefill10",
    "Heart": "Heart",
    "Fairy": "Fairy",
    "Magic": "MagicRefillSmall",
    "FullMagic": "MagicRefillFull",
    "Green": "RupeeGreen",
    "Blue": "RupeeBlue",
    "Red": "RupeeRed"
}

def merge_dicts(*dicts):
    ret = {}
    for list in dicts:
        for key in list:
            value = list[key]
            ret.update({key: value})
    
    return ret

def rename_items(region): # RENAMES ITEMS AND LOCATIONS and sorts them now???
    temp = {}
    unsorted_list = {}

    for key in region:
        if not region[key] in item_conversion_table:
            temp.update({key: region[key]})
        else:
            for smz3_name in item_conversion_table:
                if region[key] == smz3_name:
                    temp.update({key: item_conversion_table[smz3_name]})
                    break

    for key in temp:
        if not key in location_conversion_table:
            unsorted_list.update({key: temp[key]})
        else:
            for smz3_name in location_conversion_table:
                if key == smz3_name:
                    unsorted_list.update({location_conversion_table[key]: temp[key]})
                    break

    # sort index_table before we use it
    keys = list(index_table.keys())
    values = list(index_table.values())
    sorted_value_index = np.argsort(values)
    sorted_index_table = {keys[i]: values[i] for i in sorted_value_index}


    final_list = sorted_index_table.copy()

    # remove items so that sorted_index_table only has the locations of dict
    for key in sorted_index_table: 
        if not key in unsorted_list.keys(): 
            final_list.pop(key)
        else:
            final_list.update({key:unsorted_list[key]})

    return final_list

def slice_prizes(dict):
    ret = {
        "Prizes": {},
        "Special": {}
    }

    for key in dict:
        # print(key[0:8])
        if key[0:8] == "Prize - ":
            ret["Prizes"].update({key[8:]: dict[key]})
        elif key[-1] == "e": # "Misery Mire" ends with "e", but "Turtle Rock" does not
            ret["Special"].update({"Misery Mire Medallion": dict[key]})
        elif key[-1] == "k":
            ret["Special"].update({"Turtle Rock Medallion": dict[key]})

    return ret

def print_sm_location_names(dict):
    ret = {}
    for key in dict:
        ret.update({key: ""})
    
    return ret

def sort_locations(dict):

    # sort index_table before we use it
    keys = list(index_table.keys())
    values = list(index_table.values())
    sorted_value_index = np.argsort(values)
    sorted_index_table = {keys[i]: values[i] for i in sorted_value_index}

    # remove items so that sorted_index_table only has the locations of dict
    for key in sorted_index_table: 
        if not key in dict.keys(): 
            sorted_index_table.pop(key)
        else:
            sorted_index_table.update({key, dict[key]})

    return sorted_index_table
        
def handle_meta(dict, header):
    ret = {
        "Drops": {
            "PullTree": {},
            "RupeeCrab": {},
        },
        "meta": {

        }
    }
    drops = {}

    ret["Drops"]["PullTree"].update({"Tier1": tree_pull_conversion_table[dict["dropPrizes"]["treePulls"][0]]})
    ret["Drops"]["PullTree"].update({"Tier2": tree_pull_conversion_table[dict["dropPrizes"]["treePulls"][1]]})
    ret["Drops"]["PullTree"].update({"Tier3": tree_pull_conversion_table[dict["dropPrizes"]["treePulls"][2]]})
    ret["Drops"]["RupeeCrab"].update({"Main": tree_pull_conversion_table[dict["dropPrizes"]["crabContinous"]]})
    ret["Drops"]["RupeeCrab"].update({"Final": tree_pull_conversion_table[dict["dropPrizes"]["crabFinal"]]})
    ret["Drops"].update({"Stun": tree_pull_conversion_table[dict["dropPrizes"]["stun"]]})

    ret["meta"].update({"hash": header})
    for key in dict:
        if key != "dropPrizes":
            ret["meta"].update({key: dict[key]})


    return ret

def compile_nonrace_spoiler(spoiler_object):
    # all regions get their own dict

    prizes_and_medallions = slice_prizes((spoiler_object[1]["Prizes and Requirements"]))
    prizes_and_medallions["Prizes"] = rename_items(prizes_and_medallions["Prizes"])
    
    # ALTTP 

    hyrule_castle = rename_items((spoiler_object[7]["Hyrule Castle"]))
    eastern_palace = rename_items((spoiler_object[15]["Eastern Palace"]))
    desert_palace = rename_items((spoiler_object[16]["Desert Palace"]))
    tower_of_hera = rename_items((spoiler_object[17]["Tower of Hera"]))
    castle_tower = rename_items((spoiler_object[14]["Castle Tower"]))
    dark_palace = rename_items((spoiler_object[18]["Palace of Darkness"]))
    swamp_palace = rename_items((spoiler_object[19]["Swamp Palace"]))
    skull_woods = rename_items((spoiler_object[20]["Skull Woods"]))
    thieves_town = rename_items((spoiler_object[21]["Thieves' Town"]))
    ice_palace = rename_items((spoiler_object[22]["Ice Palace"]))
    misery_mire = rename_items((spoiler_object[23]["Misery Mire"]))
    turtle_rock = rename_items((spoiler_object[24]["Turtle Rock"]))
    ganons_tower = rename_items((spoiler_object[25]["Ganon's Tower"]))

    light_world_nw = rename_items((spoiler_object[4]["Light World North West"]))
    light_world_ne = rename_items((spoiler_object[5]["Light World North East"]))
    light_world_s  = rename_items((spoiler_object[6]["Light World South"]))

    light_world = merge_dicts(light_world_ne, light_world_nw, light_world_s)

    death_mountain_w = rename_items((spoiler_object[2]["Light World Death Mountain West"]))
    death_mountain_e = rename_items((spoiler_object[3]["Light World Death Mountain East"]))

    death_mountain = merge_dicts(death_mountain_w, death_mountain_e)

    spike_cave = rename_items((spoiler_object[8]["Dark World Death Mountain West"]))
    dw_dm_e = rename_items((spoiler_object[9]["Dark World Death Mountain East"]))
    dw_nw = rename_items((spoiler_object[10]["Dark World North West"]))
    dw_ne = rename_items((spoiler_object[11]["Dark World North East"]))
    dw_s = rename_items((spoiler_object[12]["Dark World South"]))
    dw_mire = rename_items((spoiler_object[13]["Dark World Mire"]))

    dark_world = merge_dicts(dw_dm_e, spike_cave, dw_ne, dw_nw, dw_s, dw_mire)

    # SM

    crat_west = rename_items((spoiler_object[26]["Crateria West"]))
    crat_central = rename_items((spoiler_object[27]["Crateria Central"]))
    crat_east = rename_items((spoiler_object[28]["Crateria East"]))

    crateria = merge_dicts(crat_west, crat_central, crat_east)

    brin_blue = rename_items((spoiler_object[29]["Brinstar Blue"]))
    brin_green = rename_items((spoiler_object[30]["Brinstar Green"]))
    brin_pink = rename_items((spoiler_object[31]["Brinstar Pink"]))
    brin_red = rename_items((spoiler_object[32]["Brinstar Red"]))
    brin_kraid = rename_items((spoiler_object[33]["Brinstar Kraid"]))

    brinstar = merge_dicts(brin_green, brin_pink, brin_blue, brin_red, brin_kraid)

    wrecked_ship = rename_items((spoiler_object[34]["Wrecked Ship"]))

    maridia_outer = rename_items((spoiler_object[35]["Maridia Outer"]))
    maridia_inner = rename_items((spoiler_object[36]["Maridia Inner"]))
    
    maridia = merge_dicts(maridia_outer, maridia_inner)

    un_west = rename_items((spoiler_object[37]["Norfair Upper West"]))
    un_east = rename_items((spoiler_object[38]["Norfair Upper East"]))
    croc = rename_items((spoiler_object[39]["Norfair Upper Crocomire"]))

    upper_norfair = merge_dicts(un_west, un_east, croc)

    ln_west = rename_items((spoiler_object[40]["Norfair Lower West"]))
    ln_east = rename_items((spoiler_object[41]["Norfair Lower East"]))

    lower_norfair = merge_dicts(ln_west, ln_east)

    metadata = handle_meta((spoiler_object[42]["Meta"]),spoiler_object[0])
    
    zelda_spoiler = {            
        "Hyrule Castle": hyrule_castle,
        "Eastern Palace": eastern_palace,
        "Desert Palace": desert_palace,
        "Tower of Hera": tower_of_hera,
        "Castle Tower": castle_tower,
        "Palace of Darkness": dark_palace,
        "Swamp Palace": swamp_palace,
        "Skull Woods": skull_woods,
        "Thieves Town": thieves_town,
        "Ice Palace": ice_palace,
        "Misery Mire": misery_mire,
        "Turtle Rock": turtle_rock,
        "Ganons Tower": ganons_tower,
        "Light World": light_world,
        "Death Mountain": death_mountain,
        "Dark World": dark_world
    }
    metroid_spoiler = {
        "Crateria": crateria,
        "Brinstar": brinstar,
        "Wrecked Ship": wrecked_ship,
        "Maridia": maridia,
        "Upper Norfair": upper_norfair,
        "Lower Norfair": lower_norfair
    }
    combined_spoiler = {
        "Prizes": prizes_and_medallions["Prizes"],
        "Special": prizes_and_medallions["Special"],
        "A Link to the Past": zelda_spoiler,
        "Super Metroid": metroid_spoiler,
        "Drops": metadata["Drops"],
        "meta": metadata["meta"]
    }

    return combined_spoiler

def compile_race_spoiler(spoiler_object):
    # all regions get their own dict

    prizes_and_medallions = slice_prizes((spoiler_object["PrizesAndRequirements"]))
    prizes_and_medallions["Prizes"] = rename_items(prizes_and_medallions["Prizes"])
    
    # ALTTP 

    hyrule_castle = rename_items((spoiler_object["Regions"]["Hyrule Castle"]))
    eastern_palace = rename_items((spoiler_object["Regions"]["Eastern Palace"]))
    desert_palace = rename_items((spoiler_object["Regions"]["Desert Palace"]))
    tower_of_hera = rename_items((spoiler_object["Regions"]["Tower of Hera"]))
    castle_tower = rename_items((spoiler_object["Regions"]["Castle Tower"]))
    dark_palace = rename_items((spoiler_object["Regions"]["Palace of Darkness"]))
    swamp_palace = rename_items((spoiler_object["Regions"]["Swamp Palace"]))
    skull_woods = rename_items((spoiler_object["Regions"]["Skull Woods"]))
    thieves_town = rename_items((spoiler_object["Regions"]["Thieves' Town"]))
    ice_palace = rename_items((spoiler_object["Regions"]["Ice Palace"]))
    misery_mire = rename_items((spoiler_object["Regions"]["Misery Mire"]))
    turtle_rock = rename_items((spoiler_object["Regions"]["Turtle Rock"]))
    ganons_tower = rename_items((spoiler_object["Regions"]["Ganon's Tower"]))

    light_world_nw = rename_items((spoiler_object["Regions"]["Light World North West"]))
    light_world_ne = rename_items((spoiler_object["Regions"]["Light World North East"]))
    light_world_s  = rename_items((spoiler_object["Regions"]["Light World South"]))

    light_world = merge_dicts(light_world_ne, light_world_nw, light_world_s)

    death_mountain_w = rename_items((spoiler_object["Regions"]["Light World Death Mountain West"]))
    death_mountain_e = rename_items((spoiler_object["Regions"]["Light World Death Mountain East"]))

    death_mountain = merge_dicts(death_mountain_w, death_mountain_e)

    spike_cave = rename_items((spoiler_object["Regions"]["Dark World Death Mountain West"]))
    dw_dm_e = rename_items((spoiler_object["Regions"]["Dark World Death Mountain East"]))
    dw_nw = rename_items((spoiler_object["Regions"]["Dark World North West"]))
    dw_ne = rename_items((spoiler_object["Regions"]["Dark World North East"]))
    dw_s = rename_items((spoiler_object["Regions"]["Dark World South"]))
    dw_mire = rename_items((spoiler_object["Regions"]["Dark World Mire"]))

    dark_world = merge_dicts(dw_dm_e, spike_cave, dw_ne, dw_nw, dw_s, dw_mire)

    # SM

    crat_west = rename_items((spoiler_object["Regions"]["Crateria West"]))
    crat_central = rename_items((spoiler_object["Regions"]["Crateria Central"]))
    crat_east = rename_items((spoiler_object["Regions"]["Crateria East"]))

    crateria = merge_dicts(crat_west, crat_central, crat_east)

    brin_blue = rename_items((spoiler_object["Regions"]["Brinstar Blue"]))
    brin_green = rename_items((spoiler_object["Regions"]["Brinstar Green"]))
    brin_pink = rename_items((spoiler_object["Regions"]["Brinstar Pink"]))
    brin_red = rename_items((spoiler_object["Regions"]["Brinstar Red"]))
    brin_kraid = rename_items((spoiler_object["Regions"]["Brinstar Kraid"]))

    brinstar = merge_dicts(brin_green, brin_pink, brin_blue, brin_red, brin_kraid)

    wrecked_ship = rename_items((spoiler_object["Regions"]["Wrecked Ship"]))

    maridia_outer = rename_items((spoiler_object["Regions"]["Maridia Outer"]))
    maridia_inner = rename_items((spoiler_object["Regions"]["Maridia Inner"]))
    
    maridia = merge_dicts(maridia_outer, maridia_inner)

    un_west = rename_items((spoiler_object["Regions"]["Norfair Upper West"]))
    un_east = rename_items((spoiler_object["Regions"]["Norfair Upper East"]))
    croc = rename_items((spoiler_object["Regions"]["Norfair Upper Crocomire"]))

    upper_norfair = merge_dicts(un_west, un_east, croc)

    ln_west = rename_items((spoiler_object["Regions"]["Norfair Lower West"]))
    ln_east = rename_items((spoiler_object["Regions"]["Norfair Lower East"]))

    lower_norfair = merge_dicts(ln_west, ln_east)

    metadata = handle_meta((spoiler_object["Meta"]),spoiler_object["Game"])
    
    zelda_spoiler = {            
        "Hyrule Castle": hyrule_castle,
        "Eastern Palace": eastern_palace,
        "Desert Palace": desert_palace,
        "Tower of Hera": tower_of_hera,
        "Castle Tower": castle_tower,
        "Palace of Darkness": dark_palace,
        "Swamp Palace": swamp_palace,
        "Skull Woods": skull_woods,
        "Thieves Town": thieves_town,
        "Ice Palace": ice_palace,
        "Misery Mire": misery_mire,
        "Turtle Rock": turtle_rock,
        "Ganons Tower": ganons_tower,
        "Light World": light_world,
        "Death Mountain": death_mountain,
        "Dark World": dark_world
    }
    metroid_spoiler = {
        "Crateria": crateria,
        "Brinstar": brinstar,
        "Wrecked Ship": wrecked_ship,
        "Maridia": maridia,
        "Upper Norfair": upper_norfair,
        "Lower Norfair": lower_norfair
    }
    combined_spoiler = {
        "Prizes": prizes_and_medallions["Prizes"],
        "Special": prizes_and_medallions["Special"],
        "A Link to the Past": zelda_spoiler,
        "Super Metroid": metroid_spoiler,
        "Drops": metadata["Drops"],
        "meta": metadata["meta"]
    }
    return combined_spoiler


def main():
    race_mode = False

    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="spoiler", default="spoiler.yaml", help="Name of the spoiler log file to be parsed. Should be a yaml.")
    parser.add_argument("-o", "--output", dest="output", default="output.json", help="Name of the output file.")
    args = parser.parse_args()
    spoiler = args.spoiler
    output = args.output
    
    with open(spoiler, 'r') as yaml_in, open(output, "w") as json_out:
        spoiler_object = yaml.safe_load(yaml_in) # yaml_object will be a list or a dict
        
        # MODIFYING THE SPOILER

        try:
            if list(spoiler_object[1])[0] == "Playthrough": 
                spoiler_object.pop(1) # remove playthrough object
        except KeyError:
            race_mode = True # race spoiler has a slightly different layout which makes my life hell

        if not race_mode:
            combined_spoiler = compile_nonrace_spoiler(spoiler_object)
        else:
            combined_spoiler = compile_race_spoiler(spoiler_object)
        

        json.dump(combined_spoiler, json_out, indent=4)
        print("Conversion complete.")
        return True

main()
