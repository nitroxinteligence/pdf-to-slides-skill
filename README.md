# PDF to Slides Skill

Skill para transformar um ou mais PDFs em uma apresentação visual, editável e fundamentada nas fontes, sem pular diretamente para resumos superficiais.

O fluxo cria Markdown fiel com referências de página, dossiês por fonte, matriz de cobertura, roteiro, texto humanizado, PPTX e QA visual.

## Instalação

```bash
npx --yes skills add nitroxinteligence/pdf-to-slides-skill \
  --global --agent codex --skill pdf-to-slides --yes --copy
```

Depois da instalação, inicie uma nova sessão do Codex e peça para usar `pdf-to-slides` com os PDFs anexados.

Na primeira execução, a skill instala automaticamente, quando ausentes:

- [Book-to-Skill](https://github.com/virgiliojr94/book-to-skill);
- [Humanizer](https://github.com/blader/humanizer);
- [PPT Master](https://github.com/hugohe3/ppt-master).

Instalações existentes não são sobrescritas automaticamente. Dependências nativas e Python exigidas por um tipo específico de PDF ou pelo renderizador são verificadas separadamente.

## Estrutura

- `SKILL.md`: contrato e fluxo principal;
- `references/pdf-ingestion.md`: extração fiel, dossiês e cobertura;
- `references/presentation-workflow.md`: narrativa, Humanizer, produção visual e QA;
- `references/bootstrap.md`: origens e regras de instalação;
- `scripts/bootstrap_skills.py`: verificação e instalação das skills dependentes.

