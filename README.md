# ⛏️ $NOCOIN Python LLM Miner

Welcome to the **$NOCOIN Miner**. This is a Python-based automation tool that helps you mine $NOCOIN rewards by solving cryptographic and blockchain puzzles using AI (LLMs).

It uses **OpenRouter** to connect to the cheapest and most efficient AI models (like Gemini 2.0 Flash) to solve challenges autonomously.

---

## 🚀 Quick Start Guide

### 1. Prerequisites
Before you start, you will need:
*   **Python 3.8+** installed on your system.
*   **A Base EVM Wallet Address:** Your public wallet address (e.g., `0x123...`) where you want to receive rewards. No private key is required!
*   **OpenRouter API Key:** 
    1.  Go to [OpenRouter.ai](https://openrouter.ai/).
    2.  Create an account and generate an **API Key**.
    3.  (Optional) Add a small amount of credit (e.g., $1-$5) if you want to use paid models, though free models are supported.

### 2. Installation

Clone the repository and install the required dependencies:

```bash
# Clone the repo
git clone https://github.com/aotlover9-base-eth/Nocoin-Miner.git

# Enter the directory
cd Nocoin-Miner

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

You need to tell the miner which API key and model to use.

1.  Create a new file named `.env` in the root folder.
2.  Open it in a text editor and add the following lines:

```text
OPENROUTER_API_KEY=your_openrouter_key_here
MODEL_ID=google/gemini-2.0-flash-lite-preview-02-05:free
```

*Note: The `MODEL_ID` above is a free/very cheap model. You can change it to any model listed on OpenRouter.*

### 4. Start Mining

Run the script:

```bash
python miner.py
```

**What happens next?**
1.  The script will ask for your **Base ETH Address**. Paste it and hit Enter.
2.  It will connect to the $NOCOIN server and fetch an unsolved puzzle.
3.  The AI will solve the puzzle and submit the answer automatically.
4.  If correct, your $NTC balance will increase instantly!
5.  If no puzzles are left, it will wait for 60 seconds and check again.

---

## 🛡️ Security
*   **No Private Keys:** This miner **NEVER** asks for your seed phrase or private key. It only needs your public address to attribute rewards to you.
*   **Environment Safety:** Your API keys are stored in the `.env` file, which is ignored by Git to prevent accidental leaks.

## 💰 Rewards
You can track your earnings and "Claim" them to your on-chain wallet by visiting the official dashboard at [nocoin.live](https://www.nocoin.live/).

---
*Developed for the $NOCOIN Resistance.*
