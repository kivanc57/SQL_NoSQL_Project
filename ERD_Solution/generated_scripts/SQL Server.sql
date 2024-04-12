CREATE TABLE [students] (
  [student_id] integer PRIMARY KEY,
  [first_name] varchar(50) NOT NULL,
  [last_name] varchar(50) NOT NULL,
  [birth_date] date NOT NULL,
  [school_email] varchar(100) UNIQUE NOT NULL,
  [address] varchar(255) NOT NULL,
  [credits_gained] int DEFAULT (0)
)
GO

CREATE TABLE [teachers] (
  [teacher_id] integer PRIMARY KEY,
  [first_name] varchar(50) NOT NULL,
  [last_name] varchar(50) NOT NULL,
  [birth_date] date NOT NULL,
  [school_email] varchar(100) UNIQUE NOT NULL,
  [address] varchar(255) NOT NULL,
  [office_no] varchar(10)
)
GO

CREATE TABLE [classrooms] (
  [class_id] integer PRIMARY KEY,
  [class_number] varchar(10) UNIQUE NOT NULL,
  [max_capacity] integer NOT NULL
)
GO

CREATE TABLE [courses] (
  [course_id] integer PRIMARY KEY,
  [course_name] varchar(100) UNIQUE NOT NULL,
  [course_type] char(1) NOT NULL,
  [from_date] datetime NOT NULL,
  [to_date] datetime NOT NULL,
  [credits] integer NOT NULL
)
GO

CREATE TABLE [teaches] (
  [teacherID] integer,
  [subjectID] integer
)
GO

CREATE TABLE [attends] (
  [studentID] integer,
  [subjectID] integer
)
GO

CREATE TABLE [assigned] (
  [studentID] integer,
  [courseID] integer
)
GO

CREATE TABLE [course_assignment] (
  [classID] integer,
  [subjectID] integer
)
GO

ALTER TABLE [teachers] ADD FOREIGN KEY ([teacher_id]) REFERENCES [teaches] ([teacherID])
GO

ALTER TABLE [courses] ADD FOREIGN KEY ([course_id]) REFERENCES [teaches] ([subjectID])
GO

ALTER TABLE [students] ADD FOREIGN KEY ([student_id]) REFERENCES [attends] ([studentID])
GO

ALTER TABLE [courses] ADD FOREIGN KEY ([course_id]) REFERENCES [attends] ([subjectID])
GO

ALTER TABLE [students] ADD FOREIGN KEY ([student_id]) REFERENCES [assigned] ([studentID])
GO

ALTER TABLE [courses] ADD FOREIGN KEY ([course_id]) REFERENCES [assigned] ([courseID])
GO

ALTER TABLE [course_assignment] ADD FOREIGN KEY ([classID]) REFERENCES [classrooms] ([class_id])
GO

ALTER TABLE [course_assignment] ADD FOREIGN KEY ([subjectID]) REFERENCES [courses] ([course_id])
GO
