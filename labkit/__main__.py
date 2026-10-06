"""Run `python -m labkit --help` from the repository root."""
from __future__ import annotations
import argparse
import sys
from pathlib import Path
from .common import load_json, write_json, write_text_private

def parser():
    p = argparse.ArgumentParser(description="Offline privacy-first reference tools")
    sub = p.add_subparsers(dest="command", required=True)
    for name in ("inventory", "training", "phishing", "plugins", "sessions", "sensors", "logs", "kpis"):
        cmd = sub.add_parser(name)
        cmd.add_argument("input", type=Path)
        cmd.add_argument("output", type=Path)
    cmp = sub.add_parser("compare")
    cmp.add_argument("before", type=Path); cmp.add_argument("after", type=Path)
    cmp.add_argument("output", type=Path); cmp.add_argument("--key", default="id")
    pim = sub.add_parser("pim")
    pim.add_argument("input", type=Path); pim.add_argument("output", type=Path)
    pim.add_argument("--since", required=True)
    pam = sub.add_parser("pam-plan")
    pam.add_argument("input", type=Path); pam.add_argument("output", type=Path)
    pam.add_argument("--suffix", required=True); pam.add_argument("--port", required=True, type=int)
    pam.add_argument("--safe")
    risks = sub.add_parser("risks")
    risks.add_argument("input", type=Path); risks.add_argument("output", type=Path)
    risks.add_argument("--as-of", required=True)
    corr = sub.add_parser("correlate")
    corr.add_argument("input", type=Path); corr.add_argument("output", type=Path)
    corr.add_argument("--ip", required=True); corr.add_argument("--as-of", required=True)
    corr.add_argument("--max-age-hours", default=12, type=float)
    report = sub.add_parser("html")
    report.add_argument("input", type=Path); report.add_argument("output", type=Path)
    report.add_argument("--title", default="Reference report")
    fit = sub.add_parser("fit")
    fit.add_argument("--source", nargs=3, type=float, required=True)
    fit.add_argument("--target", nargs=3, type=float, required=True)
    fit.add_argument("--clearance", type=float, default=0)
    fit.add_argument("output", type=Path)
    energy = sub.add_parser("energy")
    for flag in ("voltage", "amp-hours", "watts", "usable-fraction", "efficiency"):
        energy.add_argument("--" + flag, type=float, required=True)
    energy.add_argument("output", type=Path)
    flow = sub.add_parser("flow")
    for flag in ("collected-liters", "seconds", "reservoir-liters"):
        flow.add_argument("--" + flag, type=float, required=True)
    flow.add_argument("output", type=Path)
    return p

def main(argv=None):
    p = parser(); args = p.parse_args(argv)
    from . import inventory, awareness, pam, telemetry, vulnerability, reporting, engineering
    try:
        # Never overwrite an input, even through a resolved symlink path.
        for name in ("input", "before", "after"):
            source = getattr(args, name, None)
            if source is not None and source.resolve() == args.output.resolve():
                raise ValueError("Input and output must be different paths")
        data = load_json(args.input) if hasattr(args, "input") else None
        simple = {"training": awareness.training_audit, "phishing": awareness.phishing_summary,
                  "plugins": vulnerability.classify_plugins, "sessions": pam.session_summary,
                  "sensors": telemetry.sensor_summary, "logs": telemetry.log_summary,
                  "kpis": reporting.kpi_summary}
        if args.command in simple:
            result = simple[args.command](data)
        elif args.command == "inventory":
            result = inventory.reconcile(data["requested"], data["devices"])
        elif args.command == "compare":
            result = inventory.compare(load_json(args.before), load_json(args.after), args.key)
        elif args.command == "pim":
            result = awareness.pim_activations(data, args.since)
        elif args.command == "pam-plan":
            result = pam.port_plan(data, args.suffix, args.port, args.safe)
        elif args.command == "risks":
            result = vulnerability.review_risks(data, args.as_of)
        elif args.command == "correlate":
            result = telemetry.correlate_ip(data, args.ip, args.as_of, args.max_age_hours)
        elif args.command == "fit":
            result = engineering.fit_scale(args.source, args.target, args.clearance)
        elif args.command == "energy":
            result = engineering.energy_budget(args.voltage,args.amp_hours,args.watts,args.usable_fraction,args.efficiency)
        elif args.command == "flow":
            result = engineering.flow_measurement(args.collected_liters,args.seconds,args.reservoir_liters)
        elif args.command == "html":
            write_text_private(args.output, reporting.html_report(data,args.title))
            print("HTML report written. Review before sharing.")
            return 0
        else:
            raise ValueError("Unsupported command")
        write_json(args.output, result)
        print("Output written. Local outputs may contain confidential data; do not commit them.")
        return 0
    except (ValueError, KeyError, TypeError, OSError) as exc:
        # Avoid printing input data or response bodies in failure diagnostics.
        print(f"Input/output validation failed ({type(exc).__name__}). Check the schema and local file permissions.",file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
