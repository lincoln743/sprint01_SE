# -*- coding: utf-8 -*-
"""Figuras do Documento de Visão — Sprint 1 (ARGOS / Sentinela Nuclear)."""
from svgbase import Tela, CORES

CINZA_B = "#f4f4f4"
CINZA_M = "#e2e2e2"
BORDA = "#8a8a8a"
ACENTO = "#9b1c31"


def elipse(t, cx, cy, rx, ry, cor="azul"):
    b, f = CORES[cor]
    t.add('<ellipse cx="%g" cy="%g" rx="%g" ry="%g" fill="%s" stroke="%s" '
          'stroke-width="2"/>' % (cx, cy, rx, ry, f, b))


def ator(t, x, y, nome, esc=1.0):
    """Boneco palito simples."""
    c = "#333333"
    t.add('<circle cx="%g" cy="%g" r="%g" fill="none" stroke="%s" stroke-width="2"/>'
          % (x, y, 11 * esc, c))
    t.add('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2"/>'
          % (x, y + 11 * esc, x, y + 38 * esc, c))
    t.add('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2"/>'
          % (x - 15 * esc, y + 22 * esc, x + 15 * esc, y + 22 * esc, c))
    t.add('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2"/>'
          % (x, y + 38 * esc, x - 13 * esc, y + 60 * esc, c))
    t.add('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="2"/>'
          % (x, y + 38 * esc, x + 13 * esc, y + 60 * esc, c))
    for i, l in enumerate(nome.split("\n")):
        t.texto(x, y + 78 * esc + i * 17, l, tam=13.5, anc="middle")


# =============================================================== figura 1
def stakeholders():
    t = Tela(1180, 760)
    x0, y0, w, h = 150, 60, 950, 600

    t.retangulo(x0, y0, w / 2, h / 2, fundo="#fdf6e3", borda=BORDA)
    t.retangulo(x0 + w / 2, y0, w / 2, h / 2, fundo="#fbe9ec", borda=BORDA)
    t.retangulo(x0, y0 + h / 2, w / 2, h / 2, fundo="#f2f2f2", borda=BORDA)
    t.retangulo(x0 + w / 2, y0 + h / 2, w / 2, h / 2, fundo="#eaf2fb", borda=BORDA)

    t.texto(x0 + 16, y0 + 28, "MANTER SATISFEITO", tam=13, peso="bold", cor="#8a5a00")
    t.texto(x0 + w / 2 + 16, y0 + 28, "GERIR DE PERTO", tam=13, peso="bold", cor=ACENTO)
    t.texto(x0 + 16, y0 + h / 2 + 28, "MONITORAR", tam=13, peso="bold", cor="#555555")
    t.texto(x0 + w / 2 + 16, y0 + h / 2 + 28, "MANTER INFORMADO", tam=13, peso="bold",
            cor="#1f4e79")

    itens = [
        (640, 130, "Órgãos reguladores\n(CNEN, AIEA)"),
        (880, 160, "Gestor da instalação"),
        (760, 240, "Equipe de segurança\nfísica"),
        (980, 250, "Coordenador do\ncentro de operações"),
        (330, 170, "Comando da Marinha /\nAlta direção da AMAZUL"),
        (300, 300, "Área de TI e\nsegurança da informação"),
        (700, 430, "Operador de\nmonitoramento"),
        (930, 470, "Equipe de inspeção\ne manutenção"),
        (880, 580, "Administrador do\nsistema"),
        (320, 450, "Fornecedores de\nsensores e drones"),
        (340, 580, "Comunidade do entorno\ne imprensa"),
    ]
    for cx, cy, nome in itens:
        linhas = nome.split("\n")
        larg = max(len(l) for l in linhas) * 7.6 + 26
        alt = 22 * len(linhas) + 14
        t.retangulo(cx - larg / 2, cy - alt / 2, larg, alt, fundo="#ffffff",
                    borda="#555555", traco=1.5)
        for i, l in enumerate(linhas):
            t.texto(cx, cy - alt / 2 + 22 + i * 20, l, tam=13.5, anc="middle")

    t.seta(x0, y0 + h + 24, x0 + w, y0 + h + 24)
    t.texto(x0 + w / 2, y0 + h + 52, "INTERESSE no resultado do sistema", tam=14,
            peso="bold", anc="middle")
    t.add('<text x="%g" y="%g" font-family="DejaVu Sans" font-size="14" '
          'font-weight="bold" transform="rotate(-90 %g %g)" text-anchor="middle">'
          'INFLUÊNCIA sobre o projeto</text>' % (90, y0 + h / 2, 90, y0 + h / 2))
    t.seta(118, y0 + h, 118, y0)
    return t.salvar("fig_stakeholders")


