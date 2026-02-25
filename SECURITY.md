# 🛡️ Security Policy

## Supported Versions

| Version | Supported          |
|---------|--------------------|
| 1.x     | ✅ Active support  |
| < 1.0   | ❌ Not supported   |

## Reporting a Vulnerability

The Cliff-Pay team takes the security of this project seriously. If you discover a security vulnerability, we appreciate your help in disclosing it to us responsibly.

### How to Report

1. **Do NOT open a public GitHub issue.** Security vulnerabilities must be reported privately.
2. Send an email to the maintainer with the subject line: **[SECURITY] Cliff-Pay Vulnerability Report**
3. Include the following details in your report:
   - A clear description of the vulnerability
   - Steps to reproduce the issue
   - The potential impact of the vulnerability
   - Any suggested fixes (optional but appreciated)

### What to Expect

- **Acknowledgement:** You will receive a response within **48 hours** confirming receipt of your report.
- **Assessment:** The vulnerability will be evaluated and triaged within **5 business days**.
- **Resolution:** A fix will be developed and a patched release will be published. You will be credited (unless you prefer anonymity).

## Security Best Practices for Contributors

When contributing to Cliff-Pay, please adhere to the following:

- **Never commit secrets.** API keys, `SECRET_KEY`, database credentials, and tokens must never appear in source code. Use environment variables and `.env` files.
- **Use parameterized queries.** Django ORM handles this by default — avoid raw SQL unless absolutely necessary.
- **Validate all input.** Use DRF serializers for request validation. Never trust client-side data.
- **Keep dependencies updated.** Run `pip audit` or use tools like Dependabot to monitor for known vulnerabilities.
- **Use HTTPS in production.** Ensure all deployed instances enforce TLS/SSL.

## Scope

This policy applies to the Cliff-Pay codebase and its direct dependencies. Third-party services (e.g., PostgreSQL, hosting providers) have their own security policies.

---

Thank you for helping keep Cliff-Pay and its users safe. 🙏
