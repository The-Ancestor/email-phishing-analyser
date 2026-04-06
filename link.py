from config import BRANDS, SUSPICIOUS_TLDS
from urllib.parse import urlparse
import re


def extract_domain(url):
    if not url.startswith("http"):
        url = "http://" + url
    return urlparse(url).netloc.lower()


def protocol_risk(url):
    if url.startswith("https://"):
        return 0
    elif url.startswith("http://"):
        return 35
    return 10


def tld_risk(url):
    for tld in SUSPICIOUS_TLDS:
        if url.lower().endswith(tld):
            return 40
    return 0


def double_extension_risk(url):
    if re.search(r"\.(exe|zip|scr|rar|js)(\?|$)", url.lower()):
        return 40
    return 0


def subdomain_risk(domain):
    if len(domain.split(".")) > 3:
        return 20
    return 0


def brand_risk(domain):
    for brand in BRANDS:
        if brand in domain and not domain.startswith(brand):
            return 30
    return 0


def obfuscation_risk(url):
    if "@" in url:
        return 40
    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        return 30
    return 0


def analyze_link(url):
    domain = extract_domain(url)
    score = 0

    score += protocol_risk(url)
    score += tld_risk(url)
    score += double_extension_risk(url)
    score += subdomain_risk(domain)
    score += brand_risk(domain)
    score += obfuscation_risk(url)

    return score, domain


def analyze_links(links):
    results = []
    for ink in links:
        score, domain = analyze_link(ink)
        results.append({
            "url": ink,
            "domain": domain,
            "risk_score": score
        })
    return results
