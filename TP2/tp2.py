import re

def converte_cabeçalho(markdown):
    markdown = re.sub(r'^#\s+(.+)$', r'<h1>\1</h1>', markdown, flags=re.MULTILINE) #titulo
    markdown = re.sub(r'^##\s+(.+)$', r'<h2>\1</h2>', markdown, flags=re.MULTILINE) #sub-titulo
    markdown = re.sub(r'^###\s+(.+)$', r'<h3>\1</h3>', markdown, flags=re.MULTILINE) #sub sub-titulo
    return markdown

def converte_negrito(markdown):
    markdown = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown)
    return markdown

def converte_italico(markdown):
    markdown = re.sub(r'\*(.*?)\*', r'<i>\1</i>', markdown)
    return markdown

def converte_listas(markdown):
    markdown = re.sub(r'^(\d+)\.\s+(.+)$', r'<li>\2</li>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'(?<=<\/li>)\n(?=\d+\.)', '', markdown)
    markdown = re.sub(r'^(\d+)\.\s+(.+)$', r'<ol>\n\1.', markdown, count=1, flags=re.MULTILINE) + '</ol>'
    return markdown

def converte_links_e_imagens(markdown):
    markdown = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', markdown) #Imagens
    markdown = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', markdown) #Links
    return markdown

def markdown_to_html(markdown):
    markdown = converte_cabeçalho(markdown)
    markdown = converte_negrito(markdown)
    markdown = converte_italico(markdown)
    markdown = converte_listas(markdown)
    markdown = converte_links_e_imagens(markdown)
    return markdown

def le_ficheiro_markdown(caminho):
    with open(caminho, 'r', encoding='utf-8') as file:
        return file.read()

def escreve_ficheiro_html(conteudo_html, caminho):
    with open(caminho, 'w', encoding='utf-8') as file:
        file.write(conteudo_html)

caminho_input= 'input.md'
caminho_output= 'output.html'

markdown_input = le_ficheiro_markdown(caminho_input)
html_output = markdown_to_html(markdown_input)
escreve_ficheiro_html(html_output, caminho_output)

print(f"O HTML foi salvo em '{caminho_output}' com sucesso.")
