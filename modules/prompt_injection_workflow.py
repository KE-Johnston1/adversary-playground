# prompt_injection_workflow.py
"""
Prompt Injection Workflow (Batch Mode)
Runs multiple user scenarios through the injection simulator and sanitizer.
Auto-generates JSON and Markdown summaries for each scenario.
"""

import json
import os
from prompt_injection import simulate_injection
from prompt_sanitizer import sanitize_prompt
from markdown_writer import json_to_markdown

def run_workflow(scenario):
    print(f"[+] Running workflow for: {scenario}")

    # Simulate injection
    injection_result = simulate_injection(scenario)
    injected_prompt = injection_result.get("Injected Prompt", "")

    # Sanitize injected prompt
    sanitizer_result = sanitize_prompt(injected_prompt)

    # Combine results
    return {
        "Scenario": scenario,
        "Injection Simulation": injection_result,
        "Sanitization Result": sanitizer_result
    }

def save_output(data, scenario):
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{output_dir}/workflow_{scenario.lower().replace(' ', '_')}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"[+] Saved JSON: {filename}")

    # Auto-generate markdown
    json_to_markdown(filename)

if __name__ == "__main__":
    # Define batch scenarios
    scenarios = [
        "reset my password",
        "delete logs",
        "access admin panel",
        "disable security alerts",
        "check my email"
    ]

    for scenario in scenarios:
        print(f"\n=== Scenario: {scenario} ===")
        result = run_workflow(scenario)

        # Print summary to terminal
        print("\n--- Injection Simulation ---")
        for key, value in result["Injection Simulation"].items():
            if isinstance(value, list):
                for item in value:
                    print(f"  - {item}")
            else:
                print(f"{key}: {value}")

        print("\n--- Sanitization Result ---")
        for key, value in result["Sanitization Result"].items():
            if isinstance(value, list):
                for item in value:
                    print(f"  - {item}")
            else:
                print(f"{key}: {value}")

        # Save results
        save_output(result, scenario)
