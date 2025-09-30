# phishing_payload.py
"""
Phishing Payload Generator
Simulates attacker-crafted phishing emails or login pages using AI-style logic.
For ethical red team simulation and defender training only.
"""

import json
import os

def generate_payload(target_role, target_company):
    print(f"[+] Crafting phishing payload for: {target_role} at {target_company}")
    
    payload = {
        "Email Subject": f"Urgent: Account Verification Required - {target_company}",
        "Email Body": f"""
        Dear {target_role},

        We detected unusual activity on your {target_company} account. Please verify your credentials immediately to avoid suspension.

        [Verify Now] - Link to fake login page

        Regards,
        {target_company} Security Team
        """,
        "Fake Login URL": f"https://{target_company.lower()}-secure-login.com"
    }

    return payload

def save_output(data, target_role, target_company):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{output_dir}/phish_{target_company.lower()}_{target_role.lower().replace(' ', '_')}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"[+] Payload saved to {filename}")

if __name__ == "__main__":
    target_role = input("Enter target role (e.g., HR Manager): ")
    target_company = input("Enter target company name: ")
    result = generate_payload(target_role, target_company)

    print("\nPhishing Payload:")
    for key, value in result.items():
        print(f"{key}:\n{value}\n")

    save_output(result, target_role, target_company)

# Save output to file
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
filename = f"{output_dir}/prompt_injection_{scenario.lower().replace(' ', '_')}.json"

with open(filename, "w") as f:
    json.dump(result, f, indent=4)

print(f"[+] Injection simulation saved to {filename}")
