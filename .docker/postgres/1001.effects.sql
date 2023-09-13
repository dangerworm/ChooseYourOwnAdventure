INSERT INTO "common"."effects"
  ("name", "description", "buffs", "debuffs") 
VALUES
  ('Healing', 'heals', 'increases health', NULL),
  ('Poison', 'poisons', NULL, 'decreases health'),
  ('Fire', 'creates fire', 'increases power', NULL),
  ('Water', 'creates water', 'increases water power', NULL),
  ('Lightning', 'creates lightning', 'increases electricity power', NULL);