# =============================================================== figura 2
def camadas():
    t = Tela(1260, 782)

    faixas = [
        ("BORDA — onde o dado nasce", "verde", 60, [
            ("Câmeras fixas e PTZ", "visão computacional embarcada; detecção de\npessoa, veículo e objeto abandonado"),
            ("Drones autônomos", "varredura programada do perímetro e verificação\nsob demanda de um alerta"),
            ("Sensores IoT", "cerca perimetral, abertura de portas, movimento,\nvibração, radiação ambiental e meteorologia"),
        ]),
        ("PLATAFORMA — onde o dado vira informação", "azul", 268, [
            ("Ingestão e normalização", "fila de eventos, carimbo de tempo e\ngeolocalização padronizados"),
            ("Correlação e IA", "fusão de múltiplas fontes, pontuação de risco e\nsupressão de falso positivo"),
            ("Regras e orquestração", "política de severidade, despacho de drone e\nabertura de ocorrência"),
        ]),
        ("APRESENTAÇÃO — onde a informação vira ação", "ocre", 476, [
            ("Painel operacional", "mapa da planta, fila de alertas e indicadores\nem tempo real"),
            ("Verificação assistida", "vídeo, trilha do evento e ações do operador\nem uma única tela"),
            ("Registro e auditoria", "ocorrência assinada, trilha imutável e relatório\npara o regulador"),
        ]),
    ]

    for titulo, cor, y, blocos in faixas:
        t.caixa(40, y, 1180, 186, cor=cor, r=12)
        t.texto(60, y + 28, titulo, tam=15, peso="bold", cor=CORES[cor][0])
        x = 60
        for nome, desc in blocos:
            t.retangulo(x, y + 44, 368, 126, fundo="#ffffff", borda="#777777")
            t.texto(x + 16, y + 70, nome, tam=14.5, peso="bold")
            for i, l in enumerate(desc.split("\n")):
                t.texto(x + 16, y + 94 + i * 19, l, tam=13, cor="#333333")
            x += 386

    etapas = ["DADOS", "INFORMAÇÃO", "INTELIGÊNCIA", "AÇÃO"]
    legendas = ["sensores, imagens\ne telemetria",
                "eventos correlacionados\ne contextualizados",
                "risco classificado\ne priorizado",
                "alerta, despacho\ne ocorrência registrada"]
    x = 52
    for i, (e, l) in enumerate(zip(etapas, legendas)):
        t.retangulo(x, 678, 262, 42, fundo="#e6def7", borda="#4b2e83", traco=1.8)
        t.texto(x + 131, 705, e, tam=15, peso="bold", anc="middle", cor="#4b2e83")
        for k, ll in enumerate(l.split("\n")):
            t.texto(x + 131, 742 + k * 17, ll, tam=12.5, anc="middle", cor="#444444")
        if i < 3:
            t.seta(x + 266, 699, x + 294, 699)
        x += 300
    return t.salvar("fig_camadas")


