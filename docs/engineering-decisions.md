# Engineering Decisions

# Engineering Decision 1

Why Repository Pattern?

Repositories isolate data access from business logic.
This allows future migration from MongoDB to another
database with minimal impact on the rest of the codebase.

---

# Engineering Decision 2

Why Store Events Instead of Scores?

Scores are derived.

Events are facts.

Facts allow future analytics.

---

# Engineering Decision 3

Why FastAPI?

Automatic OpenAPI generation,
excellent typing support,
and clean dependency injection.


## Why Layered Architecture?

The application separates HTTP handling, business logic,
and data access to improve maintainability and testability.

---

## Why MongoDB?

Question attempts are naturally event documents.
MongoDB's document model and aggregation pipeline are
well suited for analytics.

---

## Why Store Facts Instead of Scores?

The platform stores immutable events
(question shown, answer selected, response time).

Derived analytics such as Learning Velocity
are computed later.

This keeps raw data intact
and allows analytics to evolve.

## Why Event Storage?

Instead of storing only quiz scores,
the application stores immutable quiz events.

This enables future analytics
without changing historical data.

## Lessons Learned

During this project I learned:

- Designing layered backend architectures
- Repository and Service patterns
- FastAPI routing
- MongoDB Atlas integration
- Event-driven analytics
- Engineering documentation
- Git workflow

