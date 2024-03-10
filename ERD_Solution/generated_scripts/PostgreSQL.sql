CREATE TABLE "students" (
  "id" integer PRIMARY KEY,
  "first_name" varchar(255) NOT NULL,
  "last_name" varchar(255) NOT NULL,
  "birth_date" date NOT NULL,
  "school_email" varchar(255) UNIQUE NOT NULL,
  "address" varchar(255) NOT NULL,
  "credits_gained" int DEFAULT 0,
  "subjects_enrolled" varchar(255) UNIQUE NOT NULL
);

CREATE TABLE "teachers" (
  "id" integer PRIMARY KEY,
  "first_name" varchar(255) NOT NULL,
  "last_name" varchar(255) NOT NULL,
  "birth_date" date NOT NULL,
  "school_email" varchar(255) UNIQUE NOT NULL,
  "address" varchar(255) NOT NULL,
  "office_no" float,
  "subjects_teaching" varchar(255)
);

CREATE TABLE "classrooms" (
  "id" integer PRIMARY KEY,
  "class_number" float UNIQUE NOT NULL,
  "max_capacity" integer NOT NULL,
  "subjects_held" varchar(255) UNIQUE
);

CREATE TABLE "courses" (
  "id" integer PRIMARY KEY,
  "course_name" varchar(255) UNIQUE NOT NULL,
  "course_type" char(1) NOT NULL,
  "is_open" boolean DEFAULT 1,
  "from_date" datetime NOT NULL,
  "to_date" datetime NOT NULL,
  "place" float NOT NULL,
  "credits" integer NOT NULL
);

CREATE TABLE "students_courses" (
  "students_subjects_enrolled" varchar(255),
  "courses_course_name" varchar(255),
  PRIMARY KEY ("students_subjects_enrolled", "courses_course_name")
);

ALTER TABLE "students_courses" ADD FOREIGN KEY ("students_subjects_enrolled") REFERENCES "students" ("subjects_enrolled");

ALTER TABLE "students_courses" ADD FOREIGN KEY ("courses_course_name") REFERENCES "courses" ("course_name");


ALTER TABLE "courses" ADD FOREIGN KEY ("place") REFERENCES "classrooms" ("class_number");

CREATE TABLE "teachers_courses" (
  "teachers_subjects_teaching" varchar(255),
  "courses_course_name" varchar(255),
  PRIMARY KEY ("teachers_subjects_teaching", "courses_course_name")
);

ALTER TABLE "teachers_courses" ADD FOREIGN KEY ("teachers_subjects_teaching") REFERENCES "teachers" ("subjects_teaching");

ALTER TABLE "teachers_courses" ADD FOREIGN KEY ("courses_course_name") REFERENCES "courses" ("course_name");

