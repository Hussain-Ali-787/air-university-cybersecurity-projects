# Air University Cybersecurity Academic Projects - Folder Setup Script
# Run this script from inside your repository folder.

$ErrorActionPreference = "Stop"

$folders = @(
    "semester-01-fall-2023/applications-of-ict",
    "semester-01-fall-2023/discrete-structures",
    "semester-01-fall-2023/functional-english",
    "semester-01-fall-2023/introduction-to-cybersecurity",
    "semester-01-fall-2023/programming-fundamentals",

    "semester-02-spring-2024/applied-physics",
    "semester-02-spring-2024/digital-logic-design",
    "semester-02-spring-2024/introduction-to-software-engineering",
    "semester-02-spring-2024/linear-algebra",
    "semester-02-spring-2024/object-oriented-programming",

    "semester-03-fall-2024/calculus-and-analytical-geometry",
    "semester-03-fall-2024/computer-networks",
    "semester-03-fall-2024/computer-organization-and-assembly-language",
    "semester-03-fall-2024/data-structures",
    "semester-03-fall-2024/information-assurance",
    "semester-03-fall-2024/introduction-to-management",

    "semester-04-spring-2025/malware-analysis",
    "semester-04-spring-2025/multivariable-calculus",
    "semester-04-spring-2025/network-security",
    "semester-04-spring-2025/operating-systems",
    "semester-04-spring-2025/secure-software-design-and-development",

    "semester-05-summer-2025/internship",

    "semester-06-fall-2025/artificial-intelligence",
    "semester-06-fall-2025/civics-and-community-engagement",
    "semester-06-fall-2025/digital-forensics",
    "semester-06-fall-2025/ethical-hacking-and-defense",
    "semester-06-fall-2025/expository-writing",
    "semester-06-fall-2025/parallel-and-distributed-computing",

    "final-year-project/spot-smart-privacy-oversharing-tracker"
)

foreach ($folder in $folders) {
    New-Item -ItemType Directory -Force -Path $folder | Out-Null

    $readmePath = Join-Path $folder "README.md"
    if (!(Test-Path $readmePath)) {
        $courseTitle = ($folder.Split("/")[-1] -replace "-", " ")
        $courseTitle = (Get-Culture).TextInfo.ToTitleCase($courseTitle)

        @"
# $courseTitle

## Overview

This folder contains academic work completed for the **$courseTitle** course.

## Contents

- Assignments
- Labs
- Projects
- Reports
- Presentations
- Screenshots

## Status

Content will be added and improved over time.

## Ethical Notice

All cybersecurity-related work in this folder is intended strictly for academic learning, ethical research, and authorized testing only.
"@ | Set-Content -Path $readmePath -Encoding UTF8
    }
}

# Add useful empty subfolders inside course folders
foreach ($folder in $folders) {
    New-Item -ItemType Directory -Force -Path "$folder/assignments" | Out-Null
    New-Item -ItemType Directory -Force -Path "$folder/labs" | Out-Null
    New-Item -ItemType Directory -Force -Path "$folder/projects" | Out-Null
    New-Item -ItemType Directory -Force -Path "$folder/reports" | Out-Null
    New-Item -ItemType Directory -Force -Path "$folder/presentations" | Out-Null
    New-Item -ItemType Directory -Force -Path "$folder/screenshots" | Out-Null
}

Write-Host "Folder structure created successfully." -ForegroundColor Green
Write-Host "Next commands:" -ForegroundColor Yellow
Write-Host "git status"
Write-Host "git add ."
Write-Host 'git commit -m "Add semester and course folder structure"'
Write-Host "git push origin main"
