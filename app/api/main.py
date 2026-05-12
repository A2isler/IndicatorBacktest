"""Minimal local HTTP server for scaffold visibility (no external deps)."""

from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import yaml


def _load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Invalid YAML object: {path}")
    return data


class AppHandler(BaseHTTPRequestHandler):
    config_dir = Path("app/configs")

    def _send_json(self, payload: dict, status: int = 200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):  # noqa: N802
        if self.path == "/health":
            self._send_json({"status": "ok"})
            return

        if self.path == "/config":
            try:
                backtest = _load_yaml(self.config_dir / "backtest.yaml")
                providers = _load_yaml(self.config_dir / "providers.yaml")
                symbols = _load_yaml(self.config_dir / "symbols.yaml")
            except Exception as exc:  # pragma: no cover - minimal server path
                self._send_json({"status": "error", "message": str(exc)}, status=500)
                return

            self._send_json(
                {
                    "status": "ok",
                    "backtest": backtest,
                    "providers": providers,
                    "symbols": symbols,
                }
            )
            return

        self._send_json(
            {
                "status": "ok",
                "message": "IndicatorBacktest local server",
                "endpoints": ["/health", "/config"],
            }
        )


def run(host: str = "127.0.0.1", port: int = 8000):
    server = HTTPServer((host, port), AppHandler)
    print(f"Server running at http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
