from playwright.sync_api import sync_playwright
import time
import random

class BotShopee:
    def __init__(self):
        self.respostas = [
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
Equipe TerabyteShop""",

    """Ficamos muito felizes com o seu feedback! É ótimo saber que conseguimos proporcionar uma experiência positiva com a sua compra. Esperamos que o produto supere suas expectativas no dia a dia!

Agradecemos a confiança em nossa loja. Estamos à disposição para qualquer dúvida futura.

Atenciosamente, Equipe TerabyteShop""",

    """Muito obrigado pela sua avaliação positiva! 🌟 Sua satisfação é a nossa maior prioridade. Ficamos contentes que tenha gostado da sua escolha. Aproveite muito o seu novo item!

Obrigado pela preferência! Conte sempre com a TerabyteShop para o que precisar.

Atenciosamente, Equipe TerabyteShop""",

    """Agradecemos imensamente por compartilhar sua opinião! Saber que tudo chegou corretamente e que você está satisfeito nos motiva a continuar oferecendo o melhor serviço. Fez uma excelente aquisição!

Obrigado por escolher a TerabyteShop. Seguimos à disposição sempre que precisar.

Atenciosamente, Equipe TerabyteShop""",

    """Olá! Obrigado por dedicar um tempo para nos avaliar. Ficamos honrados com a sua preferência e felizes em saber que atendemos ao que você esperava. Desejamos um excelente uso do produto!

Conte sempre conosco, estamos à disposição.

Atenciosamente, Equipe TerabyteShop""",

    """Muito obrigado pela excelente avaliação! Trabalhamos todos os dias para garantir essa qualidade que você recebeu. Esperamos ver você por aqui novamente em breve para novos upgrades!

Obrigado pela preferência! Conte sempre com a TerabyteShop.

Atenciosamente, Equipe TerabyteShop""",
]

    def pegar_resposta(self):
        return random.choice(self.respostas)

    def executar(self):
        print("--- INICIANDO BOT SHOPEE (V3 - Seletores Ajustados) ---")
        
        with sync_playwright() as p:
            # Abre o navegador
            browser = p.chromium.launch(headless=False, args=['--start-maximized'])
            context = browser.new_context(no_viewport=True)
            page = context.new_page()

            print("Acessando Shopee Seller Center...")
            page.goto("https://seller.shopee.com.br/")

            print("\n" + "="*50)
            print("1. Faça o LOGIN manualmente.")
            print("2. Vá até a tela de AVALIAÇÕES.")
            print("3. Quando carregar a lista de avaliações, VOLTE AQUI e aperte ENTER.")
            print("="*50 + "\n")
            input("Aguardando você... (Pressione Enter para iniciar)")

            while True:
                try:
                    print("Buscando avaliações pendentes...")
                    
                    # 1. ENCONTRAR BOTÕES "RESPONDER" (O que abre a caixinha)
                    # Baseado na sua imagem: <button>...<span>Responder</span>...</button>
                    botoes_abrir = page.locator("button").filter(has_text="Responder").all()
                    
                    # Filtra apenas os visíveis
                    botoes_visiveis = [b for b in botoes_abrir if b.is_visible()]
                    
                    qtd = len(botoes_visiveis)
                    print(f"Encontrados {qtd} botões 'Responder' na tela.")

                    if qtd == 0:
                        print("Nenhum botão encontrado. Rolando para baixo...")
                        page.mouse.wheel(0, 500)
                        time.sleep(3)
                        # Se continuar 0, talvez tenha acabado ou precise de F5
                        # Vamos dar continue para ele tentar rolar mais ou dar reload no final
                        # Mas se rolar muito sem achar, o loop externo daria reload.
                        # Aqui vamos pular para o reload direto se não achar nada
                        pass 

                    for i, botao in enumerate(botoes_visiveis):
                        try:
                            if not botao.is_visible():
                                continue
                                
                            print(f"-> Processando item {i+1}...")
                            botao.click(force=True)
                            time.sleep(1.5) # Espera o modal abrir

                            # 2. PREENCHER TEXTO
                            caixa_texto = page.locator("textarea").first
                            
                            if caixa_texto.is_visible():
                                resposta = self.pegar_resposta()
                                caixa_texto.fill(resposta)
                                time.sleep(0.5)

                                # 3. CLICAR EM "ENVIAR" (Baseado na sua segunda imagem)
                                # Imagem mostra: <button>...<span>Enviar</span>...</button>
                                btn_enviar = page.locator("button").filter(has_text="Enviar").last
                                
                                if btn_enviar.is_visible():
                                    btn_enviar.click()
                                    print("   Enviado com sucesso!")
                                    time.sleep(2) # Espera modal fechar
                                else:
                                    print("   ERRO: Botão 'Enviar' não apareceu.")
                                    page.keyboard.press("Escape")
                            
                            else:
                                print("   ERRO: Caixa de texto não abriu.")
                                page.keyboard.press("Escape")

                        except Exception as e:
                            print(f"   Erro no item {i+1}: {e}")
                            page.keyboard.press("Escape")

                    print("Ciclo concluído. Atualizando página em 5s...")
                    time.sleep(5)
                    page.reload()
                    page.wait_for_load_state("networkidle")

                except KeyboardInterrupt:
                    print("\nParado pelo usuário.")
                    break
                except Exception as e:
                    print(f"Erro geral: {e}")
                    time.sleep(5)

if __name__ == "__main__":
    bot = BotShopee()
    bot.executar()