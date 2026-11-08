from fastapi import FastAPI
import redis

app = FastAPI(title="ThreadMatch API", version="1.0")

# Connect to the ThreadMatch Redis instance on port 6380
cache = redis.Redis(host='localhost', port=6380, db=0, decode_responses=True)

@app.get("/health")
def health_check():
    """Verify API and Redis connectivity."""
    redis_status = cache.ping()
    return {
        "status": "online",
        "redis_connected": redis_status,
        "mode": "antigravity"
    }