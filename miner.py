import os
import time
import requests
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_ID = os.getenv("MODEL_ID", "google/gemini-2.0-flash-lite-preview-02-05:free")
NOCOIN_API_KEY = os.getenv("NOCOIN_API_KEY")
NOCOIN_BASE_URL = os.getenv("NOCOIN_BASE_URL")

# Initialize OpenAI client for OpenRouter
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=OPENROUTER_API_KEY,
)

def get_llm_answer(prompt):
    """Solve the puzzle using LLM via OpenRouter."""
    print(f"Solving with {MODEL_ID}...")
    try:
        completion = client.chat.completions.create(
          model=MODEL_ID,
          messages=[
            {
              "role": "system",
              "content": (
                  "You are a cryptographic solver for the $NOCOIN resistance. "
                  "Provide the canonical answer to the puzzle. "
                  "The answer must be lowercase, trimmed, and single-spaced. "
                  "Provide ONLY the final answer, no explanation."
              )
            },
            {
              "role": "user",
              "content": f"Puzzle: {prompt}"
            }
          ]
        )
        answer = completion.choices[0].message.content.strip().lower()
        # Clean up any potential '0x' prefix if LLM includes it unnecessarily for numeric/hex
        if "0x" in answer and len(answer) > 2 and prompt.lower().find("0x") == -1:
             # Basic heuristic: if prompt asks for 'starts with which 6 hex chars'
             pass 
        return answer
    except Exception as e:
        print(f"LLM Error: {e}")
        return None

def fetch_puzzle(eth_address):
    """Pull an unsolved puzzle from the $NOCOIN API."""
    try:
        response = requests.get(
            f"{NOCOIN_BASE_URL}?eth={eth_address}",
            headers={"apikey": NOCOIN_API_KEY}
        )
        if response.status_code == 200:
            return response.json().get("puzzle")
        else:
            print(f"API Error ({response.status_code}): {response.text}")
            return None
    except Exception as e:
        print(f"Fetch Error: {e}")
        return None

def submit_solution(eth_address, puzzle_id, answer):
    """Submit the solution to the $NOCOIN API."""
    try:
        payload = {
            "eth_address": eth_address,
            "agent_name": "Python-LLM-Miner",
            "puzzle_id": puzzle_id,
            "answer": answer
        }
        response = requests.post(
            NOCOIN_BASE_URL,
            headers={
                "apikey": NOCOIN_API_KEY,
                "Content-Type": "application/json"
            },
            json=payload
        )
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Submit Error ({response.status_code}): {response.text}")
            return None
    except Exception as e:
        print(f"Submission Error: {e}")
        return None

def main():
    print("=== $NOCOIN Python LLM Miner ===")
    eth_address = input("Enter your Base ETH Address (0x...): ").strip()
    
    if not eth_address.startswith("0x"):
        print("Invalid ETH address format.")
        return

    if not OPENROUTER_API_KEY or OPENROUTER_API_KEY == "your_key_here":
        print("Error: Please set your OPENROUTER_API_KEY in the .env file.")
        return

    print(f"Target Wallet: {eth_address}")
    print(f"Using Model: {MODEL_ID}")
    print("Starting mining loop...")

    while True:
        print("\nFetching next puzzle...")
        puzzle = fetch_puzzle(eth_address)

        if not puzzle:
            print("No puzzles available or all solved. Sleeping for 60 seconds...")
            time.sleep(60)
            continue

        print(f"Puzzle Found: {puzzle['prompt']}")
        print(f"Category: {puzzle['category']} | Reward: {puzzle['reward']} $NTC")

        answer = get_llm_answer(puzzle['prompt'])
        
        if answer:
            print(f"Submitting Answer: '{answer}'")
            result = submit_solution(eth_address, puzzle['id'], answer)
            
            if result and result.get("correct"):
                print(f"SUCCESS! Reward: {result['reward']} $NTC | New Balance: {result['balance']}")
            else:
                print(f"FAILED: Incorrect answer. Result: {result}")
        else:
            print("Skipping puzzle due to LLM error.")
        
        # Anti-spam delay
        time.sleep(2)

if __name__ == "__main__":
    main()
