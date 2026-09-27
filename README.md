# PDF to Slides Skill

Skill para transformar PDFs e documentos de apoio em apresentações visuais, editáveis e fundamentadas nas fontes, sem pular diretamente para resumos superficiais. Quando o projeto pede, também orienta a produção e a revisão de PDFs complementares, como prévias, cadernos do aluno, diagnósticos e guias do apresentador.

O fluxo cria Markdown fiel com referências de página, dossiês por fonte, matriz de cobertura, roteiro, PPTX editável e QA visual. Para aulas gravadas, acrescenta progressão pedagógica, notas de fala, demonstração do método e controle de duração. Quando solicitado, produz HTML autocontido e PDFs complementares. Cada formato é validado separadamente.

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

Se o pedido inclui apresentação HTML, a rota opcional instala [Frontend Slides](https://github.com/zarazhangrui/frontend-slides) quando ausente, usando `--with-frontend-slides` no bootstrap. Instalações existentes não são sobrescritas automaticamente. Dependências nativas e Python exigidas por um tipo específico de PDF ou pelo renderizador são verificadas separadamente.

O redesign começa pela inspeção visual integral do deck existente e de qualquer manual de marca fornecido. O sistema de composição verifica hierarquia, grid, tipografia, contraste, diagramas, neutralidade antes de interações, ativos oficiais e direitos. Quando PPTX e prévia PDF são solicitados juntos, a prévia sai do PPTX final; fontes substituídas pelo exportador e limites de acessibilidade são registrados explicitamente.

## Estrutura

- `SKILL.md`: contrato e fluxo principal;
- `references/pdf-ingestion.md`: extração fiel, dossiês e cobertura;
- `references/presentation-workflow.md`: narrativa, Humanizer, produção visual e QA;
- `references/visual-design.md`: auditoria do deck, sistema de composição, contraste, marca e ativos;
- `references/multiformat-production.md`: PPTX nativo, HTML, PDF, fontes e paridade de exportação;
- `references/instructional-decks.md`: aulas gravadas, andragogia, storytelling e prova de conceito;
- `references/pdf-companions.md`: prévias, cadernos, diagnósticos e verificação de PDFs;
- `references/bootstrap.md`: origens e regras de instalação;
- `scripts/bootstrap_skills.py`: verificação e instalação das skills dependentes.
