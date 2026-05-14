# Safe Upload Checklist for Cybersecurity Projects

Use this checklist before uploading any project to GitHub.

## Remove Secrets

- [ ] `.env` files removed
- [ ] API keys removed
- [ ] Passwords removed
- [ ] Tokens removed
- [ ] Private keys removed
- [ ] Database credentials removed

## Remove Private Information

- [ ] University portal screenshots removed or sanitized
- [ ] Other students' names removed if not required
- [ ] Personal emails/phone numbers removed
- [ ] Real user data removed
- [ ] Client/company data removed

## Review Cybersecurity Content

- [ ] No live malware binaries
- [ ] No real exploit targets
- [ ] No unauthorized credentials
- [ ] No harmful payloads
- [ ] No sensitive packet captures
- [ ] No private forensic images or memory dumps

## Keep Safe Alternatives

Recommended to upload:

- [ ] Reports
- [ ] Screenshots
- [ ] Sanitized code
- [ ] Lab-only examples
- [ ] Architecture diagrams
- [ ] Defensive explanations
- [ ] Setup instructions
- [ ] Ethical notice

## Final Git Check

Run before commit:

```bash
git status
git diff --cached
```

Then commit only after reviewing the files.
