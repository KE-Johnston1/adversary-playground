# recon_bot.py
"""
Recon Bot Module
Simulates attacker-style OSINT gathering using AI-style logic.
Saves output to a JSON file for later visualization.
"""

import json
import os

def simulate_recon(target_name, target_domain):
    print(f"[+] Starting recon on: {target_name} ({target_domain})")
    recon_data = {
        "Company Overview": f"{target_name} is a mid-sized tech firm specializing in cloud services.",
        "Tech Stack": ["Python", "AWS", "Docker", "React"],
        "Public Exposure": [
            "Careers page with open roles",
            "GitHub repos under org name",
            f"Subdomain: api.{target_domain}"
        ]
    }
    return recon_data

def save_output(data, target_name):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{output_dir}/recon_{target_name.lower()}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"\n[+] Recon data saved to {filename}")

if __name__ == "__main__":
    target_name = input("Enter target company name: ")
    target_domain = input("Enter target domain: ")
    results = simulate_recon(target_name, target_domain)

    print("\nRecon Summary:")
    for key, value in results.items():
        print(f"{key}: {value}")

    save_output(results, target_name)
