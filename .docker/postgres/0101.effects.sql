CREATE TABLE "common"."effects" (
    "id" INT GENERATED ALWAYS AS IDENTITY,
    "name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "buffs" TEXT NULL,
    "debuffs" TEXT NULL,
    CONSTRAINT "effects_pkey" PRIMARY KEY ("id")
);
