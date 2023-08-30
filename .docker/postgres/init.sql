GRANT ALL PRIVILEGES ON DATABASE postgres TO postgres;

CREATE TABLE "public"."test" (
    "id" int generated always as identity,
    "name" TEXT COLLATE "pg_catalog"."default" NOT NULL,
    CONSTRAINT "test_pkey" PRIMARY KEY ("id")
);

INSERT INTO "public"."test" ("name") 
VALUES ('Hello, World!');

CREATE TABLE "public"."effects" (
    "id" int generated always as identity,
    "name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "buffs" TEXT NULL,
    "debuffs" TEXT NULL,
    CONSTRAINT "effects_pkey" PRIMARY KEY ("id")
);

INSERT INTO "public"."effects" ("name", "description", "buffs", "debuffs") 
VALUES 
('Magic', 'creates fire', 'increases power', Null),
('Magic', 'creates water', 'increases water power', Null),
('Magic', 'creates lightning', 'increases electricity power', Null)
;