# =============================================================== figura 3
def contexto():
    t = Tela(1260, 700)

    t.retangulo(360, 230, 520, 230, fundo="#dff0e4", borda="#1e6b3a", traco=2.6, r=14)
    t.texto(620, 282, "ARGOS", tam=26, peso="bold", anc="middle", cor="#1e6b3a")
    t.texto(620, 312, "[Sistema de software]", tam=13, anc="middle", cor="#444444")
    t.paragrafo(620, 346, [
        "Monitora o perímetro e as áreas restritas da instalação,",
        "correlaciona sensores, câmeras e drones, classifica o risco",
        "e apoia a decisão do operador em tempo real.",
    ], tam=13.5, anc="middle", cor="#222222")

    esq = [
        (120, "Operador de\nmonitoramento", "acompanha o painel e\nvalida cada alerta"),
        (300, "Equipe de\nsegurança física", "recebe o despacho e\natende a ocorrência"),
        (480, "Gestor da\ninstalação", "acompanha indicadores\ne relatórios"),
    ]
    for y, nome, desc in esq:
        t.retangulo(40, y, 250, 108, fundo="#ebebeb", borda="#3f3f3f", traco=2)
        t.texto(60, y + 30, nome.split("\n")[0], tam=14.5, peso="bold")
        t.texto(60, y + 50, nome.split("\n")[1], tam=14.5, peso="bold")
        for i, l in enumerate(desc.split("\n")):
            t.texto(60, y + 74 + i * 18, l, tam=12.5, cor="#444444")
        t.seta(294, y + 54, 356, 300 if y != 300 else 310)

    dir_ = [
        (60, "Sistema de controle\nde acesso", "credenciais e registro\nde entrada e saída"),
        (210, "CFTV existente", "fluxo de vídeo das\ncâmeras já instaladas"),
        (360, "Estação meteorológica\ne monitoração radiológica", "condições ambientais\ne taxa de dose"),
        (510, "Centro de operações\nda instalação", "notificação e\nregistro de ocorrência"),
    ]
    for y, nome, desc in dir_:
        t.retangulo(930, y, 290, 110, fundo="#eaf2fb", borda="#1f4e79", traco=2)
        ls = nome.split("\n")
        for i, l in enumerate(ls):
            t.texto(950, y + 28 + i * 19, l, tam=14, peso="bold", cor="#1f4e79")
        for i, l in enumerate(desc.split("\n")):
            t.texto(950, y + 28 + len(ls) * 19 + 6 + i * 17, l, tam=12.5, cor="#444444")
        t.seta(884, 320, 926, y + 55)

    t.texto(40, 640, "Pessoas", tam=13, peso="bold")
    t.texto(930, 640, "Sistemas e fontes externas", tam=13, peso="bold")
    t.texto(620, 660, "Diagrama de contexto (C4 — nível 1). O detalhamento em contêineres "
            "e componentes será produzido na Sprint 2.",
            tam=13, anc="middle", italico=True, cor="#555555")
    return t.salvar("fig_contexto")


# =============================================================== figura 4
def casos_uso():
    t = Tela(1260, 720)

    t.retangulo(330, 40, 600, 640, fundo="#fbfbfb", borda="#555555", traco=2, r=8)
    t.texto(630, 68, "ARGOS", tam=16, peso="bold", anc="middle")

    casos = [
        (630, 120, "Monitorar perímetro\nem tempo real", "verde"),
        (630, 212, "Receber e triar alerta\nde anomalia", "verde"),
        (630, 304, "Verificar ocorrência\ncom drone", "azul"),
        (630, 396, "Registrar e classificar\na ocorrência", "azul"),
        (630, 488, "Consultar indicadores\ne relatórios", "ocre"),
        (630, 580, "Administrar sensores,\nrotas e usuários", "cinza"),
    ]
    for cx, cy, nome, cor in casos:
        elipse(t, cx, cy, 185, 40, cor=cor)
        ls = nome.split("\n")
        for i, l in enumerate(ls):
            t.texto(cx, cy - 4 + i * 19 - (len(ls) - 1) * 8, l, tam=14, anc="middle")

    ator(t, 150, 150, "Operador de\nmonitoramento")
    ator(t, 150, 390, "Equipe de\nsegurança física")
    ator(t, 150, 600, "Administrador\ndo sistema")
    ator(t, 1120, 180, "Gestor da\ninstalação")
    ator(t, 1120, 430, "Equipe de\ninspeção")

    lig = [
        (178, 180, 450, 125), (178, 185, 450, 215), (178, 195, 452, 300),
        (178, 420, 452, 320), (178, 425, 452, 400),
        (178, 625, 455, 580),
        (1092, 215, 812, 490), (1092, 220, 812, 405),
        (1092, 462, 812, 310),
    ]
    for x1, y1, x2, y2 in lig:
        t.linha(x1, y1, x2, y2, cor="#555555", larg=1.6)

    t.linha(630, 252, 630, 264, cor="#555555", larg=1.6, tracejado="6 4")
    t.texto(648, 262, "«include»", tam=12, italico=True, cor="#555555")
    t.linha(630, 344, 630, 356, cor="#555555", larg=1.6, tracejado="6 4")
    t.texto(648, 354, "«include»", tam=12, italico=True, cor="#555555")

    t.texto(630, 706, "Visão preliminar dos casos de uso; o detalhamento com fluxos "
            "principal e alternativos é previsto para a Sprint 2.",
            tam=13, anc="middle", italico=True, cor="#555555")
    return t.salvar("fig_casos_uso")


