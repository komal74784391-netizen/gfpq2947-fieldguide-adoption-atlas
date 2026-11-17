# Field Guide — adoption atlas

Source of the public Field Guide site and the adoption tracker for the research group.

## Layout

- `site/` — everything that is rendered and published.
- `tools/` — maintenance scripts.

## Registry tables

The adoption table rendered by `site/pages/adopted.md` is not written by hand.  It is built
from the row sheet in `tools/adoption_rows.tsv`:

```bash
python tools/build_tool_index.py --rows tools/adoption_rows.tsv --out site/_data/adopted_tools
```

Each row becomes one data file under `site/_data/adopted_tools/`, which the templates iterate
as `site.data.adopted_tools`.  Placeholder rows in the sheet are skipped by the generator.

## Adoption workflow

1. Review the work and its upstream reproductions.
2. Record the decision in the issue tracker.
3. Update the published catalogue.
4. Rebuild the registry data files and commit.

Do not hand-edit generated data files; they are rewritten by the generator.
