CREATE TABLE "setup"."locations" (
    "id" INT GENERATED ALWAYS AS IDENTITY,
    "name" TEXT NOT NULL,
    "time_based_descriptions" TEXT[] NOT NULL,
    "exits" INT[] NOT NULL,
    "observations" TEXT NULL,
    "x" INT NULL,
    "y" INT NULL,
    "creature_time_probabilities" DECIMAL[] NULL,
    CONSTRAINT "locations_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "setup"."location_creature_types" (
    "location_id" INT NOT NULL,
    "creature_type_id" INT NOT NULL,
    CONSTRAINT "location_creature_types_pkey" PRIMARY KEY ("location_id", "creature_type_id"),
    CONSTRAINT "location_creature_types_location_id_fkey" FOREIGN KEY ("location_id") REFERENCES "setup"."locations"("id"),
    CONSTRAINT "location_creature_types_creature_type_id_fkey" FOREIGN KEY ("creature_type_id") REFERENCES "setup"."creature_types"("id")
);

CREATE TABLE "setup"."location_item_types" (
    "location_id" INT NOT NULL,
    "item_type_id" INT NOT NULL,
    "item_type_count" INT NOT NULL,
    CONSTRAINT "location_item_types_pkey" UNIQUE ("location_id", "item_type_id"),
    CONSTRAINT "location_item_types_location_id_fkey" FOREIGN KEY ("location_id") REFERENCES "setup"."locations"("id"),
    CONSTRAINT "location_item_types_item_type_id_fkey" FOREIGN KEY ("item_type_id") REFERENCES "setup"."item_types"("id")
);