# =============================================================== figura 5
def fluxo():
    t = Tela(1260, 820)

    def etapa(x, y, w, h, titulo, desc, cor):
        t.caixa(x, y, w, h, cor=cor, r=10)
        t.texto(x + w / 2, y + 28, titulo, tam=15, peso="bold", anc="middle")
        for i, l in enumerate(desc.split("\n")):
            t.texto(x + w / 2, y + 52 + i * 18, l, tam=12.5, anc="middle", cor="#333333")

    etapa(60, 60, 250, 100, "1 · Captura",
          "sensor, câmera ou drone\nregistra um evento", "verde")
    t.seta(314, 110, 364, 110)
    etapa(368, 60, 250, 100, "2 · Borda",
          "visão computacional classifica\no quadro em milissegundos", "verde")
    t.seta(622, 110, 672, 110)
    etapa(676, 60, 250, 100, "3 · Correlação",
          "a plataforma cruza as fontes\ne pontua o risco", "azul")
    t.seta(930, 110, 980, 110)
    etapa(984, 60, 220, 100, "4 · Alerta",
          "severidade atribuída\ne alerta publicado", "azul")

    t.seta(1094, 164, 1094, 212)
    etapa(900, 216, 304, 100, "5 · Painel operacional",
          "alerta entra na fila, com mapa,\nvídeo e contexto do evento", "ocre")

    t.seta(898, 266, 848, 266)
    t.losango(700, 266, 290, 110, cor="amarelo")
    t.texto(700, 258, "6 · O operador confirma", tam=14, peso="bold", anc="middle")
    t.texto(700, 278, "a anomalia?", tam=14, peso="bold", anc="middle")

    t.seta(700, 322, 700, 372)
    t.texto(712, 350, "sim", tam=13, cor="#1e6b3a")
    etapa(560, 376, 280, 100, "7 · Verificação",
          "drone é despachado para a\ncoordenada e transmite ao vivo", "ver")

    t.seta(554, 266, 464, 266)
    t.texto(500, 254, "não", tam=13, cor=ACENTO)
    etapa(200, 216, 264, 100, "6a · Falso positivo",
          "operador classifica o motivo;\no caso realimenta o modelo", "cinza")
    t.linha(332, 318, 332, 742, cor="#666666", larg=2.4)
    t.seta(332, 742, 494, 742)

    t.seta(700, 480, 700, 530)
    etapa(560, 534, 280, 100, "8 · Resposta",
          "equipe de segurança é acionada\ncom instrução e localização", "ver")
    t.seta(700, 638, 700, 688)
    etapa(500, 692, 400, 100, "9 · Registro e auditoria",
          "ocorrência registrada com trilha completa, disponível para\nrelatório e para o órgão regulador", "lilas")

    t.texto(52, 520, "Realimentação do modelo", tam=13, peso="bold", cor="#555555")
    t.paragrafo(52, 544, [
        "Tanto a confirmação quanto o",
        "falso positivo são rotulados pelo",
        "operador e entram no conjunto",
        "de treinamento — a precisão do",
        "sistema cresce com o uso.",
    ], tam=12.5, cor="#555555")
    return t.salvar("fig_fluxo")


# =========================================================== wireframes
def _moldura(t, titulo, sub):
    t.retangulo(30, 30, t.w - 60, t.h - 60, fundo="#ffffff", borda="#444444",
                traco=2.4, r=8)
    t.retangulo(30, 30, t.w - 60, 54, fundo="#3f3f3f", borda="#3f3f3f", r=8)
    t.texto(54, 64, "ARGOS", tam=18, peso="bold", cor="#ffffff")
    t.texto(142, 64, titulo, tam=14, cor="#dddddd")
    t.texto(t.w - 54, 64, sub, tam=13, cor="#dddddd", anc="end")


