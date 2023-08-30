CREATE TABLE "public"."damage_types" (
    "id" INT GENERATED ALWAYS AS IDENTITY,
    "name" TEXT NOT NULL,
    CONSTRAINT "damage_types_pkey" PRIMARY KEY ("id")
);
