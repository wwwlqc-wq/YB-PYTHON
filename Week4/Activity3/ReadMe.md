# 📌 Week4 — Activity3

## 📄 Project Overview

This Python project demonstrates basic database design and operations using SQLite3 with an object‑oriented approach.  
It focuses on implementing **CRUD operations**, **entity classes**, and **generic repository patterns** to interact with a designed university/course database.

---

## 📍 Core Features

### 🧱 1. Database Schema

The following tables are created in SQLite:

- **students**  
- **teachers**  
- **courses**  
- **enrollments** (student ↔ course relation)  
- **teaching_assignments** (teacher ↔ course relation)

These tables include common audit fields (`create_time`, `modify_time`, `is_deleted`) to manage soft deletion and tracking of records.

---

## 🛠 Architecture

### 🔹 Entities (Python Classes)

Each database table has a corresponding Python class extending a base entity class:

- `Student`
- `Teacher`
- `Course`
- `Enrollment`
- `TeachingAssignment`

Each entity encapsulates its fields and supports automatic handling of auditing values (timestamps and soft delete).

---

### 📦 Generic Repository

A generic repository (`Repository[T]`) is implemented to provide:

- Create (`insert`)
- Read (`select`, `select_by_id`)
- Update (`update_by_id`)
- Soft delete and hard delete
- Pagination
- Support for flexible conditions

The repository adapts automatically to SQLite by switching placeholders (`?`).

---

### 🧪 Core Business Logic

The project includes examples comparing real use cases such as:

- Counting students enrolled in a specific course  
- Listing teachers teaching a given course  
- Demonstrating pagination and filtered queries

These are implemented using the generic repositories and tested against sample datasets.

---

## 🧰 Setup and Usage

### 📌 Requirements

```bash
pip install pymysql
