import re
import link
import language

def main():
    # -- INPUT --
    field = input("Paste email text:\n")

    # -- LINK EXTRACTION --
    full_url_pattern = r'https?://[^\s]+'
    domain_pattern = r'\b(?:www\.)?([a-zA-Z0-9-]+\.[a-zA-Z]{2,})\b'

    full_urls = re.findall(full_url_pattern, field)

    if full_urls:
        links = full_urls
    else:
        raw_domains = re.findall(domain_pattern, field)
        links = ["http://" + d for d in raw_domains]

    # -- SAVE LINKS --
    with open("link.txt", "w") as f:
        for ink in links:
            f.write(ink + "\n")

    # -- ANALYSIS --
    try:
        language_score = language.language_risk_score(field)
        link_results = link.analyze_links(links)
    except Exception as e:
        print(f"Error during analysis: {e}")
        return

    # -- FINAL REPORT --
    total_link_score = sum(item["risk_score"] for item in link_results)
    total_score = language_score + total_link_score

    print("\n--- PHISHING ANALYSIS REPORT ---")
    print(f"Language risk score: {language_score}")
    print(f"Total link risk score: {total_link_score}")
    print(f"OVERALL RISK SCORE: {total_score}\n")

    for item in link_results:
        print(f"Link: {item['url']}")
        print(f"Domain: {item['domain']}")
        print(f"Link risk score: {item['risk_score']}\n")

    if total_score >= 70:
        print("HIGH RISK — Likely phishing email")
    elif total_score >= 40:
        print("MEDIUM RISK — Suspicious content detected")
    else:
        print("LOW RISK — No strong phishing indicators")


if __name__ == "__main__":
    main()
