# ARGOS — Sprint 1 · Documento de Visão

**Análise de Risco e Guarda Operacional por Sensoriamento**

Entrega da **Sprint 1** do *Sentinela Nuclear Challenge*, proposto pela **AMAZUL —
Amazônia Azul Tecnologias de Defesa S.A.**, na disciplina de **Software Engineering**
da FIAP.

| | |
|---|---|
| **Turma** | 2CCPS — Ciência da Computação |
| **Grupo** | NextGen |
| **Professor** | Leandro Ramos da Silva |
| **Entrega** | Documento de Visão e Definição da Solução |
| **Versão** | 1.0 — 30/10/2026 |

## Integrantes

| Nome | RM | Atribuição nesta Sprint |
|---|---|---|
| Gustavo Franzoti Gonçalves | RM566983 | Análise do contexto e mapeamento de stakeholders |
| Lincoln Simão Pereira | RM567284 | Definição da solução, arquitetura conceitual e repositório |
| Maykon Santana Fonseca | RM567041 | Escopo, requisitos iniciais e matriz de rastreabilidade |
| Nicolas Sakaue Nishimura | RM567752 | Protótipo conceitual e fluxo de utilização |

## O desafio

> Como utilizar drones, sensores, visão computacional e Inteligência Artificial para
> monitorar, inspecionar e identificar situações anômalas em ambientes críticos
> relacionados à segurança física de instalações nucleares?

## A proposta em uma frase

O **ARGOS** reúne sensores IoT, câmeras com visão computacional na borda e drones
autônomos, correlaciona essas fontes por Inteligência Artificial e entrega ao
operador **eventos já triados, classificados por risco e georreferenciados** — em vez
de dezenas de imagens para vigiar. A decisão final permanece humana e cada ação fica
registrada em trilha auditável.

O problema atacado é de **tempo e atenção**: a proteção física só é efetiva se
*detecção + resposta* couber dentro do tempo que as barreiras físicas concedem, e o
elo frágil hoje é a detecção dependente de atenção humana sustentada.

## Entregável

📄 **[docs/Sprint1_Documento_de_Visao_ARGOS.pdf](docs/Sprint1_Documento_de_Visao_ARGOS.pdf)**
— documento completo em ABNT (30 páginas, 8 figuras, 11 tabelas), contendo:

1. Introdução
2. Contexto do Problema
3. Objetivos da Solução
4. Stakeholders
5. Descrição da Solução Proposta
6. Benefícios Esperados
7. Escopo (dentro e fora)
8. Protótipo Conceitual
9. Conclusão
10. Referências · Apêndice A — Matriz de rastreabilidade

## Estrutura do repositório

```
sprint01_SE/
├── docs/          documento de visão em PDF (entregável da Sprint)
├── prototipo/     protótipo conceitual de baixa fidelidade
├── diagramas/     diagramas de apoio (C4, casos de uso, camadas, stakeholders)
└── src-doc/       fontes: LaTeX do documento e scripts que geram as figuras
```

## Protótipo conceitual

| Tela | Pergunta que responde |
|---|---|
| [Painel operacional](prototipo/01_painel_operacional.png) | O que está acontecendo agora? |
| [Verificação da ocorrência](prototipo/02_verificacao_ocorrencia.png) | O que é isto, exatamente? |
| [Inspeção aérea](prototipo/03_inspecao_aerea.png) | O que o drone está vendo? |
| [Fluxo de utilização](prototipo/04_fluxo_de_uso.png) | Do evento captado ao registro da ocorrência |

Baixa fidelidade, por definição: o protótipo valida o fluxo de trabalho, não o
acabamento visual.

## Diagramas

| Diagrama | Conteúdo |
|---|---|
| [Contexto (C4 — nível 1)](diagramas/contexto_c4.png) | Quem usa o ARGOS e com que sistemas ele conversa |
| [Arquitetura em camadas](diagramas/arquitetura_camadas.png) | Borda → Plataforma → Apresentação; dados → informação → inteligência → ação |
| [Casos de uso](diagramas/casos_de_uso.png) | Visão preliminar dos casos de uso e atores |
| [Matriz de stakeholders](diagramas/matriz_stakeholders.png) | Influência × interesse |

## Escopo em uma olhada

**Dentro:** monitorar perímetro e áreas restritas; detectar intrusão, permanência
indevida, objeto abandonado e violação de barreira; correlacionar fontes e
classificar severidade; alertas automáticos; painel operacional com mapa; despacho de
drone para verificação; inspeção programada; registro auditável; monitoração da saúde
do próprio sistema.

**Fora:** segurança nuclear do processo (*safety*); resposta automática sem
intervenção humana; identificação biométrica e reconhecimento facial; substituição do
controle de acesso; contramedidas ativas contra drones; fabricação de hardware.

## Como reconstruir o PDF

Requer `pdflatex` (TeX Live), `python3` e `cairosvg`.

```bash
cd src-doc
pip install cairosvg
python3 figuras.py          # gera os .png a partir dos .svg
pdflatex principal.tex
pdflatex principal.tex      # segunda passada: sumário e referências cruzadas
```

## Próximos passos (Sprint 2)

- Detalhar os casos de uso com fluxos principal e alternativos
- Produzir o modelo de domínio e os diagramas C4 de contêineres e componentes
- Avaliar a viabilidade dos modelos de visão computacional na borda
- Especificar as interfaces de integração com CFTV, controle de acesso e sensores
- Validar o protótipo com quem exerce, na prática, o papel de operador

## Observação sobre os dados

O grupo não teve acesso a dados operacionais reais de nenhuma instalação da AMAZUL.
Os valores apresentados como linha de base são **estimativas da equipe**, construídas
a partir de literatura pública e do enunciado do desafio, e estão identificados como
tal no documento. Nenhum deles deve ser lido como medição.
