CREATE TABLE "public"."locations" (
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

CREATE TABLE "public"."location_creature_types" (
    "location_id" INT NOT NULL,
    "creature_type_id" INT NOT NULL,
    CONSTRAINT "location_creature_types_uniq" UNIQUE ("location_id", "creature_type_id"),
    CONSTRAINT "location_creature_types_location_id_fkey" FOREIGN KEY ("location_id") REFERENCES "public"."locations"("id"),
    CONSTRAINT "location_creature_types_creature_type_id_fkey" FOREIGN KEY ("creature_type_id") REFERENCES "public"."creature_types"("id")
);

CREATE TABLE "public"."location_items" (
    "location_id" INT NOT NULL,
    "item_id" INT NOT NULL,
    CONSTRAINT "location_items_uniq" UNIQUE ("location_id", "item_id"),
    CONSTRAINT "location_items_location_id_fkey" FOREIGN KEY ("location_id") REFERENCES "public"."locations"("id"),
    CONSTRAINT "location_items_item_id_fkey" FOREIGN KEY ("item_id") REFERENCES "public"."items"("id")
);
