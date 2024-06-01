CREATE TABLE "public"."langchain_pg_collection" (
	"uuid" uuid NOT NULL,
	"name" varchar,
	"cmetadata" json,
	CONSTRAINT "langchain_pg_collection_pkey" PRIMARY KEY ("uuid")
);

CREATE TABLE "public"."langchain_pg_embedding" (
	"uuid" uuid NOT NULL,
	"collection_id" uuid,
	"embedding" vector(1536),
	"document" varchar,
	"cmetadata" json,
	"custom_id" varchar,
	CONSTRAINT "langchain_pg_embedding_pkey" PRIMARY KEY ("uuid")
);
