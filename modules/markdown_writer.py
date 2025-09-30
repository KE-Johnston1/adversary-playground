# markdown_writer.py
"""
Markdown Writer
Converts workflow JSON output into a clean, recruiter-ready markdown summary.
"""

import json
import os

def json_to_markdown(json_path):
    if not os.path.exists(json_path):
        print(f"[!] File not found: {json_path}")
        return

    with open(json_path, "r") as f:
        data = json.load(f)

    md_lines = ["# 📝 Module Output Summary\n"]

    # Scenario
    scenario = data.get("Scenario", "N/A")
    md_lines.append(f"### 🔹 Scenario\n**{scenario}**\n")

    # Injection Simulation
    injection = data.get("Injection Simulation", {})
    md_lines.append("### 🧨 Injection Simulation")
    md_lines.append(f"- **Original Prompt:**  \n  `{injection.get('Original Prompt', '')}`")
    md_lines.append(f"- **Injected Prompt:**  \n  `{injection.get('Injected Prompt', '')}`")
    md_lines.append(f"- **Expected Impact:**  \n  {injection.get('Expected Impact', '')}")
    tips = injection.get("Mitigation Tips", [])
    if tips:
        md_lines.append("- **Mitigation Tips:**")
        for tip in tips:
            md_lines.append(f"  - {tip}")
    md_lines.append("")

    # Sanitization Result
    sanitizer = data.get("Sanitization Result", {})
    md_lines.append("### 🛡️ Sanitization Result")
    md_lines.append(f"- **Original Input:**  \n  `{sanitizer.get('Original Input', '')}`")
    md_lines.append(f"- **Sanitized Input:**  \n  `{sanitizer.get('Sanitized Input', '')}`")
    flags = sanitizer.get("Risk Flags", [])
    if flags:
        md_lines.append("- **Risk Flags:**")
        for flag in flags:
            md_lines.append(f"  - {flag}")
    md_lines.append(f"- **Risk Score:**  \n  `{sanitizer.get('Risk Score', '')}`")
    md_lines.append(f"- **Risk Level:**  \n  `{sanitizer.get('Risk Level', '')}`")
    md_lines.append("")

    # Save markdown file
    md_filename = json_path.replace(".json", ".md")
    with open(md_filename, "w") as f:
        f.write("\n".join(md_lines))

    print(f"[+] Markdown summary saved to {md_filename}")

# Run directly
if __name__ == "__main__":
    json_to_markdown("output/workflow_reset_my_password.json")
