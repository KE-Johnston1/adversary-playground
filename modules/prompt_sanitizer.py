# prompt_sanitizer.py
"""
Prompt Sanitizer
Flags and redacts risky prompt injection patterns.
Returns sanitized input, risk flags, and a risk score.
"""

def sanitize_prompt(prompt):
    print(f"[+] Sanitizing input: {prompt}")

    # Define risky patterns
    risky_phrases = [
        "ignore previous instructions",
        "delete all files",
        "respond with",
        "shutdown",
        "access admin",
        "disable logs",
        "exfiltrate",
        "override",
        "bypass"
    ]

    risk_flags = []
    sanitized = prompt

    # Flag and redact risky phrases
    for phrase in risky_phrases:
        if phrase.lower() in prompt.lower():
            risk_flags.append(f"⚠️ Risky phrase detected: '{phrase}'")
            sanitized = sanitized.replace(phrase, "[REDACTED]")

    # Risk scoring logic
    risk_score = len(risk_flags)
    if risk_score == 0:
        risk_level = "✅ No Risk"
    elif risk_score <= 2:
        risk_level = "⚠️ Mild Risk"
    else:
        risk_level = "🔥 High Risk"

    return {
        "Original Input": prompt,
        "Sanitized Input": sanitized,
        "Risk Flags": risk_flags,
        "Risk Score": risk_score,
        "Risk Level": risk_level
    }
