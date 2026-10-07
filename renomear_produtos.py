import os
import shutil # Importar o módulo de cópia
from PIL import Image
import pytesseract


# Definir explicitamente o caminho do Tesseract no Mac (caso use o Homebrew padrão):
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract' 
# Nota: Se o seu Mac for mais antigo com processador Intel, o caminho costuma ser '/usr/local/bin/tesseract'

PASTA_ORIGEM = "/Users/sergioxavier/MeusProjetos/CatalogoPWA/wwwroot/imagens"
PASTA_DESTINO = "/Users/sergioxavier/MeusProjetos/CatalogoPWA/wwwroot/imagens"

# Criar a pasta de destino se não existir
os.makedirs(PASTA_DESTINO, exist_ok=True)

def copiar_e_renomear_produtos():
    for ficheiro in os.listdir(PASTA_ORIGEM):
        if ficheiro.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            caminho_original = os.path.join(PASTA_ORIGEM, ficheiro)
            
            try:
                img = Image.open(caminho_original)
                texto_extraido = pytesseract.image_to_string(img, lang='por')
                linhas = [linha.strip() for linha in texto_extraido.split('\n') if linha.strip()]
                
                if linhas:
                    novo_nome_base = " ".join(linhas[:2])
                    
                    carateres_proibidos = '<>:"/\\|?*'
                    for c in carateres_proibidos:
                        novo_nome_base = novo_nome_base.replace(c, '')
                        
                    novo_nome_base = novo_nome_base[:50].strip()
                    extensao = os.path.splitext(ficheiro)[1]
                    novo_nome_ficheiro = f"{novo_nome_base}{extensao}"
                    
                    caminho_destino = os.path.join(PASTA_DESTINO, novo_nome_ficheiro)
                    
                    # EM VEZ DE RENOMEAR, FAZEMOS UMA CÓPIA:
                    shutil.copy(caminho_original, caminho_destino)
                    print(f"Copiado e renomeado: '{ficheiro}' -> '{novo_nome_ficheiro}'")
                    
            except Exception as e:
                print(f"Erro ao processar o ficheiro {ficheiro}: {e}")

if __name__ == "__main__":
    copiar_e_renomear_produtos()