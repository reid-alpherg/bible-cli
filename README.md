# bible-cli

CLI to query Bible texts from multiple Portuguese translations.

## Installation

```bash
pip install bible-cli
```

## Usage

### Query a verse

```bash
bible-cli query "[book] [chapter]:[verse] [translation]"
```

### Examples

Single verse:
```bash
bible-cli query "João 3:16"
```

Verse range:
```bash
bible-cli query "Eclesiastes 3:15-16"
```

Specifying a translation:
```bash
bible-cli query "Gênesis 1:1 NVI"
```

## Available translations

| Code  | Description |
|-------|-------------|
| ACF   | Almeida Corrigida Fiel (default) |
| ARA   | Almeida Revista e Atualizada |
| ARC   | Almeida Revista e Corrigida |
| AS21  | Almeida Século 21 |
| JFAA  | João Ferreira de Almeida Atualizada |
| KJA   | King James Atualizada |
| KJF   | King James Fiel |
| NAA   | Nova Almeida Atualizada |
| NBV   | Nova Bíblia Viva |
| NTLH  | Nova Tradução na Linguagem de Hoje |
| NVI   | Nova Versão Internacional |
| NVT   | Nova Versão Transformadora |
| TB    | Tradução Brasileira |

> The default translation is **ACF** when none is specified.

## Query format

```
[book] [chapter]:[start verse]-[end verse] [translation]
```

- `translation` is optional
- `end verse` is optional (for ranges)

---

## CLI usage

After installing, the `bible-cli` command is available in the terminal.

```bash
# Single verse
bible-cli query "Salmos 23:1"

# Verse range
bible-cli query "Salmos 23:1-3"

# With a specific translation
bible-cli query "Salmos 23:1 NVI"

# App info
bible-cli about
```

---

## Python module usage

`QueryProcessor` is the main interface for programmatic use.

```python
from bible_cli import QueryProcessor

processor = QueryProcessor()

# Single verse
text = processor.process_query("João 3:16")
print(text)

# Verse range
text = processor.process_query("Gênesis 1:1-3")
print(text)

# With a specific translation
text = processor.process_query("Romanos 8:28 ARA")
print(text)
```

`process_query` returns a `str` with the formatted verses, or `None` if no verses are found.
