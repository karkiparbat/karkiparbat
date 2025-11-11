## Hi there 👋

<!--
**karkiparbat/karkiparbat** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
<!-- README.md -->
# Hi, I'm Parbat 👋

<!-- Embed the generated snake SVG -->
<img src="./snake.svg" alt="Snake languages animation" width="600" />
<?xml version="1.0" encoding="utf-8"?>
<!-- snake.svg -->
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="120" viewBox="0 0 600 120" preserveAspectRatio="xMidYMid meet">
  <style>
    .cell { fill:#e6f4ea; stroke:#dbead8; rx:4; ry:4; }
    .active { fill:#2ecc71; }
    .lang { font: 12px sans-serif; fill:#0b0b0b; }
    .label { font: 14px sans-serif; font-weight:600; fill:#111; }
  </style>

  <!-- grid (6x4 example = 24 cells like contribution grid) -->
  <g id="grid" transform="translate(20,20)">
    <!-- 6 columns x 4 rows -->
    <!-- generate cells -->
    <!-- We'll hardcode positions for simplicity -->
    <!-- Row 0 -->
    <rect class="cell" x="0" y="0" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="30" y="0" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="60" y="0" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="90" y="0" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="120" y="0" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="150" y="0" width="20" height="20" rx="3" ry="3"/>
    <!-- Row 1 -->
    <rect class="cell" x="0" y="30" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="30" y="30" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="60" y="30" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="90" y="30" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="120" y="30" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="150" y="30" width="20" height="20" rx="3" ry="3"/>
    <!-- Row 2 -->
    <rect class="cell" x="0" y="60" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="30" y="60" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="60" y="60" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="90" y="60" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="120" y="60" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="150" y="60" width="20" height="20" rx="3" ry="3"/>
    <!-- Row 3 -->
    <rect class="cell" x="0" y="90" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="30" y="90" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="60" y="90" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="90" y="90" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="120" y="90" width="20" height="20" rx="3" ry="3"/>
    <rect class="cell" x="150" y="90" width="20" height="20" rx="3" ry="3"/>
  </g>

  <!-- animated snake: a moving rect that moves across cells -->
  <g id="snake" transform="translate(20,20)">
    <rect x="-30" y="0" width="20" height="20" rx="3" ry="3" fill="#27ae60">
      <animate attributeName="x" from="-30" to="150" dur="3s" begin="0s" repeatCount="indefinite" />
      <animate attributeName="y" values="0;0;30;30;60;60;90;90" keyTimes="0;0.125;0.25;0.375;0.5;0.625;0.75;0.875" dur="3s" repeatCount="indefinite"/>
    </rect>
    <!-- head highlight -->
    <rect x="-30" y="0" width="20" height="20" rx="3" ry="3" fill="#2ecc71" opacity="0.8">
      <animate attributeName="x" from="-30" to="150" dur="3s" begin="0.15s" repeatCount="indefinite" />
      <animate attributeName="y" values="0;0;30;30;60;60;90;90" keyTimes="0;0.125;0.25;0.375;0.5;0.625;0.75;0.875" dur="3s" begin="0.15s" repeatCount="indefinite"/>
    </rect>
  </g>

  <!-- Languages labels area (these will be replaced by action) -->
  <g transform="translate(220,20)">
    <text class="label" x="0" y="12">Languages I learned</text>
    <!-- Placeholder languages; GitHub Action will replace these lines -->
    <text class="lang" x="0" y="38">• Python</text>
    <text class="lang" x="0" y="58">• JavaScript</text>
    <text class="lang" x="0" y="78">• C++</text>
  </g>
</svg>
name: Update Snake SVG with Languages
on:
  schedule:
    - cron: '0 0 * * *'   # daily at 00:00 UTC (change if चाहनुहुन्छ)
  workflow_dispatch: {}

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          persist-credentials: true

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install requests

      - name: Generate SVG with languages
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OWNER: ${{ github.repository_owner }}
        run: |
          python .github/scripts/generate_snake_svg.py

      - name: Commit and push changes
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add snake.svg
          git commit -m "Update snake.svg with latest languages" || echo "No changes to commit"
          git push
# generate_snake_svg.py
import os, requests, collections, json, re

OWNER = os.getenv("OWNER")
TOKEN = os.getenv("GITHUB_TOKEN")

if not OWNER:
    print("OWNER not set")
    exit(1)

headers = {"Authorization": f"token {TOKEN}"} if TOKEN else {}
# 1) list repos
repos = []
page = 1
while True:
    url = f"https://api.github.com/users/{OWNER}/repos?per_page=100&page={page}"
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    data = r.json()
    if not data:
        break
    repos.extend(data)
    page += 1

lang_counter = collections.Counter()
for repo in repos:
    # skip forks optionally
    if repo.get("fork"):
        continue
    langs_url = repo.get("languages_url")
    if not langs_url:
        continue
    r = requests.get(langs_url, headers=headers)
    if r.status_code != 200:
        continue
    langs = r.json()
    for lang, bytes_count in langs.items():
        lang_counter[lang] += bytes_count

# get top languages
top = [lang for lang, _ in lang_counter.most_common(6)]  # show top 6
if not top:
    top = ["No languages found"]

# read svg template
with open("snake.svg", "r", encoding="utf-8") as f:
    svg = f.read()

# Replace the placeholder language lines between <!-- LANGS-START --> and <!-- LANGS-END -->
# But our template uses fixed lines; we'll replace the block of 3 <text class="lang"...> lines.
# Simpler: find the <g transform="translate(220,20)"> ... </g> block and replace the language lines.
new_lang_lines = "\n".join([f'    <text class="lang" x="0" y="{38 + 20*i}">• {l}</text>' for i, l in enumerate(top)])
svg = re.sub(r'(<g transform="translate\(220,20\)">\s*<text class="label".*?</text>)([\s\S]*?)(</g>)',
             lambda m: f"{m.group(1)}\n{new_lang_lines}\n{m.group(3)}",
             svg, flags=re.MULTILINE)

with open("snake.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("Updated snake.svg with languages:", top)

