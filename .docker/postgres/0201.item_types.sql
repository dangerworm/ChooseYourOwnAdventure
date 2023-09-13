CREATE TABLE "setup"."item_types" (
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
    CONSTRAINT "item_types_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "setup"."contained_item_types" (
    "item_type_id" INT NOT NULL,
    "contained_item_type_id" INT NOT NULL,
    "contained_item_type_amount" INT NOT NULL,
    CONSTRAINT "contained_item_types_pkey" PRIMARY KEY ("item_type_id", "contained_item_type_id"),
    CONSTRAINT "contained_item_types_item_type_id_fkey" FOREIGN KEY ("item_type_id") REFERENCES "setup"."item_types"("id"),
    CONSTRAINT "contained_item_types_contained_item_type_id_fkey" FOREIGN KEY ("contained_item_type_id") REFERENCES "setup"."item_types"("id")
);

CREATE TABLE "setup"."item_type_effects" (
    "item_type_id" INT NOT NULL,
    "effect_id" INT NOT NULL,
    CONSTRAINT "item_type_effects_pkey" PRIMARY KEY ("item_type_id", "effect_id"),
    CONSTRAINT "item_type_effects_item_type_id_fkey" FOREIGN KEY ("item_type_id") REFERENCES "setup"."item_types"("id"),
    CONSTRAINT "item_type_effects_effect_id_fkey" FOREIGN KEY ("effect_id") REFERENCES "common"."effects"("id")
);
