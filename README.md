# 🚀 FastAPI Learning Journey

Welcome to my FastAPI learning repository! This repo is designed to help me (and others) learn **FastAPI** step by step, with well-documented examples, explanations, and real-world use cases.

---

## 📘 What is FastAPI?

> **FastAPI** is a modern, high-performance, web framework for building APIs with Python 3.7+ based on standard Python type hints.

- 🚀 Fast: One of the fastest Python frameworks
- 🧠 Easy: Designed for simplicity, intuitive usage, and clear docs
- 🔐 Built-in validation: Uses Pydantic for data validation
- 📦 Async-ready: Excellent support for `async/await`
- 📄 Auto-docs: Swagger and ReDoc integration by default

---

## 📁 01-Web-Server-Basics

This folder contains the foundational concepts of creating a web API using FastAPI.

### ✅ File: `main.py`

This is a simple web server demo with the following covered:

| Concept | Route | Description |
|--------|-------|-------------|
| Root Endpoint | `/` | Basic welcome message |
| Path Parameter | `/path-parameter/{name}` | Accepts value directly from the URL |
| Query Parameter | `/query-parameter?name=...` | Accepts query string input |
| Path + Query Parameter | `/path-with-query-parameter/{name}?age=...` | Combines both |
| Optional Parameters | `/optional-query-parameter` | Accepts or defaults values |
| Request Body with Pydantic | `/create-book` (POST) | Accepts JSON body using model |
| Request Headers | `/get-headers` | Displays incoming request headers |

---

## ▶️ How to Run

1. **Install dependencies**
    uv sync
    uv run 01-Web-Server-Basics
