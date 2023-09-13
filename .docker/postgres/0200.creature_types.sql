CREATE TABLE "setup"."creature_types" (
    "id" int generated always as identity,
    "name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "observations" TEXT[] NULL,
    "time_probabilities" DECIMAL[] NOT NULL,
    "hit_points_range" INT[] NOT NULL,
    "agility_range" INT[] NOT NULL,
    "charisma_range" INT[] NOT NULL,
    "endurance_range" INT[] NOT NULL,
    "intelligence_range" INT[] NOT NULL,
    "mana_range" INT[] NOT NULL,
    "perception_range" INT[] NOT NULL,
    "strength_range" INT[] NOT NULL,
    CONSTRAINT "creature_types_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "setup"."creature_type_immunities" (
  "creature_type_id" INT NOT NULL,
  "damage_type_id" INT NOT NULL,
  CONSTRAINT "creature_type_immunities_pkey" PRIMARY KEY ("creature_type_id", "damage_type_id"),
  CONSTRAINT "creature_type_immunities_creature_type_id_fkey" FOREIGN KEY ("creature_type_id") REFERENCES "setup"."creature_types"("id"),
  CONSTRAINT "creature_type_immunities_damage_type_id_fkey" FOREIGN KEY ("damage_type_id") REFERENCES "common"."damage_types"("id")
);

CREATE TABLE "setup"."creature_type_resistances" (
  "creature_type_id" INT NOT NULL,
  "damage_type_id" INT NOT NULL,
  CONSTRAINT "creature_type_resistances_pkey" PRIMARY KEY ("creature_type_id", "damage_type_id"),
  CONSTRAINT "creature_type_resistances_creature_type_id_fkey" FOREIGN KEY ("creature_type_id") REFERENCES "setup"."creature_types"("id"),
  CONSTRAINT "creature_type_resistances_damage_type_id_fkey" FOREIGN KEY ("damage_type_id") REFERENCES "common"."damage_types"("id")
);

CREATE TABLE "setup"."creature_type_weaknesses" (
  "creature_type_id" INT NOT NULL,
  "damage_type_id" INT NOT NULL,
  CONSTRAINT "creature_type_weaknesses_pkey" PRIMARY KEY ("creature_type_id", "damage_type_id"),
  CONSTRAINT "creature_type_weaknesses_creature_type_id_fkey" FOREIGN KEY ("creature_type_id") REFERENCES "setup"."creature_types"("id"),
  CONSTRAINT "creature_type_weaknesses_damage_type_id_fkey" FOREIGN KEY ("damage_type_id") REFERENCES "common"."damage_types"("id")
);