with open("text.txt", "r", encoding="utf8") as markdown:
    markdownContent = markdown.read()
    print(markdownContent)
with open("text.txt", "w", encoding="utf-8") as markdown:
    markdown.write(f"{markdownContent}1{markdownContent}")
    print(f"{markdownContent}1{markdownContent}")
