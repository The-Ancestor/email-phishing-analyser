Email Phishing Analyser

A lightweight Python-based phishing detection tool that analyzes email text and embedded links to identify potential phishing attempts using rule-based heuristics.

-- Features --
-- Language Analysis --
Detects suspicious grammar patterns
Identifies excessive punctuation (e.g., !!!, ???)
Flags unusual capitalization
Detects urgency-based wording (e.g., "verify now", "urgent")
-- Link Analysis --
Detects insecure protocols (http)
Flags suspicious file extensions (.exe, .zip, etc.)
Identifies suspicious subdomains
Detects brand impersonation (e.g., paypal-login.xyz)
Extracts and analyzes domains

-- Risk Scoring System --

Combines language + link risks
Outputs:
LOW RISK
MEDIUM RISK
HIGH RISK

-- Installation --
Clone the repository:
git clone https://github.com/your-username/phishing-detector.git
cd phishing-detector

-- Usage--

Run the main script:

python analyser.py

Paste the email text when prompted:

Paste email text:
