CREATE TABLE "Airports" (
  "airport_id" serial PRIMARY KEY,
  "name" varchar(100),
  "city" varchar(100),
  "country" varchar(100)
);

ALTER TABLE "Airports"
RENAME TO "InternationalAirports";

ALTER TABLE "InternationalAirports"
ADD COLUMN "code" varchar(10);

ALTER TABLE "InternationalAirports"
DROP COLUMN "code"