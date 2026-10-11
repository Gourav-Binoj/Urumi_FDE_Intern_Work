from fastapi import FastAPI

app = FastAPI(title="Urumi MCP Gateway")

@app.get("/health")
def health():
    return {"status": "ok"}
