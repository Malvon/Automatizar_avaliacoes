import time
import random
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ================= MENSAGENS =================
respostas_aleatorias = [
    """Agradecemos muito sua avaliação! Espero que o produto corresponda às suas expectativas. Aproveite bastante sua compra, foi uma excelente escolha!

Obrigado pela preferência! Conte sempre com a TerabyteShop, seguimos à disposição para o que precisar.

Atenciosamente,
Equipe TerabyteShop""",

    """Sua avaliação é muito importante e somos muitos gratos pelo feedback!
Ficamos felizes que o item adquirido tenha sido uma excelente escolha. Que ele lhe proporcione uma ótima experiência!

Obrigado pela preferência! Conte sempre com a TerabyteShop, seguimos à disposição para o que precisar.

Atenciosamente,
Equipe TerabyteShop""",

    """Agradecemos imensamente seu feedback positivo.
Que bom saber que o item atendeu ao que você esperava. Que você aproveite ao máximo sua nova aquisição!

Obrigado pela preferência! Conte sempre com a TerabyteShop, seguimos à disposição para o que precisar.

Atenciosamente,
Equipe TerabyteShop""",

    """Agradecemos muito sua avaliação!

Que bom que o produto chegou como o esperado. Aproveite bastante sua compra, foi uma excelente escolha!
Obrigado pela preferência! Conte sempre com a TerabyteShop, seguimos à disposição para o que precisar.

Atenciosamente,
Equipe TerabyteShop"""
]

# ================= INICIALIZAÇÃO =================
chrome_options = Options()
chrome_options.add_experimental_option("detach", True) 
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://seller.shopee.com.br/portal/rating")

wait = WebDriverWait(driver, 10)

print("=====================================================")
print("  ROBÔ SHOPEE - SOMENTE RESPOSTAS (SEM EXCEL)")
print("=====================================================")
print("1. Faça login e use o filtro 'Não Respondidas'.")
input("2. Pressione ENTER aqui para começar a responder...")

print("\nIniciando automação...")
indice_pulo = 0

while True:
    try:
        # Pausa para atualizar a lista visualmente
        time.sleep(2.5) 

        # 1. Encontrar botões visíveis na tela
        botoes = driver.find_elements(By.XPATH, "//button[contains(., 'Responder')] | //span[contains(text(), 'Responder')]/ancestor::button")
        botoes = [b for b in botoes if b.is_displayed()]
        
        qtd_total = len(botoes)
        
        # Se o índice de pulo for maior que a quantidade de botões, acabou a página
        if qtd_total <= indice_pulo:
            print(f"\n>>> Fim dos itens processáveis na tela atual.")
            break 

        print(f"Fila: {qtd_total} | Ignorando os primeiros {indice_pulo} (Erros anteriores)")

        # Seleciona o botão da vez
        botao_atual = botoes[indice_pulo]
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao_atual)
        
        # --- APENAS PARA VISUALIZAÇÃO NO CONSOLE (Identifica quem é) ---
        nome_cliente = "Desconhecido"
        data_avaliacao = "--/--"
        try:
            container = botao_atual.find_element(By.XPATH, "./ancestor::div[contains(@class, 'shopee-product-rating__main-area')] | ./ancestor::div[5]")
            texto_completo = container.text
            
            # Tenta pegar nome
            linhas = texto_completo.split('\n')
            if linhas: nome_cliente = linhas[0]
            
            # Tenta pegar data (apenas para você ver no console)
            match_data = re.search(r'(\d{2}/\d{2}/\d{4})', texto_completo)
            if match_data: data_avaliacao = match_data.group(1)
        except:
            pass

        # Escolhe a mensagem
        msg_escolhida = random.choice(respostas_aleatorias)

        # 2. Executa a Resposta
        try:
            # Clica no botão Responder
            driver.execute_script("arguments[0].click();", botao_atual)
            
            # Espera a caixa de texto aparecer (Espera inteligente)
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
            
            # Localiza a textarea visível (do modal aberto)
            textareas = driver.find_elements(By.TAG_NAME, "textarea")
            caixa_texto = next((t for t in textareas if t.is_displayed()), None)
            
            if caixa_texto:
                caixa_texto.click()
                caixa_texto.send_keys(msg_escolhida)
                time.sleep(0.5)

                # Busca botão Enviar
                botoes_enviar = driver.find_elements(By.XPATH, "//button[contains(., 'Enviar')]")
                botao_enviar_final = next((b for b in botoes_enviar if b.is_displayed()), None)
                
                if botao_enviar_final:
                    driver.execute_script("arguments[0].click();", botao_enviar_final)
                    
                    # Feedback no Console
                    print(f" -> ✅ RESPONDIDO: {nome_cliente} ({data_avaliacao})")
                    
                    # Pausa para a Shopee processar e remover o item da lista
                    time.sleep(4) 
                else:
                    raise Exception("Botão Enviar sumiu")
            else:
                raise Exception("Caixa de texto não apareceu")

        except Exception as e_processo:
            print(f" -> ❌ Falha neste item. Pulando para o próximo...")
            webdriver.ActionChains(driver).send_keys(u'\ue00c').perform() # Aperta ESC por segurança
            indice_pulo += 1 
            time.sleep(1)

    except Exception as e_geral:
        print(f"Erro no loop principal: {e_geral}")
        time.sleep(2)

print("\n------------------------------------------------")
print("Processo Finalizado.")
print("------------------------------------------------")