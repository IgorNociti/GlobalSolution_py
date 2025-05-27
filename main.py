"""
Henrique Maciel RM559628
Igor Nociti Rm560225

"""

import random
from faker import Faker
from datetime import datetime
import folium

"""
Importação de bibliotecas:
- random: para gerar valores aleatórios simulando sensores
- faker: para gerar nomes de ruas fictícios
- datetime: para registrar a hora do alerta
- folium: para criar o mapa interativo com os bueiros
"""

fake = Faker('pt_BR')

"""
Essa função gera coordenadas aleatórias na cidade de São Paulo.
Serve para simular onde está localizado cada bueiro.
""" 
def gerar_coordenadas_sp():
    lat = random.uniform(-23.70, -23.50)
    lon = random.uniform(-46.75, -46.55)
    return lat, lon

""" 
Essa função cria uma lista com vários bueiros.
Cada bueiro tem um nome de rua, um nível de água, uma vazão de água,
tempo de chuva, localização (lat/lon) e um nível de risco.
Tudo isso é gerado aleatoriamente como uma simulação.
""" 
def gerar_bueiros(qtd=7):
    bueiros = []
    for _ in range(qtd):
        rua = fake.street_name()
        nivel = round(random.uniform(10, 60), 2)
        vazao = round(random.uniform(0, 20), 2)
        chuva = random.randint(0, 60)
        lat, lon = gerar_coordenadas_sp()

        """
        Essa parte avalia o risco com base nas condições simuladas:
        - Se o nível de água está muito alto, a vazão baixa e está chovendo muito → risco crítico
        - Se o nível está moderado e choveu muito → risco baixo
        - Caso contrário → sem risco
        """
        if nivel > 40 and vazao < 10 and chuva >= 20:
            risco = "🚨 RISCO CRÍTICO"
            cor = "red"
        elif nivel > 30 and chuva > 30:
            risco = "⚠️ RISCO BAIXO"
            cor = "orange"
        else:
            risco = "✅ SEM RISCO"
            cor = "green"

        bueiros.append({
            "rua": rua,
            "nivel": nivel,
            "vazao": vazao,
            "chuva": chuva,
            "risco": risco,
            "cor": cor,
            "lat": lat,
            "lon": lon
        })
    return bueiros

""" 
Essa função cria um mapa da cidade com todos os bueiros simulados.
Cada bueiro aparece com um marcador colorido mostrando o nível de risco.
O mapa é salvo como um arquivo HTML que pode ser aberto no navegador.
""" 
def gerar_mapa_bueiros(bueiros):
    mapa = folium.Map(location=[-23.55, -46.63], zoom_start=12)
    for b in bueiros:
        popup = f"""
        <b>{b['risco']}</b><br>
        Rua: {b['rua']}<br>
        Nível: {b['nivel']} cm<br>
        Vazão: {b['vazao']} L/min<br>
        Chuva: {b['chuva']} min
        """
        folium.Marker(
            location=[b['lat'], b['lon']],
            popup=popup,
            icon=folium.Icon(color=b['cor'])
        ).add_to(mapa)

    mapa.save("mapa_bueiros.html")
    print("📍 Mapa salvo como 'mapa_bueiros.html'")

"""
Essa função salva as informações de cada bueiro em um arquivo chamado 'log_bueiros.txt'.
Cada linha do arquivo mostra o que aconteceu em determinada rua, como se fosse um histórico.
""" 
def registrar_log(bueiro):
    data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    log = f"[{data_hora}] Rua: {bueiro['rua']} | Nível: {bueiro['nivel']}cm | Vazão: {bueiro['vazao']}L/min | Chuva: {bueiro['chuva']}min | Alerta: {bueiro['risco']}\n"
    with open("log_bueiros.txt", "a", encoding="utf-8") as f:
        f.write(log)

""" 
Essa é a função principal que executa todo o programa:
- Gera os bueiros
- Mostra os alertas no terminal
- Salva os dados no arquivo de log
- Cria o mapa com os alertas
Ela também trata qualquer erro que possa acontecer com try/except.
""" 
def main():
    print("\n💧 Monitoramento Inteligente de Bueiros Urbanos 💧\n")
    try:
        bueiros = gerar_bueiros()

        for b in bueiros:
            print(f"🛣️ {b['rua']} → {b['risco']} (Nível: {b['nivel']}cm | Vazão: {b['vazao']}L/min | Chuva: {b['chuva']}min)")
            registrar_log(b)

        gerar_mapa_bueiros(bueiros)
        print("\n✅ Dados salvos em 'log_bueiros.txt' e mapa gerado com sucesso!\n")

    except Exception as e:
        print(f"⚠️ Erro durante a execução: {e}")

""" 
Aqui é onde o programa realmente começa a rodar.
Ele chama a função principal acima.
""" 
if __name__ == "__main__":
    main()
