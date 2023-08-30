CREATE TABLE "public"."effects" (
    "id" INT GENERATED ALWAYS AS IDENTITY,
    "name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "buffs" TEXT NULL,
    "debuffs" TEXT NULL,
    CONSTRAINT "effects_pkey" PRIMARY KEY ("id")
);

INSERT INTO "public"."effects"
  ("name", "description", "buffs", "debuffs") 
VALUES
  ('Healing', 'heals', 'increases health', NULL),
  ('Poison', 'poisons', NULL, 'decreases health'),
  ('Fire', 'creates fire', 'increases power', NULL),
  ('Water', 'creates water', 'increases water power', NULL),
  ('Lightning', 'creates lightning', 'increases electricity power', NULL);
