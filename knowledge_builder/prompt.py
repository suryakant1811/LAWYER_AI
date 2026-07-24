def get_markdown_prompt(text):

    return f"""
    You are an expert legal knowledge engineer.

Analyze this document.

Return ONLY valid JSON.

{{
    "category":"",
    "intent":"",
    "title":"",
    "markdown":""
}}

Rules:

Category must be one of

banking

cybercrime

police

consumer

employment

property

education

healthcare

government_services

Markdown must follow:

# Title

## Description

## Applicable Laws

## Immediate Actions

## Evidence

## Timeline

## Authority

## Official Sources

Return JSON only.

Return ONLY valid JSON.

Do NOT use markdown.

Do NOT use ```json.

Do NOT add any explanation.

Document:

{text}
"""