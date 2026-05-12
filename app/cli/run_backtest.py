"""CLI entrypoint for scaffold validation and configuration preview."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
import yaml


def _load_yaml(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Config must be a mapping/object: {path}")
    return data


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="IndicatorBacktest CLI")
    parser.add_argument("--config-dir", default="app/configs", help="Path to config directory")
    parser.add_argument("--dry-run", action="store_true", help="Validate and print loaded config")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    config_dir = Path(args.config_dir)

    try:
        backtest = _load_yaml(config_dir / "backtest.yaml")
        providers = _load_yaml(config_dir / "providers.yaml")
        symbols = _load_yaml(config_dir / "symbols.yaml")
    except (FileNotFoundError, ValueError, yaml.YAMLError) as exc:
        print(f"[ERROR] {exc}")
        return 1

    symbol_count = len(symbols.get("symbols", [])) if isinstance(symbols.get("symbols"), list) else 0
    primary_provider = providers.get("providers", {}).get("primary", "unknown")
    risk_pct = float(backtest.get("backtest", {}).get("risk_per_trade", 0.0)) * 100

    print("IndicatorBacktest scaffold is ready.")
    print(f"- Config dir      : {config_dir}")
    print(f"- Primary provider: {primary_provider}")
    print(f"- Symbols loaded  : {symbol_count}")
    print(f"- Risk per trade  : {risk_pct:.2f}%")

    if args.dry_run:
        print("\n[DRY RUN] Loaded config keys:")
        print(f"  backtest : {list(backtest.keys())}")
        print(f"  providers: {list(providers.keys())}")
        print(f"  symbols  : {list(symbols.keys())}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
