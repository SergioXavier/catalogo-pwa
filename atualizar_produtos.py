import os
import json

# Caminhos
pasta_imagens = "/Users/sergioxavier/MeusProjetos/CatalogoPWA/wwwroot/imagens"
ficheiro_json = "/Users/sergioxavier/MeusProjetos/CatalogoPWA/wwwroot/produtos.json"

# Extensões de imagem aceites
extensoes = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif"}

produtos = []

# Percorrer os ficheiros da pasta
ficheiros = sorted(os.listdir(pasta_imagens))

for nome_ficheiro in ficheiros:
    caminho = os.path.join(pasta_imagens, nome_ficheiro)

    # Ignorar pastas
    if not os.path.isfile(caminho):
        continue

    # Separar nome e extensão
    nome_base, extensao = os.path.splitext(nome_ficheiro)

    # Verificar extensão
    if extensao.lower() not in extensoes:
        continue

    # Excluir imagens chamadas Logo, logo, LOGO, etc.
    if nome_base.lower() == "logo":
        continue

    # Criar nome do produto a partir do nome do ficheiro
    nome_produto = nome_base.replace("_", " ").replace("-", " ").strip()

    # Colocar a primeira letra de cada palavra em maiúscula
    nome_produto = nome_produto.title()

    produtos.append({
        "id": len(produtos) + 1,
        "nome": nome_produto,
        "imagem": f"imagens/{nome_ficheiro}"
    })

# Escrever o JSON
with open(ficheiro_json, "w", encoding="utf-8") as ficheiro:
    json.dump(produtos, ficheiro, ensure_ascii=False, indent=4)

print(f"{len(produtos)} produtos atualizados.")
print(f"JSON: {ficheiro_json}")