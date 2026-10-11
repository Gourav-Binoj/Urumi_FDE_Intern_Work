from fastapi import FastAPI

app = FastAPI(title="Urumi MCP Gateway")

@app.get("/health")
def health():
    return {"status": "ok"}
@app.get("/")
def root():
    return {"service": "urumi-mcp-gateway", "docs": "/docs", "health": "/health"}