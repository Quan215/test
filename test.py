with open("test.txt", "r", encoding="utf8") as markdown:
    markdownContent = markdown.read()
with open("test.txt", "w", encoding="utf-8") as markdown:
    markdown.write(f"{markdownContent}1{markdownContent}")
