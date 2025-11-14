
snake_svg = "<img src='snake.svg' alt='GitHub Snake'>"

with open("README.md", "r") as f:
    readme_content = f.read()

if snake_svg not in readme_content:
    readme_content += "\n" + snake_svg

with open("README.md", "w") as f:
    f.write(readme_content)

with open("remade.md", "a") as f:
    f.write("\n<!-- profile update trigger -->")
