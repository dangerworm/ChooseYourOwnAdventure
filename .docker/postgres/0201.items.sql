CREATE TABLE "public"."items" (
    "id" int generated always as identity,
    "name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "observations" TEXT[] NULL,
    "value" INT NOT NULL,
    "weight" INT NOT NULL,
    "hit_points" INT NOT NULL,
    "starting_hit_points" INT NOT NULL,
    "attack_points" INT NOT NULL,
    "uses_count" INT NOT NULL,
    CONSTRAINT "items_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "public"."contained_items" (
    "item_id" INT NOT NULL,
    "contained_item_id" INT NOT NULL,
    CONSTRAINT "contained_items_uniq" UNIQUE ("item_id", "contained_item_id"),
    CONSTRAINT "contained_items_item_id_fkey" FOREIGN KEY ("item_id") REFERENCES "public"."items"("id"),
    CONSTRAINT "contained_items_contained_item_id_fkey" FOREIGN KEY ("contained_item_id") REFERENCES "public"."items"("id")
);

CREATE TABLE "public"."item_effects" (
    "item_id" INT NOT NULL,
    "effect_id" INT NOT NULL,
    CONSTRAINT "item_effects_uniq" UNIQUE ("item_id", "effect_id"),
    CONSTRAINT "item_effects_item_id_fkey" FOREIGN KEY ("item_id") REFERENCES "public"."items"("id"),
    CONSTRAINT "item_effects_effect_id_fkey" FOREIGN KEY ("effect_id") REFERENCES "public"."effects"("id")
);

