INSERT INTO "setup"."item_types"
  ("name", "description", "observations", "weight", "value", "hit_points", "starting_hit_points", "attack_points", "uses_count")
VALUES
  ('Sword', 'A sharp sword', ARRAY ['It shines in the light', 'It is very sharp'], 400, 10, 100, 100, 20, -1),
  ('Shield', 'A sturdy shield', ARRAY ['It is polished to a fine sheen'], 350, 10, 100, 100, 3, -1),
  ('Healing Potion', 'Red fluid in a glass container', ARRAY ['The liquid within the vial shimmers and swirls'], 10, 25, 5, 5, 2, 1),
  ('Gold', 'A gold coin', NULL, 1, 1, 1000, 1000, 0, 1),
  ('Diamond', 'An small but exquisite gem', NULL, 1, 500, 1000000, 1000000, 0, 1),
  ('Barrel', 'A wooden barrel', NULL, 300, 10, 20, 20, 20, -1),
  ('Chest', 'An iron chest', ARRAY ['It is extremely heavy'], 750, 50, 30, 30, 40, -1),
  ('Pouch', 'A cloth pouch', NULL, 5, 1, 1, 1, 0, -1);

INSERT INTO "setup"."contained_item_types" 
  ("item_type_id", "contained_item_type_id", "contained_item_type_amount")
VALUES
  (6, 1, 2),
  (7, 2, 1),
  (7, 8, 1),
  (8, 3, 10);

INSERT INTO "setup"."item_type_effects" 
  ("item_type_id", "effect_id")
VALUES
  (1, 3),
  (3, 1);