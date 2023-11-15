INSERT INTO "setup"."creature_types"
  ("name",
  "description",
  "observations",
  "time_probabilities", 
  "hit_points_range",
  "agility_range",
  "charisma_range",
  "endurance_range",
  "intelligence_range",
  "mana_range",
  "perception_range",
  "strength_range"
  )
VALUES
  ('ogre', 'A ugly angry ogre', ARRAY ['The ogre appears to be carrying something', 'It looks shiny and valuable'], ARRAY[1, 0.4, 0.4, 0.7], ARRAY [10, 20], ARRAY [1, 5], ARRAY[1,3], ARRAY[15,20], ARRAY[1,2], ARRAY[0,1], ARRAY[0,3], ARRAY[15,25]),
  ('fairy', 'A tiny bright fairy', ARRAY ['The fairy is incredibly fast', 'magic dust flies around you'], ARRAY[0.4, 0.7, 0.9, 0.1], ARRAY [4, 8], ARRAY [15, 20], ARRAY[15,19], ARRAY [10,15], ARRAY[22,27], ARRAY[15,21], ARRAY[14,19], ARRAY[5,9]);

INSERT INTO "setup"."creature_type_immunities"
  ("creature_type_id", "damage_type_id")
VALUES
  (1, 3),
  (2, 9);

INSERT INTO "setup"."creature_type_resistances"
  ("creature_type_id", "damage_type_id")
VALUES
  (1, 2),
  (2, 6);

INSERT INTO "setup"."creature_type_weaknesses"
  ("creature_type_id", "damage_type_id")
VALUES
  (1, 9),
  (2, 4);
