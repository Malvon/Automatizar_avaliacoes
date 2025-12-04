import pyautogui
import time
import random
import pyperclip

class BotAtendimento:
    def __init__(self):
        # Configurações iniciais
        pyautogui.PAUSE = 0.5
        pyautogui.FAILSAFE = True
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

    def selecionar_resposta_aleatoria(self):
        return random.choice(self.respostas)

    def colar_texto(self, texto):
        pyperclip.copy(texto)
        pyautogui.hotkey('ctrl', 'v')

    def responder_chamado(self, x_msg, y_msg, x_enviar, y_enviar):
        """Função genérica para responder um chamado baseado nas coordenadas"""
        # 1. Clica no campo de mensagem
        pyautogui.click(x=x_msg, y=y_msg)
        time.sleep(0.5)

        # 2. Cola a resposta
        texto = self.selecionar_resposta_aleatoria()
        self.colar_texto(texto)
        time.sleep(0.5)

        # 3. Clica em enviar (e confirmações se houver)
        pyautogui.click(x=x_enviar, y=y_enviar)
        time.sleep(0.5)
        
        # Se houver um segundo clique de confirmação logo abaixo (ajuste conforme necessário)
        pyautogui.click(x=x_enviar, y=y_enviar - 31) # Exemplo baseado no seu código (741 -> 710)

    def executar(self):
        print("Iniciando automação. Ctrl+C para parar.")
        contador = 1
        
        try:
            while True:
                print(f"--- Ciclo {contador} ---")

                # --- PRIMEIRO ATENDIMENTO (TOPO) ---
                pyautogui.click(x=1633, y=855) # Abre o chamado/menu
                time.sleep(1)
                
                # Usa o método da classe (limpo e reutilizável)
                self.responder_chamado(x_msg=931, y_msg=594, x_enviar=1197, y_enviar=741)

                # --- SCROLL E SEGUNDO ATENDIMENTO ---
                pyautogui.scroll(-5000)
                time.sleep(1)

                # Clica na resposta mais abaixo (sequência de cliques de preparação)
                coords_preparacao = [(1635, 612), (1635, 754), (1635, 829), (1635, 929)]
                for x, y in coords_preparacao:
                    pyautogui.click(x=x, y=y)
                
                # Responde o segundo
                self.responder_chamado(x_msg=931, y_msg=594, x_enviar=1197, y_enviar=741)

                # --- REFRESH ---
                print("Aguardando refresh...")
                time.sleep(5)
                pyautogui.press('f5')
                time.sleep(4) # Espera carregar
                
                contador += 1

        except KeyboardInterrupt:
            print("Parado pelo usuário.")

if __name__ == "__main__":
    bot = BotAtendimento()
    # Dê 5 segundos para focar na tela
    time.sleep(5)
    bot.executar()