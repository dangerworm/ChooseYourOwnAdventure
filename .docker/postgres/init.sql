GRANT ALL PRIVILEGES ON DATABASE postgres TO postgres;

CREATE TABLE "public"."test" (
    "id" int4 NOT NULL,
    "name" TEXT COLLATE "pg_catalog"."default" NOT NULL,
    CONSTRAINT "test_pkey" PRIMARY KEY ("id")
);

INSERT INTO "public"."test" ("id", "name") 
VALUES (1, 'Hello, World!');