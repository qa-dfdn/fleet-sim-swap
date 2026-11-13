"""Request handler for fleet-sim-swap."""

def handle(event: dict) -> dict:
    kind = event.get("kind", "scan")
    return {"ok": True, "kind": kind, "service": "fleet-sim-swap"}
