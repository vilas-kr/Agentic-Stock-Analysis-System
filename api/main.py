from fastapi import FastAPI, HTTPException
from orchestration.orchestration import run_trading_assistant

app = FastAPI()


@app.get("/")
async def home():
    return {"status": "running"}


@app.get("/analyze")
async def analyze(user_query: str):
    try:
        result = await run_trading_assistant(user_query)
        return result.model_dump()

    except Exception as e:

        error_message = str(e)
        # API Key Errors
        if any(keyword in error_message.lower() for keyword in [
            "api key",
            "apikey",
            "invalid key",
            "expired key"
        ]):
            raise HTTPException(
                status_code=401,
                detail="API key has expired or is invalid. Please update the API key."
            )

        # Rate Limit Errors
        if any(keyword in error_message.lower() for keyword in [
            "rate limit",
            "too many requests"
        ]):
            raise HTTPException(
                status_code=429,
                detail="API rate limit exceeded. Please try again later."
            )

        # Generic Errors
        raise HTTPException(
            status_code=500,
            detail=f"Analysis failed: {error_message}"
        )