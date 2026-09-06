# Universal Circle Memory - A Memory Required By All

**Problem:** Everyone forgets — birthdays, promises, likes. Founder forgets investor decks, customers, metrics.

**Solution:** One universal memory for your entire circle. Built on Solari.

**Why Universal = Founder (Demo Day, Investor Promises, Customer Evolution) + Family (Birthdays) = Everyone needs circle memory. TAM expansion for Solari.**

## Production Ready
- **REAL Solari:** `pip install solari-ai`, if SOLARI_API_KEY set → real cloud, else local fallback (works in Codespace)
- **GRAVITY:** 0.95 Investor Demo Day + 0.9 Promise to Sarah + 0.95 Mom birthday > 0.3 random like (founder + family priority)
- **FORK:** Tracks change over time — Rahul wants free plan -> enterprise plan (customer upsell evolution, no history delete)
- **API:** `uvicorn app:app --reload`
- **Docker:** `docker build . && docker run -p 8000:8000`

## Quick Start
`pip install -r requirements.txt && python main.py`

**Stack:** REAL solari-ai SDK + local fallback, FastAPI, Docker, Release v1.0.0