def tela_painel():
    t = Tela(1260, 790)
    _moldura(t, "Painel operacional", "Centro de Operações  ·  op. M. Fonseca  ·  14:32")

    # menu lateral
    t.retangulo(30, 84, 180, 676, fundo=CINZA_M, borda=CINZA_M, r=0)
    menu = ["Painel", "Ocorrências", "Drones", "Sensores", "Rotas de inspeção",
            "Relatórios", "Administração"]
    for i, m in enumerate(menu):
        if i == 0:
            t.retangulo(30, 100 + i * 46, 180, 40, fundo="#ffffff", borda="#ffffff", r=0)
            t.retangulo(30, 100 + i * 46, 5, 40, fundo=ACENTO, borda=ACENTO, r=0)
        t.texto(54, 126 + i * 46, m, tam=14, peso="bold" if i == 0 else "normal")

    # mapa
    t.retangulo(226, 100, 640, 420, fundo="#f7f9fb", borda=BORDA)
    t.texto(246, 126, "Planta da instalação — setores A a D", tam=14, peso="bold")
    t.texto(846, 126, "[ mapa / planta baixa ]", tam=12, anc="end", cor="#888888")

    t.retangulo(250, 146, 592, 356, fundo="#eef2f5", borda="#c9ced3", tracejado="6 5")
    t.retangulo(286, 200, 230, 150, fundo="#ffffff", borda="#9aa3ab")
    t.texto(300, 224, "Prédio do reator", tam=12.5, cor="#555555")
    t.retangulo(560, 200, 180, 110, fundo="#ffffff", borda="#9aa3ab")
    t.texto(574, 224, "Depósito", tam=12.5, cor="#555555")
    t.retangulo(286, 384, 454, 90, fundo="#ffffff", borda="#9aa3ab")
    t.texto(300, 408, "Pátio / cerca perimetral oeste", tam=12.5, cor="#555555")

    for cx, cy in [(330, 180), (520, 180), (700, 190), (330, 370), (620, 420), (780, 300)]:
        t.circulo(cx, cy, 9, cor="azul", traco=1.6)
    t.circulo(500, 440, 15, cor="ver", traco=2.4)
    t.texto(500, 445, "!", tam=15, peso="bold", anc="middle", cor=ACENTO)
    t.circulo(660, 250, 12, cor="verde", traco=2)
    t.texto(660, 255, "D", tam=12, peso="bold", anc="middle", cor="#1e6b3a")

    t.texto(250, 492, "● câmera    ◉ drone em voo    ! alerta ativo", tam=12.5,
            cor="#555555")

    # fila de alertas
    t.retangulo(882, 100, 348, 420, fundo="#ffffff", borda=BORDA)
    t.texto(902, 126, "Alertas ativos (3)", tam=14, peso="bold")
    t.texto(1210, 126, "filtrar", tam=12.5, anc="end", cor="#777777")
    alertas = [
        ("ALTA", "Pessoa não identificada", "Cerca oeste · setor C · 14:31", "ver"),
        ("MÉDIA", "Drone não autorizado", "Espaço aéreo norte · 14:18", "ocre"),
        ("BAIXA", "Porta aberta além do tempo", "Depósito B2 · 14:04", "amarelo"),
    ]
    y = 146
    for sev, titulo, ctx, cor in alertas:
        t.retangulo(902, y, 308, 104, fundo="#ffffff", borda="#bbbbbb")
        t.caixa(916, y + 14, 72, 24, cor=cor, r=12)
        t.texto(952, y + 31, sev, tam=11.5, peso="bold", anc="middle")
        t.texto(1000, y + 31, titulo, tam=13.5, peso="bold")
        t.texto(916, y + 60, ctx, tam=12.5, cor="#555555")
        t.retangulo(916, y + 70, 110, 24, fundo=CINZA_B, borda="#999999")
        t.texto(971, y + 87, "verificar", tam=12, anc="middle")
        t.retangulo(1036, y + 70, 110, 24, fundo=CINZA_B, borda="#999999")
        t.texto(1091, y + 87, "despachar", tam=12, anc="middle")
        y += 118

    # indicadores
    kpis = [("Alertas abertos", "3"), ("Tempo médio de detecção", "38 s"),
            ("Falsos positivos (24 h)", "7 %"), ("Drones disponíveis", "2 de 3"),
            ("Sensores fora do ar", "1")]
    x = 226
    for nome, valor in kpis:
        t.retangulo(x, 540, 192, 90, fundo=CINZA_B, borda=BORDA)
        t.texto(x + 96, 574, valor, tam=22, peso="bold", anc="middle")
        t.texto(x + 96, 600, nome, tam=12, anc="middle", cor="#555555")
        x += 202

    t.retangulo(226, 648, 1004, 82, fundo="#ffffff", borda=BORDA)
    t.texto(246, 674, "Últimos registros", tam=13.5, peso="bold")
    t.texto(246, 698, "14:02  Ocorrência #2418 encerrada — ronda confirmou animal de "
            "grande porte junto à cerca leste.", tam=12.5, cor="#444444")
    t.texto(246, 718, "13:47  Inspeção programada do setor D concluída pelo drone "
            "ARG-02 — sem apontamentos.", tam=12.5, cor="#444444")
    return t.salvar("fig_tela_painel")


