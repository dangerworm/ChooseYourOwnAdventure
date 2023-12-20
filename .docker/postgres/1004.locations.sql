INSERT INTO "setup"."locations"
(
  "time_based_descriptions",
  "observations",
  "exits",
  "x",
  "y"
)
VALUES

--location 1

(
  ARRAY ['It''s a bright sunlit morning.', 
  'It''s a calm, breezy afternoon.', 
  'It''s a quiet, warm evening.', 
  'It''s a dark, gloomy night.'], --time based descriptions
  'This looks like Ogre country...', --observations
  ARRAY [2], --exits
  4, --x coord
  1--y coord
),

--location 2

(
  ARRAY ['Location  morning.', 
  'Location 2 afternoon.', 
  'Location 2 evening.',
  'Location 2 night.'], --time based descriptions
  'This looks like a peaceful spot', --observations
  ARRAY [0, 1, 2, 3], --exits
  4, --x coord
  2--y coord
),

--location 3

(
  ARRAY ['As you continue along the path to the north, you eventually arrive at a small jungle village. 
  The villagers look at you warily, as they have never seen someone like you before. The village is made up 
  of a collection of small huts and buildings, with thatched roofs and walls made from woven branches and mud. 
  As you look around, you see that the villagers are going about their daily activities. Some are tending to 
  crops in the nearby fields, while others are preparing food over open fires. The air is thick with the sound 
  of jungle animals and birds, and the scent of cooking fires and jungle plants. You notice that there is only 
  one exit from the village, and that is back the way you came to the west. This realization makes you feel a little 
  uneasy, as you realize that you are completely surrounded by the dense jungle. Despite this, you also feel a sense 
  of wonder and curiosity about this new place, and you wonder what kind of adventures await you in this mysterious 
  corner of the world.', 'As you continue along the path to the north, you eventually arrive at a small jungle village. 
  The villagers look at you warily, as they have never seen someone like you before. The village is made up of a 
  collection of small huts and buildings, with thatched roofs and walls made from woven branches and mud. As you 
  look around, you see that the villagers are going about their daily activities. Some are tending to crops in the 
  nearby fields, while others are preparing food over open fires. The air is thick with the sound of jungle animals 
  and birds, and the scent of cooking fires and jungle plants. You notice that there is only one exit from the village, 
  and that is back the way you came to the west. This realization makes you feel a little uneasy, as you realize that 
  you are completely surrounded by the dense jungle. Despite this, you also feel a sense of wonder and curiosity about 
  this new place, and you wonder what kind of adventures await you in this mysterious corner of the world.', 
  'Location 3 afternoon.', 
  'Location 3 evening.',
  'Location 3 night.'], --time based descriptions
  'You hear something nearby', --observations
  ARRAY [3], --exits
  11, --x coord
  1--y coord
),

--location 4

(
  ARRAY ['Location 4 morning.', 
  'Location 4 afternoon.', 
  'Location 4 evening.',
  'Location 4 night.'], --time based descriptions
  'You can see a toad, it looks suspicious..', --observations
  ARRAY [1, 2], --exits
  2, --x coord
  2--y coord
),

--location 5

(
  ARRAY ['Location 5 morning.', 
  'Location 5 afternoon.', 
  'Location 5 evening.',
  'Location 5 night.'], --time based descriptions
  'You can not see a thing, it is far too foggy.', --observations
  ARRAY [0, 1, 2, 3], --exits
  4, --x coord
  2--y coord
),

--location 6

(
  ARRAY ['Location 6 morning.', 
  'Location 6 afternoon.', 
  'Location 6 evening.',
  'Location 6 night.'], --time based descriptions
  'There are no words to describe what you see.', --observations
  ARRAY [3, 1, 2], --exits
  6, --x coord
  2--y coord
),

--location 7
(
  ARRAY ['Location 7 morning.', 
  'Location 7 afternoon.', 
  'Location 7 evening.',
  'Location 7 night.'], --time based descriptions
  'You can smell a fire burning somewhere', --observations
  ARRAY [3, 0, 2], --exits
  9, --x coord
  2--y coord
),

