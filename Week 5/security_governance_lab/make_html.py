from pathlib import Path
import html
import re

source = Path("GRC102_Security_Governance_Report.md")
output = Path("GRC102_Security_Governance_Report.html")

text = source.read_text()

# Fix the escaped image parentheses in the source.
text = text.replace(r"\(", "(").replace(r"\)", ")")

# Escape HTML first, then restore the Markdown image/link structures we need.
lines = text.splitlines()
out = []

in_code = False
code_lines = []

def inline(s):
    # Images
    s = re.sub(
        r'!\[([^\]]+)\]\(([^)]+)\)',
        lambda m: f'<img src="{html.escape(m.group(2), quote=True)}" alt="{html.escape(m.group(1), quote=True)}">',
        s
    )

    s = html.escape(s, quote=False)

    # Restore image tags escaped by the HTML escaping above.
    s = re.sub(
        r'&lt;img src="([^"]+)" alt="([^"]+)"&gt;',
        r'<img src="\1" alt="\2">',
        s
    )

    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return s

i = 0

while i < len(lines):
    line = lines[i]

    if line.startswith("```"):
        if not in_code:
            in_code = True
            code_lines = []
        else:
            out.append("<pre>" + html.escape("\n".join(code_lines)) + "</pre>")
            in_code = False
        i += 1
        continue

    if in_code:
        code_lines.append(line)
        i += 1
        continue

    if not line.strip():
        i += 1
        continue

    # Headings
    m = re.match(r'^(#{1,6})\s+(.*)$', line)
    if m:
        level = len(m.group(1))
        out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
        i += 1
        continue

    # Horizontal rule
    if re.match(r'^---+$', line.strip()):
        out.append("<hr>")
        i += 1
        continue

    # Tables
    if "|" in line and i + 1 < len(lines) and "|" in lines[i + 1]:
        table_lines = []
        while i < len(lines) and "|" in lines[i]:
            table_lines.append(lines[i])
            i += 1

        if len(table_lines) >= 2:
            headers = [x.strip() for x in table_lines[0].strip("|").split("|")]
            rows = []

            for row in table_lines[2:]:
                cells = [x.strip() for x in row.strip("|").split("|")]
                if cells:
                    rows.append(cells)

            out.append("<table>")
            out.append("<thead><tr>")
            for h in headers:
                out.append(f"<th>{inline(h)}</th>")
            out.append("</tr></thead><tbody>")

            for row in rows:
                out.append("<tr>")
                for cell in row:
                    out.append(f"<td>{inline(cell)}</td>")
                out.append("</tr>")

            out.append("</tbody></table>")
        continue

    # Numbered lists
    if re.match(r'^\d+\.\s+', line):
        items = []
        while i < len(lines) and re.match(r'^\d+\.\s+', lines[i]):
            items.append(re.sub(r'^\d+\.\s+', '', lines[i]))
            i += 1

        out.append("<ol>")
        for item in items:
            out.append(f"<li>{inline(item)}</li>")
        out.append("</ol>")
        continue

    # Bullet lists
    if re.match(r'^[-*]\s+', line):
        items = []
        while i < len(lines) and re.match(r'^[-*]\s+', lines[i]):
            items.append(re.sub(r'^[-*]\s+', '', lines[i]))
            i += 1

        out.append("<ul>")
        for item in items:
            out.append(f"<li>{inline(item)}</li>")
        out.append("</ul>")
        continue

    # Normal paragraph
    out.append(f"<p>{inline(line)}</p>")
    i += 1

html_doc = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>GRC102 Security Governance Simulation</title>
<style>
@page {
    size: A4;
    margin: 18mm;
}

body {
    font-family: Arial, Helvetica, sans-serif;
    max-width: 900px;
    margin: 0 auto;
    color: #222;
    line-height: 1.55;
    font-size: 11pt;
}

h1 {
    font-size: 26pt;
    margin-top: 0;
    padding-bottom: 10px;
    border-bottom: 2px solid #222;
}

h2 {
    font-size: 20pt;
    margin-top: 34px;
    border-bottom: 1px solid #ccc;
    padding-bottom: 5px;
}

h3 {
    font-size: 15pt;
    margin-top: 25px;
}

p {
    margin: 9px 0;
}

img {
    max-width: 92%;
    height: auto;
    display: block;
    margin: 18px auto;
    page-break-inside: avoid;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 18px 0;
    font-size: 9.5pt;
}

th, td {
    border: 1px solid #bbb;
    padding: 7px;
    vertical-align: top;
}

th {
    background: #eeeeee;
}

code {
    font-family: Menlo, Monaco, monospace;
    background: #f1f1f1;
    padding: 2px 4px;
    border-radius: 3px;
}

pre {
    background: #f5f5f5;
    padding: 12px;
    border: 1px solid #ddd;
    overflow-wrap: break-word;
    white-space: pre-wrap;
    font-size: 9pt;
}

hr {
    border: 0;
    border-top: 1px solid #ccc;
    margin: 30px 0;
}

li {
    margin-bottom: 5px;
}

@media print {
    h1, h2, h3 {
        page-break-after: avoid;
    }

    img {
        page-break-inside: avoid;
    }

    table {
        page-break-inside: avoid;
    }
}
</style>
</head>
<body>
""" + "\n".join(out) + """
</body>
</html>
"""

output.write_text(html_doc)
print(f"Created {output}")
