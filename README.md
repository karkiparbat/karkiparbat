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
<h1 align="center">👋 Hi, I'm Parbat Karki</h1>
<h3 align="center">A passionate developer & entrepreneur from Pokhara, Nepal 🇳🇵</h3>

---

### 💫 About Me  
- 🔭 I’m currently working on "visual studio code"
- 🌱 I’m learning **html,  CSS, javascript, and python**  
- 💬 Ask me about **Dropshipping, Web Development, or Business Ideas**  
- ⚡ Fun fact: I love creating online businesses and designing digital products  

📧 **Reach me at:** [karkiparbat048@gmail.com](mailto:karkiparbat048@gmail.com)  
🌐 **Connect with me:** [LinkedIn](https://linkedin.com/in/karkiparbat) | [Portfolio](https://karkiparbat.github.io)

---

### 🛠️ Languages & Tools  
<p align="center">
  <img src="https://skillicons.dev/icons?i=html,css,js,react,nodejs,express,mongodb,tailwind,git,github,vscode,figma,python" />
</p>

---

### 📊 GitHub Stats  

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=karkiparbat&show_icons=true&theme=tokyonight&hide_border=true" alt="GitHub Stats" />
  <img src="https://streak-stats.demolab.com?user=karkiparbat&theme=tokyonight&hide_border=true" alt="GitHub Streak" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=karkiparbat&layout=compact&theme=tokyonight&hide_border=true" alt="Top Languages" />
</p>

---

name: 🐍 Generate Real GitHub Contribution Snake


on:
schedule:
- cron: '0 * * * *' # Runs every hour
workflow_dispatch:


jobs:
build:
runs-on: ubuntu-latest


steps:
- name: Checkout repository
uses: actions/checkout@v3


- name: Set up Python
uses: actions/setup-python@v4
with:
python-version: '3.x'


- name: Install dependencies
run: |
python -m pip install --upgrade pip
pip install matplotlib numpy requests pillow


- name: Generate Real Contribution Snake
env:
GITHUB_USER: ${{ github.repository_owner }}
run: |
python .github/scripts/generate_snake_svg.py


- name: Commit and Push SVG
run: |
git config --local user.email "github-actions[bot]@users.noreply.github.com"
git config --local user.name "github-actions[bot]"
git add output/github-contribution-grid-snake.svg
git commit -m "🐍 Update real contribution snake" || echo "No changes to commit"
git push
Generate an animated GitHub contribution snake based on real user contribution data.
html = requests.get(url).text


# Extract contribution data from the SVG structure
import re
pattern = re.compile(r'<rect .*?data-date="(.*?)".*?data-level="(\d)".*?>')
data = pattern.findall(html)


# Create grid layout (by week columns and weekday rows)
weeks = {}
for date_str, level in data:
date = datetime.strptime(date_str, "%Y-%m-%d")
week = date.isocalendar()[1]
weekday = date.weekday()
if week not in weeks:
weeks[week] = {}
weeks[week][weekday] = int(level)


# Convert into ordered columns
weeks_sorted = sorted(weeks.keys())
COLS = len(weeks_sorted)
ROWS = 7
CELL, GAP, MARGIN = 12, 3, 6
SVG_W = MARGIN*2 + COLS*CELL + (COLS-1)*GAP
SVG_H = MARGIN*2 + ROWS*CELL + (ROWS-1)*GAP


COLORS = ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]


def E(tag, **attrs):
el = Element(tag)
for k, v in attrs.items():
el.set(k, str(v))
return el


svg = E('svg', xmlns='http://www.w3.org/2000/svg', version='1.1', width=str(SVG_W), height=str(SVG_H), viewBox=f"0 0 {SVG_W} {SVG_H}")
SubElement(svg, 'rect', x='0', y='0', width=str(SVG_W), height=str(SVG_H), fill='white')


grid = SubElement(svg, 'g', id='grid')
centers = []
for ci, week in enumerate(weeks_sorted):
for ri in range(ROWS):
x = MARGIN + ci*(CELL+GAP)
y = MARGIN + ri*(CELL+GAP)
val = weeks[week].get(ri, 0)
color = COLORS[val]
SubElement(grid, 'rect', x=str(x), y=str(y), width=str(CELL), height=str(CELL), rx='2', ry='2', fill=color)
centers.append((x+CELL/2, y+CELL/2))


# === SNAKE PATH === #
path_d = ' '.join([('M' if i == 0 else 'L') + f"{x:.1f},{y:.1f}" for i, (x, y) in enumerate(centers)])
path_id = 'snakePath'
SubElement(svg, 'path', id=path_id, d=path_d, fill='none', stroke='none')


# === SNAKE === #
snake = SubElement(svg, 'g', id='snake')
SubElement(snake, 'circle', cx='0', cy='0', r='6', fill='#ff9933', stroke='#cc5500', stroke_width='1.2')
anim = SubElement(snake, 'animateMotion', dur='12s', repeatCount='indefinite')
SubElement(anim, 'mpath', href=f'#{path_id}')
SubElement(snake, 'animateTransform', attributeName='transform', attributeType='XML', type='scale', values='1;1.1;1', dur='1.5s', repeatCount='indefinite')


SubElement(svg, 'text', x=str(MARGIN), y=str(SVG_H - 5), font_size='9', fill='#555').text = f'🐍 Real Contributions: {USER}'


with open(OUT_FILE, 'wb') as f:
f.write(tostring(svg, encoding='utf-8'))


print(f"✅ Real contribution snake SVG generated for {USER}: {OUT_FILE}")
