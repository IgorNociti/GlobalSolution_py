💧 EcoDrain – Simulador de Monitoramento Urbano
🧠 Prevenção de enchentes começa antes da água subir. Essa solução simula como tecnologia acessível pode salvar vidas em áreas urbanas.

❤️ Desenvolvedores:
Henrique Maciel Rm559628


Igor Nociti Rm560225


Pedro Paulo Sabino RM559578

📽️ Demonstração
▶️ Vídeo demonstrativo: [INSIRA LINK DO VÍDEO AQUI]
📊 Link do PDF: mapa_bueiros.html (gerado automaticamente após a execução)

O Bueiro Inteligente é um sistema desenvolvido em Python para simular um sistema de alerta preventivo contra enchentes urbanas.
Utilizando dados fictícios de sensores, o sistema detecta o nível de risco de cada bueiro com base na vazão, nível da água e tempo de chuva, apresentando essas informações em um mapa interativo da cidade.

🌆 Ideal para estudos de soluções tecnológicas em defesa civil e prevenção de desastres urbanos.

✨ Funcionalidades
✅ Geração de nomes de ruas aleatórios com base em bairros brasileiros
📏 Simulação de dados de sensores: nível da água (cm), vazão (L/min) e tempo de chuva (min)
🚦 Avaliação de risco automatizada (sem risco, risco baixo, risco crítico)
🗺️ Mapa interativo com marcadores coloridos por nível de risco
📋 Registro de alertas em arquivo de log com data e hora
💬 Comentários explicativos acessíveis mesmo para iniciantes
⚠️ Tratamento de exceções para evitar falhas inesperadas

🚀 Como Usar
Pré-requisitos:

Python 3 instalado

Instale as bibliotecas necessárias:

bash
Copiar
Editar
pip install faker folium
Execute o sistema no terminal:

bash
Copiar
Editar
python bueiro_inteligente.py
📁 Estrutura do Projeto
bash
Copiar
Editar
📦 bueiro-inteligente
├── bueiro_inteligente.py        # Código principal com simulação e mapa
├── log_bueiros.txt              # Histórico dos alertas registrados
├── mapa_bueiros.html            # Mapa gerado com os bueiros simulados
🛠️ Tecnologias e Bibliotecas Utilizadas
Python 3

random, datetime (padrão da linguagem)

Faker – geração de nomes de ruas fictícias

Folium – visualização de mapas interativos

🧠 Tecnologias e Conceitos Aplicados
Estruturas de dados (listas e dicionários)

Manipulação de arquivos (.txt)

Funções modulares e reutilizáveis

Tratamento de exceções com try/except
