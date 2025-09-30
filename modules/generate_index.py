# generate_index.py
"""
Markdown Index Generator
Scans the output folder for workflow markdown files and creates a clickable index.
"""

import os

def generate_index():
    output_dir = "output"
    index_file = os.path.join(output_dir, "workflow_index.md")

    # Confirm output folder exists
    if not os.path.exists(output_dir):
        print(f"[!] Output folder not found: {output_dir}")
        return

    # Find all markdown files that start with 'workflow_'
    md_files = [f for f in os.listdir(output_dir) if f.startswith("workflow_") and f.endswith(".md")]

    if not md_files:
        print("[!] No workflow markdown files found.")
        return

    print(f"[*] Found {len(md_files)} markdown files.")

    # Build markdown index content
    lines = ["# 📚 Workflow Summary Index\n", "Click any scenario to view its full attacker/defender output.\n"]

    for filename in sorted(md_files):
        scenario_name = filename.replace("workflow_", "").replace(".md", "").replace("_", " ").title()
        lines.append(f"- [{scenario_name}]({filename})")

    # Save index file
    with open(index_file, "w") as f:
        f.write("\n".join(lines))

    print(f"[+] Markdown index saved to {index_file}")

if __name__ == "__main__":
    generate_index()
