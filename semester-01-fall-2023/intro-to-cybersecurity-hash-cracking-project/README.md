# Hash Cracking Demonstration using John the Ripper

## Course

**Introduction to Cybersecurity**  
BS Cyber Security  
Air University Islamabad

## Project Type

Research Presentation and Live Tool Demonstration

## Overview

This project was completed as part of the Introduction to Cybersecurity course. The objective was to research, present, and demonstrate the use of a cybersecurity tool in a controlled academic environment. Our selected topic was **password hash cracking** using **John the Ripper** on Kali Linux.

The project explained the concept of password hashing, the role of wordlists in password recovery, and how tools such as John the Ripper and Johnny GUI can be used to test weak password security. A live demonstration was performed using a dummy password hash and a custom wordlist generated for educational purposes.

## Problem Statement

Passwords are commonly stored as hashes instead of plain text. Although hashing improves password storage security, weak passwords can still be recovered if attackers obtain password hashes and use dictionary, brute-force, or rule-based cracking techniques. This project demonstrates how weak password choices can be exploited and why strong password policies, salting, and secure hashing algorithms are necessary.

## Objectives

- Research the purpose and usage of John the Ripper.
- Explain how password hashes work.
- Demonstrate hash cracking using a dummy MD5 hash.
- Show the role of custom wordlists in password recovery.
- Present mitigation techniques against password cracking risks.
- Demonstrate Johnny as a graphical interface for John the Ripper.

## Tools and Technologies

- Kali Linux
- John the Ripper
- Johnny GUI
- CUPP wordlist generator
- MD5 hashing
- Linux terminal
- Custom wordlist

## Topics Covered

- Benefits of Kali Linux for cybersecurity learning
- Overview of John the Ripper
- Understanding hashed passwords
- Generating a password hash
- Creating a custom wordlist
- Executing John the Ripper
- Cracking ZIP and PDF password hashes conceptually
- Using Johnny GUI
- Mitigation against hash cracking risks

## Methodology

The project followed these steps:

1. Selected John the Ripper as the cybersecurity tool for demonstration.
2. Researched Kali Linux and John the Ripper.
3. Explained password hashing and why hashes are used.
4. Generated a dummy MD5 password hash.
5. Created a custom wordlist using CUPP.
6. Used John the Ripper to compare wordlist entries against the hash.
7. Demonstrated the cracked password output.
8. Explained Johnny GUI as an easier interface for beginners.
9. Presented mitigation strategies against hash cracking attacks.

## Demonstration Summary

The live demonstration used a controlled lab setup. A dummy password was converted into an MD5 hash and stored in a text file. A small custom wordlist was generated using CUPP. John the Ripper was then executed with the selected wordlist, hash format, and hash file. The tool matched the correct password from the wordlist and displayed the cracked password.

## Example Command Structure

```bash
john --wordlist=<wordlist-file> --format=<hash-format> <hash-file>
```

Example:

```bash
john --wordlist=jazib.txt --format=Raw-MD5 password1.txt
```

> Note: Commands are shown for academic understanding only and should only be used in authorized lab environments.

## Security Lessons Learned

- Weak passwords are vulnerable to dictionary and wordlist-based attacks.
- Hashing alone is not enough if passwords are weak.
- MD5 is outdated and should not be used for secure password storage.
- Salting makes precomputed attacks more difficult.
- Strong password policies reduce cracking success.
- Multi-factor authentication adds an additional layer of protection.
- Secure password storage should use modern password hashing algorithms such as bcrypt, scrypt, Argon2, or PBKDF2.

## Mitigation Techniques

- Use long and complex passwords.
- Avoid personal information in passwords.
- Use salted hashes.
- Avoid outdated hashing algorithms such as MD5 and SHA-1.
- Use adaptive password hashing algorithms.
- Enforce account lockout or rate limiting.
- Use multi-factor authentication.
- Monitor for leaked password hashes.
- Educate users about password security.

## Repository Structure

```text
hash-cracking-john-the-ripper/
│
├── README.md
├── presentation/
│   └── CYS Project (Light).pptx
├── docs/
├── screenshots/
└── demo-notes/
```

## Ethical Notice

This project is intended strictly for academic learning, ethical research, and authorized cybersecurity lab demonstrations. It must not be used to crack passwords, access accounts, or test systems without explicit permission.

## Disclaimer

The demonstration was performed using dummy data in a controlled educational environment. No real user credentials, systems, or accounts were targeted.
