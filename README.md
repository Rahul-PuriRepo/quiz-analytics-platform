# Quiz Analytics Platform

A production-oriented Quiz Analytics Platform built using **React**, **FastAPI**, and **MongoDB**.

The platform is designed around clean architecture principles, event-driven analytics, and scalable backend engineering practices.

---

## Vision

Rather than storing only quiz scores, this platform captures every quiz interaction as immutable events and derives meaningful learning insights using MongoDB aggregation pipelines.

Core philosophy:

> Store facts. Compute insights.

---

## Tech Stack

### Frontend

- React
- Vite

### Backend

- FastAPI
- Python

### Database

- MongoDB

### Documentation

- Swagger UI (OpenAPI)

---

## Project Structure

```text
backend/
frontend/
docs/
diagrams/
scripts/
```

---

## Current Progress

- [x] Repository Initialized
- [x] Project Architecture Designed
- [x] FastAPI Configured
- [x] Swagger Documentation
- [x] APIRouter Setup
- [ ] MongoDB Connection
- [ ] Repository Layer
- [ ] Service Layer
- [ ] Quiz Engine
- [ ] Analytics Engine
- [ ] React Integration
- [ ] Deployment

---

## Architecture Philosophy

This project follows a layered architecture.

```text
React

↓

FastAPI

↓

API Layer

↓

Service Layer

↓

Repository Layer

↓

MongoDB

↓

Analytics
```

Every layer owns exactly one responsibility.

---

## Design Principles

- Single Responsibility Principle
- Separation of Concerns
- Repository Pattern
- Service Layer Pattern
- Event-driven Analytics
- Configuration Management
- Clean Project Structure

---

## Status

🚧 Currently under active development.


## Roadmap

### Phase 1
- [x] Project Architecture
- [x] FastAPI Setup
- [x] Swagger Documentation

### Phase 2
- [ ] MongoDB Integration
- [ ] Repository Pattern
- [ ] Service Layer

### Phase 3
- [ ] Quiz Engine
- [ ] Event Tracking

### Phase 4
- [ ] Learning Velocity Index
- [ ] Fatigue Analysis
- [ ] Question Difficulty Index

### Phase 5
- [ ] React Integration
- [ ] Deployment