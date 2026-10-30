# -*- coding: utf-8 -*-
"""Pequena biblioteca de desenho SVG usada nas figuras do plano de testes."""
import cairosvg

FONTE = "DejaVu Sans, Verdana, sans-serif"

CORES = {
    "azul":    ("#1f4e79", "#dce9f5"),
    "verde":   ("#1e6b3a", "#dff0e4"),
    "ocre":    ("#8a5a00", "#fbeed2"),
    "ver":     ("#9b1c31", "#fadde2"),
    "lilas":   ("#4b2e83", "#e6def7"),
    "cinza":   ("#3f3f3f", "#ebebeb"),
    "amarelo": ("#7a6500", "#fbf4cd"),
}


def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


class Tela:
    def __init__(self, w, h, fundo="#ffffff"):
        self.w, self.h = w, h
        self.p = ['<rect x="0" y="0" width="%d" height="%d" fill="%s"/>' % (w, h, fundo)]

    def add(self, s):
        self.p.append(s)

    def caixa(self, x, y, w, h, cor="azul", r=10, traco=2.2, tracejado=None, fundo=None):
        b, f = CORES[cor]
        d = ' stroke-dasharray="%s"' % tracejado if tracejado else ""
        self.add('<rect x="%g" y="%g" width="%g" height="%g" rx="%g" fill="%s" stroke="%s" '
                 'stroke-width="%g"%s/>' % (x, y, w, h, r, fundo or f, b, traco, d))

    def texto(self, x, y, t, tam=15, cor="#111111", peso="normal", anc="start",
              italico=False, mono=False):
        fam = "DejaVu Sans Mono, monospace" if mono else FONTE
        it = ' font-style="italic"' if italico else ""
        self.add('<text x="%g" y="%g" font-family="%s" font-size="%g" fill="%s" '
                 'font-weight="%s" text-anchor="%s"%s>%s</text>'
                 % (x, y, fam, tam, cor, peso, anc, it, esc(t)))

    def paragrafo(self, x, y, linhas, tam=14, cor="#222222", dy=19, anc="start", peso="normal"):
        for i, l in enumerate(linhas):
            self.texto(x, y + i * dy, l, tam=tam, cor=cor, anc=anc, peso=peso)

    def seta(self, x1, y1, x2, y2, cor="#444444", larg=2.4, cab=9):
        self.add('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" stroke-width="%g" '
                 'marker-end="url(#pf)"/>' % (x1, y1, x2, y2, cor, larg))

    def poligono(self, pts, cor="azul", traco=2.2):
        b, f = CORES[cor]
        s = " ".join("%g,%g" % p for p in pts)
        self.add('<polygon points="%s" fill="%s" stroke="%s" stroke-width="%g"/>' % (s, f, b, traco))

    def circulo(self, cx, cy, r, cor="azul", traco=2.0, fundo=None):
        b, f = CORES[cor]
        self.add('<circle cx="%g" cy="%g" r="%g" fill="%s" stroke="%s" '
                 'stroke-width="%g"/>' % (cx, cy, r, fundo or f, b, traco))

    def losango(self, cx, cy, w, h, cor="amarelo", traco=2.0):
        b, f = CORES[cor]
        pts = "%g,%g %g,%g %g,%g %g,%g" % (cx, cy - h / 2, cx + w / 2, cy,
                                           cx, cy + h / 2, cx - w / 2, cy)
        self.add('<polygon points="%s" fill="%s" stroke="%s" stroke-width="%g"/>'
                 % (pts, f, b, traco))

    def linha(self, x1, y1, x2, y2, cor="#666666", larg=1.6, tracejado=None):
        d = ' stroke-dasharray="%s"' % tracejado if tracejado else ""
        self.add('<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="%s" '
                 'stroke-width="%g"%s/>' % (x1, y1, x2, y2, cor, larg, d))

    def retangulo(self, x, y, w, h, fundo="#ffffff", borda="#999999",
                  traco=1.4, r=4, tracejado=None):
        d = ' stroke-dasharray="%s"' % tracejado if tracejado else ""
        self.add('<rect x="%g" y="%g" width="%g" height="%g" rx="%g" fill="%s" '
                 'stroke="%s" stroke-width="%g"%s/>' % (x, y, w, h, r, fundo,
                                                        borda, traco, d))

    def salvar(self, nome, escala=2.4):
        cab = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
               'viewBox="0 0 %d %d">' % (self.w, self.h, self.w, self.h))
        defs = ('<defs><marker id="pf" markerWidth="10" markerHeight="10" refX="9" refY="3.2" '
                'orient="auto"><path d="M0,0 L9,3.2 L0,6.4 z" fill="#444444"/></marker></defs>')
        svg = cab + defs + "".join(self.p) + "</svg>"
        with open(nome + ".svg", "w", encoding="utf-8") as f:
            f.write(svg)
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=nome + ".png",
                         output_width=int(self.w * escala), output_height=int(self.h * escala))
        return nome + ".png"
