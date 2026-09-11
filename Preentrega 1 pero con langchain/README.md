# Cliente de LLM robusto y asíncrono
Este es un ejemplo de :
Pre-entrega 1 — Módulo 1, AI Engineering (Coderhouse).
pero usando langchain para simplificar el codeo, lo que antes se hacia en varios archivos ahora lo puedes sintetizar en 1 sola funcion main.py

# Requisitos

- Python 3.12+
- Una API key de OpenAI y/o de Anthropic

# Instalación

```bash
python3.12 -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

# Variables de entorno

copiá `.env.example` a `.env` y completá tus claves reales:

```bash
cp .env.example .env
```

| Variable             | Descripción                                              | Obligatoria | 
|----------------------|-----------------------------------------------------------|-------------|
| `OPENAI_API_KEY`     | Tu API key de OpenAI                                       | Si usás `LLM_PROVIDER=openai` |
| `ANTHROPIC_API_KEY`  | Tu API key de Anthropic                                     | Si usás `LLM_PROVIDER=anthropic` |
| `LLM_PROVIDER`       | Qué proveedor usa `main.py` por defecto: `openai` o `anthropic` | No (default: `openai`) |

**Importante:** `.env` nunca se sube al repositorio (está en `.gitignore`).
Solo se versiona `.env.example`, sin claves reales.
