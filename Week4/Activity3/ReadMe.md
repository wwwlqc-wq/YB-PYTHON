📌 Project Name

University Course Management OOP + Generic Python CRUD Framework

📍 Core Objective

This project demonstrates how to implement an OOP-based Python project to manage a university course system.

Key objectives:

Model students, teachers, courses, enrollments, and teaching assignments.

Support CRUD operations using generic repositories.

Handle audit fields (create_time, modify_time) and soft deletes (is_deleted).

Demonstrate common queries:

Count the number of students enrolled in a course.

List all teachers teaching a specific course.

🛠 Key Technologies
⭐ 1. Python Standard Library

sqlite3 for database operations.

datetime for managing timestamps.

typing for generics: TypeVar, Generic, Type.

🧱 2. Database Abstraction Layer

DBEngine abstract base class for database operations.

SQLiteEngine implements execute, fetch, executescript, commit, rollback, close.

Parameterized queries to prevent SQL injection.

🧠 3. Generic Repository Design

Repository[T] supports any entity subclass of BaseEntity.

Provides CRUD operations:

insert, select, select_by_id

update_by_id, soft_delete, hard_delete

Supports pagination and LIKE queries.

Automatically handles audit fields and soft delete flags.

🧾 4. ORM-Like Entity Mapping

BaseEntity includes:

create_time, modify_time, is_deleted

Optional primary key specification (__id_field__)

Entities can be easily converted to dictionaries for SQL mapping.

🔍 5. SQL Logging with AOP

debug_sql decorator logs SQL queries before execution.

Colors SQL keywords and parameters for readability.

Shows execution time for monitoring performance.

🧪 6. Data and Business Implementation

Entities created for:

Students (50 records)

Teachers (10 records)

Courses (5 records)

Enrollments (Student-Course mapping)

TeachingAssignments (Teacher-Course mapping)

Example queries implemented using repositories:

Count students in MSE800.

List teachers for MSE801.

🧩 Design Highlights

Generic + Base classes improve code reuse.

Clean layered architecture separates entities, repositories, and DB engine.

Dynamic SQL placeholders (? for SQLite, %s for MySQL).

Automatic audit field management.

Supports soft delete and hard delete.

Pagination and fuzzy search support.

SQL debug logging for observability.