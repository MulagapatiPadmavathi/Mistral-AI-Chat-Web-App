def format_respose(response_text):
    """Formats response with bullet points or number lists."""
    lines = response_text.split("\n")
    formatted_lines = []

    for line in lines:
        if line.strip():
            if line.startswith("-") or line.startswith("*"):
                formatted_lines.append(f". {line[1:].strip()}")
            elif line[0].isdigit() and line[1] == ".":
                formatted_lines.append(f"➡️ {line}")
            else:
                formatted_lines.append(line)
                
    return "\n".join(formatted_lines)