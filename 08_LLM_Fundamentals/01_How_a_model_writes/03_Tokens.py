"""
===============================================================================
                       TOKENS IN LLMs — FROM THE BASICS
===============================================================================

Key Takeaway:
Large Language Models (LLMs) do not directly process text as ordinary words. 
A tokenizer converts text into tokens, and each token is represented by a 
unique numerical identifier called a Token ID.

-------------------------------------------------------------------------------
1. WHAT IS A TOKEN?
-------------------------------------------------------------------------------
A token is a small piece of text that a language model processes. A token can be:
  - A complete word       : "hello"
  - Part of a word        : "un", "sub", "scribing"
  - Punctuation marks     : "?", "!", "."
  - Text with leading space: " how"

Note: 1 Word != 1 Token. Token counts vary based on the tokenizer's rules.

Example:
  Input Text : "hi how are you?"
  Tokens     : ['hi', ' how', ' are', ' you', '?']  (Total: 5 tokens)
  *Notice: " how", " are", and " you" include their leading spaces.

-------------------------------------------------------------------------------
2. TOKENIZER vs. TOKEN ID
-------------------------------------------------------------------------------
  - Tokenizer : The tool/algorithm that splits raw text into tokens and maps 
                them to numerical identifiers.
  - Token ID  : The unique integer index assigned to a specific token within 
                the tokenizer's vocabulary dictionary.

Mapping Example (Illustrative IDs):
  Token  | Token ID
  -------+---------
  "hi"   | 101
  " how" | 205
  " are" | 309
  " you" | 412
  "?"    | 27

Execution Flow:
  Raw Text   -->  "hi how are you?"
  Tokenizer  -->  ['hi', ' how', ' are', ' you', '?']
  Token IDs  -->  [101, 205, 309, 412, 27]
  Model Input-->  Embeddings -> Neural Network Layers -> Output

Important:
  Token IDs are strictly identifiers/indices in a vocabulary dictionary. 
  The structural semantic meaning is learned downstream through numerical 
  vectors called Embeddings inside the model.
===============================================================================
"""
import tiktoken
# encoding is a variable holding the tokenizer encoding object.
# The model processes these token IDs through its numerical representations, called embeddings
encoding = tiktoken.get_encoding("o200k_harmony")
ids = encoding.encode("Value of plank constant")
print(ids)
print([encoding.decode([i]) for i in ids])
print(f"There are {len(ids)} tokens")
for text in [
    "refund",
    "unsubscribing",
    "My parcel has not arrived",
    "मेरा पार्सल नहीं आया"
]:
    ids = encoding.encode(text)
    print(len(ids), [encoding.decode([i]) for i in ids])

print(encoding.n_vocab)

# - encoding is the tokenizer object.
# - .encode() is a method that converts text into token IDs.
# - "hi how are you?" is the input string.
# - ids stores the resulting list of integers.