--location 8
(
  ARRAY ['Location 8 morning.', 
  'Location 8 afternoon.', 
  'Location 8 evening.',
  'Location 8 night.'], --time based descriptions
  'You can smell something awful. Just awful!', --observations
  ARRAY [0], --exits
  2, --x coord
  3--y coord
),

--location 9
(
  ARRAY ['Location 9 morning.', 
  'Location 9 afternoon.', 
  'Location 9 evening.',
  'Location 9 night.'], --time based descriptions
  'You cannot see anything at all.', --observations
  ARRAY [3], --exits
  11, --x coord
  3--y coord
),

--location 10
(
  ARRAY ['Location 10 morning.', 
  'Location 10 afternoon.', 
  'Location 10 evening.',
  'Location 10 night.'], --time based descriptions
  'You see a smouldering fire.', --observations
  ARRAY [0, 2], --exits
  4, --x coord
  6--y coord
),

--location 11
(
  ARRAY ['Location 11 morning.', 
  'Location 11 afternoon.', 
  'Location 11 evening.',
  'Location 11 night.'], --time based descriptions
  'A well trodden path is before you.', --observations
  ARRAY [0, 2], --exits
  7, --x coord
  6--y coord
),

--location 12
(
  ARRAY ['Location 12 morning.', 
  'Location 12 afternoon.', 
  'Location 12 evening.',
  'Location 12 night.'], --time based descriptions
  'A burning hut is in the distance.', --observations
  ARRAY [0, 1, 2, 3], --exits
  4, --x coord
  8--y coord
),

--location 13
(
  ARRAY ['Location 13 morning.', 
  'Location 13 afternoon.', 
  'Location 13 evening.',
  'Location 13 night.'], --time based descriptions
  'You are concerned you are going in circles.', --observations
  ARRAY [0], --exits
  0, --x coord
  9--y coord
),

--location 14
(
  ARRAY ['Location 14 morning.', 
  'Location 14 afternoon.', 
  'Location 14 evening.',
  'Location 14 night.'], --time based descriptions
  'You are sure you have been here before. It is all getting confusing.', --observations
  ARRAY [0, 1, 2, 3], --exits
  3, --x coord
  13--y coord
),

--location 15
(
  ARRAY ['Location 15 morning.', 
  'Location 15 afternoon.', 
  'Location 15 evening.',
  'Location 15 night.'], --time based descriptions
  'You cannot see anything, but you can hear some faint whispers amongst the trees.', --observations
  ARRAY [0], --exits
  1, --x coord
  15--y coord
),

--location 16
(
  ARRAY ['Location 16 morning.', 
  'Location 16 afternoon.', 
  'Location 16 evening.',
  'Location 16 night.'], --time based descriptions
  'You see a ghostly image in front of you.', --observations
  ARRAY [1, 3], --exits
  9, --x coord
  8--y coord
),

--location 17
(
  ARRAY ['Location 17 morning.', 
  'Location 17 afternoon.', 
  'Location 17 evening.',
  'Location 17 night.'], --time based descriptions
  'You are getting weary.', --observations
  ARRAY [0, 2], --exits
  3, --x coord
  17--y coord
);

INSERT INTO "setup"."location_creature_types"
(
  "location_id",
  "creature_type_id",
  "creature_type_count"
)
VALUES
  (1, 1, 1),
  (2, 2, 1),
  (3, 1, 1),
  (4, 2, 1),
  (5, 1, 1),
  (6, 2, 1),
  (7, 1, 1),
  (8, 2, 1),
  (9, 1, 1),
  (10, 2, 1),
  (11, 1, 1),
  (12, 2, 1),
  (13, 1, 1),
  (14, 2, 1),
  (15, 1, 1),
  (16, 2, 1),
  (17, 1, 1);
  
INSERT INTO "setup"."location_item_types"
(
  "location_id",
  "item_type_id",
  "item_type_count"
)
VALUES
  (1, 8, 1),
  (1, 1, 1),
  (2, 1, 1);