def tela_ocorrencia():
    t = Tela(1260, 740)
    _moldura(t, "Ocorrência #2431 — verificação", "severidade ALTA  ·  aberta às 14:31")

    t.retangulo(56, 104, 580, 400, fundo="#2b2b2b", borda="#2b2b2b")
    t.texto(76, 132, "Câmera CAM-17 · cerca oeste · ao vivo", tam=13, cor="#eeeeee")
    t.retangulo(250, 190, 190, 250, fundo="none", borda="#ff4d6d", traco=3)
    t.texto(250, 182, "pessoa  0,93", tam=13, peso="bold", cor="#ff4d6d")
    t.retangulo(470, 300, 110, 80, fundo="none", borda="#ffd166", traco=2.5,
                tracejado="6 4")
    t.texto(470, 292, "objeto  0,61", tam=12.5, peso="bold", cor="#ffd166")
    t.texto(76, 486, "[ quadro do vídeo com as detecções do modelo ]", tam=12,
            cor="#999999")

    t.retangulo(56, 520, 580, 184, fundo="#ffffff", borda=BORDA)
    t.texto(76, 548, "Linha do tempo do evento", tam=14, peso="bold")
    linha = [
        ("14:31:02", "sensor de cerca FEN-09 registra vibração acima do limiar"),
        ("14:31:03", "CAM-17 confirma presença humana (confiança 0,93) na borda"),
        ("14:31:04", "correlação eleva o risco para ALTA e publica o alerta"),
        ("14:31:19", "operador abre a ocorrência e solicita verificação aérea"),
        ("14:31:40", "drone ARG-02 decola para a coordenada"),
    ]
    for i, (h, d) in enumerate(linha):
        t.circulo(90, 576 + i * 25, 4, cor="ver", traco=1)
        t.texto(106, 581 + i * 25, h, tam=12.5, peso="bold", mono=True)
        t.texto(186, 581 + i * 25, d, tam=12.5, cor="#333333")

    t.retangulo(656, 104, 548, 290, fundo="#ffffff", borda=BORDA)
    t.texto(676, 132, "Contexto do alerta", tam=14, peso="bold")
    dados = [
        ("Local", "Setor C — cerca perimetral oeste, poste 14"),
        ("Coordenada", "23°26'S  47°33'W  ·  zona restrita nível 2"),
        ("Fontes correlacionadas", "FEN-09 (vibração) + CAM-17 (vídeo)"),
        ("Acesso autorizado", "nenhuma credencial registrada no setor"),
        ("Condições", "noite, 18 °C, visibilidade boa, vento 9 km/h"),
        ("Radiação ambiental", "0,11 µSv/h — dentro da faixa normal"),
        ("Histórico do ponto", "2 ocorrências em 30 dias, ambas confirmadas"),
    ]
    for i, (k, v) in enumerate(dados):
        t.texto(676, 162 + i * 30, k, tam=12.5, peso="bold", cor="#555555")
        t.texto(880, 162 + i * 30, v, tam=12.5, cor="#222222")

    t.retangulo(656, 410, 548, 294, fundo="#ffffff", borda=BORDA)
    t.texto(676, 438, "Ações do operador", tam=14, peso="bold")
    botoes = [
        ("Despachar drone de verificação", "ver"),
        ("Acionar equipe de segurança", "ocre"),
        ("Classificar como falso positivo", "cinza"),
        ("Encerrar e registrar ocorrência", "verde"),
    ]
    for i, (b, cor) in enumerate(botoes):
        t.caixa(676, 458 + i * 50, 420, 38, cor=cor, r=6)
        t.texto(886, 482 + i * 50, b, tam=13.5, peso="bold", anc="middle")
    t.texto(676, 676, "Toda ação fica registrada com usuário, horário e "
            "justificativa — a trilha é imutável.", tam=12, italico=True, cor="#555555")
    return t.salvar("fig_tela_ocorrencia")


