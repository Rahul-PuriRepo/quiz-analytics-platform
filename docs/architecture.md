# System Architecture

## Objective

Build a scalable Quiz Analytics Platform capable of capturing every user interaction and transforming raw events into meaningful learning insights.

---

## High-Level Flow

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

Analytics Engine

---

## Core Engineering Principle

Store facts.

Compute insights.

Never store derived analytics.

---

## Single Source of Truth

QuestionAttempt collection.

Every analytics API derives its results from QuestionAttempt events.

---

## Layer Responsibilities

### API

Receives HTTP requests.

Returns HTTP responses.

### Service

Implements business rules.

### Repository

Communicates with MongoDB.

### Database

Maintains connections.

### Analytics

Generates reports and insights.