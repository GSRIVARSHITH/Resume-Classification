import re

PROJECT_HEADERS    = ["projects", "project experience", "academic projects", "personal projects"]
ACHIEVE_HEADERS    = ["achievements", "awards", "honors", "accomplishments", "certifications"]
EDUCATION_HEADERS  = ["education", "academic background", "qualifications"]
EXPERIENCE_HEADERS = ["experience", "work experience", "employment", "professional experience"]

def find_section(text, headers):
    lines = text.split('\n')
    section_lines = []
    capturing = False

    for line in lines:
        stripped = line.strip().lower()

        # Start capturing if header matches
        if any(h in stripped for h in headers):
            capturing = True
            continue

        # Stop if we hit another known section header
        if capturing:
            is_other_header = any(
                h in stripped
                for h in PROJECT_HEADERS + ACHIEVE_HEADERS + EDUCATION_HEADERS + EXPERIENCE_HEADERS
                if stripped and not any(h in stripped for h in headers)
            )
            if is_other_header and stripped:
                break
            if stripped:
                section_lines.append(line.strip())

    return section_lines

def extract_projects(text):
    return find_section(text, PROJECT_HEADERS)

def extract_achievements(text):
    return find_section(text, ACHIEVE_HEADERS)

def extract_education(text):
    return find_section(text, EDUCATION_HEADERS)

def extract_experience(text):
    return find_section(text, EXPERIENCE_HEADERS)