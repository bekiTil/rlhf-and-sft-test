import os
import torch
import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM
from prompts import build_prompt

HF_MODEL_ID = os.environ.get("HF_MODEL_ID", "BekiTila/bitext-dpo-tinyllama-support")

tokenizer = AutoTokenizer.from_pretrained(HF_MODEL_ID, use_fast=True)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    HF_MODEL_ID,
    device_map="auto",
    dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
)
model.eval()


def _normalize_history(history):
    """
    Normalize Gradio chat history into list of (user, assistant) tuples.
    Handles multiple Gradio formats.
    """
    if not history:
        return []

    # Format A: list of dict messages: {"role": "user"/"assistant", "content": "..."}
    if isinstance(history[0], dict) and "role" in history[0]:
        pairs = []
        pending_user = None
        for m in history:
            role = m.get("role")
            content = m.get("content", "")
            if role == "user":
                pending_user = content
            elif role == "assistant" and pending_user is not None:
                pairs.append((pending_user, content))
                pending_user = None
        return pairs

    # Format B: list of dict pairs: {"user": "...", "assistant": "..."}
    if isinstance(history[0], dict) and ("user" in history[0] or "assistant" in history[0]):
        return [(h.get("user", ""), h.get("assistant", "")) for h in history]

    # Format C: list of [user, assistant] or (user, assistant)
    pairs = []
    for h in history:
        try:
            pairs.append((h[0], h[1]))
        except Exception:
            pass
    return pairs


@torch.inference_mode()
def respond(message, history):
    hist = _normalize_history(history)
    prompt = build_prompt(message, hist)

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    out = model.generate(
        **inputs,
        max_new_tokens=256,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.1,
        pad_token_id=tokenizer.eos_token_id,
    )

    full = tokenizer.decode(out[0], skip_special_tokens=True)

    # Return only the final assistant part
    if "### Assistant:" in full:
        answer = full.split("### Assistant:")[-1].strip()
    else:
        # fallback if formatting differs
        answer = full.strip()

    return answer


demo = gr.ChatInterface(
    fn=respond,
    title="Customer Support Assistant (HF Model)",
    description="A helpful customer support assistant fine-tuned on support conversations.",
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