def tela_inspecao():
    t = Tela(1260, 700)
    _moldura(t, "Inspeção aérea — drone ARG-02", "missão MIS-0147  ·  em execução")

    t.retangulo(56, 104, 700, 440, fundo="#f7f9fb", borda=BORDA)
    t.texto(76, 132, "Rota de inspeção — perímetro oeste", tam=14, peso="bold")
    t.retangulo(80, 150, 652, 376, fundo="#eef2f5", borda="#c9ced3", tracejado="6 5")

    pontos = [(160, 460), (260, 300), (420, 230), (560, 300), (640, 420), (560, 490)]
    for i in range(len(pontos) - 1):
        t.linha(pontos[i][0], pontos[i][1], pontos[i + 1][0], pontos[i + 1][1],
                cor="#1f4e79", larg=2.4, tracejado="8 5")
    for i, (x, y) in enumerate(pontos):
        t.circulo(x, y, 13, cor="azul", traco=2)
        t.texto(x, y + 5, str(i + 1), tam=12.5, peso="bold", anc="middle")
    t.circulo(420, 230, 21, cor="ver", traco=2.6, fundo="none")
    t.texto(452, 224, "posição atual", tam=12.5, peso="bold", cor=ACENTO)
    t.circulo(640, 420, 21, cor="ocre", traco=2.4, fundo="none")
    t.texto(612, 414, "ponto da ocorrência #2431", tam=12.5, anc="end", cor="#8a5a00")

    t.retangulo(776, 104, 428, 196, fundo="#ffffff", borda=BORDA)
    t.texto(796, 132, "Telemetria", tam=14, peso="bold")
    tel = [("Bateria", "68 %  ·  autonomia 14 min"),
           ("Altitude", "42 m AGL"),
           ("Enlace", "estável  ·  -58 dBm"),
           ("Velocidade", "6,2 m/s"),
           ("Próximo ponto", "waypoint 4 em 25 s")]
    for i, (k, v) in enumerate(tel):
        t.texto(796, 162 + i * 27, k, tam=12.5, peso="bold", cor="#555555")
        t.texto(952, 162 + i * 27, v, tam=12.5, mono=True)

    t.retangulo(776, 316, 428, 228, fundo="#2b2b2b", borda="#2b2b2b")
    t.texto(796, 344, "Vídeo da câmera embarcada", tam=13, cor="#eeeeee")
    t.retangulo(860, 376, 180, 120, fundo="none", borda="#ff4d6d", traco=2.5)
    t.texto(860, 368, "pessoa  0,88", tam=12.5, peso="bold", cor="#ff4d6d")
    t.texto(796, 528, "[ transmissão ao vivo ]", tam=12, cor="#999999")

    t.retangulo(56, 560, 1148, 110, fundo="#ffffff", borda=BORDA)
    t.texto(76, 588, "Checklist da missão", tam=14, peso="bold")
    itens = [("espaço aéreo liberado (NOTAM e ICA 100-40)", True),
             ("bateria e enlace verificados", True),
             ("rota aprovada pelo supervisor", True),
             ("gravação em curso", True),
             ("relatório ao pousar", False)]
    x = 76
    for texto_item, feito in itens:
        t.retangulo(x, 606, 18, 18, fundo="#ffffff", borda="#555555", traco=1.6, r=3)
        if feito:
            t.linha(x + 4, y_ := 615, x + 8, 620, cor="#1e6b3a", larg=2.6)
            t.linha(x + 8, 620, x + 14, 609, cor="#1e6b3a", larg=2.6)
        t.texto(x + 26, 620, texto_item, tam=12.5)
        x += len(texto_item) * 6.6 + 54
    t.texto(76, 652, "A missão só é iniciada com o espaço aéreo liberado; a gravação "
            "integral é anexada à ocorrência.", tam=12, italico=True, cor="#555555")
    return t.salvar("fig_tela_inspecao")


if __name__ == "__main__":
    for f in (stakeholders, camadas, contexto, casos_uso, fluxo,
              tela_painel, tela_ocorrencia, tela_inspecao):
        print(f())
