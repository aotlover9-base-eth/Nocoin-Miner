# $NOCOIN Python LLM Miner

A Python-based miner that uses LLMs (via OpenRouter) to solve cryptographic puzzles for the $NOCOIN resistance.

## Features
- **LLM Integration:** Uses OpenRouter to autonomously solve puzzles.
- **Cost Efficient:** Defaults to free models to minimize credit usage.
- **Security:** Requires a public wallet address; no private keys needed.
- **Configuration:** Simple `.env` based setup.

## Setup

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment:**
   Edit `nocoin_python_miner/.env` and add your `OPENROUTER_API_KEY`.
   You can also change the `MODEL_ID` to any model supported by OpenRouter (e.g., `google/gemini-2.0-flash-lite-preview-02-05:free`).

3. **Run the Miner:**
   ```bash
   python miner.py
   ```
   The script will prompt you for your Base ETH address upon starting.

## Mining Loop
The miner will continuously check for new puzzles. If no puzzles are available, it will sleep for 60 seconds before retrying.
