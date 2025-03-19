from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class DeepSeekProcessor:
    def __init__(self):
        self.model_name = "deepseek-ai/deepseek-moe-16b-base"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.bfloat16,
            device_map="auto",
            trust_remote_code=True  # Critical for DeepSeek models
        )

    def process_content(self, text: str):
        prompt = f"""Extract products and prices from this text:
        
        {text}
        
        Return JSON format:
        {{"products": [{{"name": "...", "price": "..."}}]}}
        """
        
        inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")
        outputs = self.model.generate(
            inputs.input_ids,
            max_new_tokens=1024,
            temperature=0.3
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
