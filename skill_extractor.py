SKILL_DB = [
    # Programming
    "python", "java", "javascript", "c++", "c#", "r", "sql", "typescript",
    "go", "rust", "kotlin", "swift",
    # ML/AI
    "machine learning", "deep learning", "nlp", "computer vision",
    "tensorflow", "pytorch", "scikit-learn", "keras", "pandas", "numpy",
    # Web
    "react", "node.js", "django", "flask", "html", "css",
    "fastapi", "express", "vue.js", "angular",
    # Cloud/DevOps
    "aws", "azure", "gcp", "docker", "kubernetes", "git", "ci/cd",
    # Databases
    "mysql", "postgresql", "mongodb", "redis", "sqlite",
    # Other
    "excel", "power bi", "tableau", "linux", "agile", "rest api"
]

def extract_skills(text):
    text_lower = text.lower()
    found = []
    for skill in SKILL_DB:
        if skill in text_lower:
            found.append(skill.title())
    return list(set(found))