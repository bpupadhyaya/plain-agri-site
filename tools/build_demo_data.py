"""Builds assets/js/demo-data.js from the private PlainAgri content repo (public extracts only:
source titles/URLs, two free-tier calculators, one free-tier diagnostic tree). Re-run when content changes."""
import json, os
SRC = os.path.expanduser("~/coding_common/pvt/plain-agri/content/data")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sources = {s["id"]: s for s in json.load(open(f"{SRC}/sources.json"))}
calcs = {c["id"]: c for c in json.load(open(f"{SRC}/calculators.json"))}
tree = next(t for t in json.load(open(f"{SRC}/diagnostics.json")) if t["id"] == "leaf-yellowing")
keep = ["rainwater-harvest", "planting-date"]
need = set()
for k in keep: need |= set(calcs[k]["sources"])
for n in tree["nodes"].values():
    if "result" in n: need |= set(n["result"]["sources"])
data = {
  "sources": {i: {k: sources[i].get(k) for k in ("title", "publisher", "url", "kind")} for i in sorted(need)},
  "calculators": {k: {f: calcs[k][f] for f in ("id", "title", "summary", "inputs", "formula", "outputs", "notes", "assumptions", "sources")} for k in keep},
  "tree": tree,
}
open(f"{ROOT}/assets/js/demo-data.js", "w").write("window.PA_DATA=" + json.dumps(data, separators=(",", ":")) + ";\n")
print("sources", len(data["sources"]), "bytes", os.path.getsize(f"{ROOT}/assets/js/demo-data.js"))
