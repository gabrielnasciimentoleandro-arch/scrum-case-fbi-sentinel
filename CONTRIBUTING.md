# Como contribuir

Contribuições que melhorem a precisão histórica, a clareza da análise ou a acessibilidade dos documentos são bem-vindas.

## Princípios editoriais

1. Priorize documentos do FBI, GAO, DOJ OIG e outras fontes primárias.
2. Diferencie fatos documentados, relatos de praticantes e interpretações.
3. Não apresente a afirmação de “90% de economia” como custo total do programa.
4. Não atribua ao Scrum resultados que também dependam de governança, contratos, equipe ou infraestrutura.
5. Cite toda informação externa e não reproduza textos sem licença e atribuição.
6. Preserve o caráter autoral e crítico do projeto.

## Validação

Antes de propor uma mudança, execute:

```bash
python scripts/validate_project.py
python -m unittest discover -s tests -v
```

Se a resenha for alterada, regenere os documentos:

```bash
python scripts/generate_deliverables.py
```
