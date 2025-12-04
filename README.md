# Automatizar_avaliacoes

Scripts criados para responder avaliações da Shopee.

Assim que cheguei no setor de Marketplace na Terabyte recebi uma demanda que seria responder as avaliações feitas pelos clientes nos ultimos dois meses e planilha-las, a principio pensei em utilizar o Selenium para a automação, porém tive erros ao encontrar o botão 'Responder' e não estava conseguindo resolver.
Após isso fui pro mais basico e desenvolvi um script com Pyautogui, o que a principio funcionou porém estava demorando em torno de 20 segundos para responder cada avaliação, então lembrei que poderia fazer com playwright e essa é a versão que melhor funcionou até o momento.

Respondi em torno de duas mil avaliações em poucous minutos.

Nesse repositorio tambem está contido um script em selenium que serve para ler as paginas respondidas e extrair alguns dados especificos como Nome do cliente, Nome do produto, Comentario do cliente, Resposta do vendedor.
