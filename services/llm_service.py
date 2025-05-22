from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os
from dotenv import load_dotenv

load_dotenv() 

LOCAL_MODEL= os.getenv(key="LOCAL_MODEL")

class LLMService:

    def __init__(self, model_name=LOCAL_MODEL, max_length=50, no_repeat_ngram_size=2):
       
        self.model_name = model_name
        self.max_length = max_length
        self.no_repeat_ngram_size = no_repeat_ngram_size
        self.model, self.tokenizer = self.load_model()

    def load_model(self):

        """
        Loads the model and its tokenizer from the Hugging Face Hub.
        
        Returns:
        tuple: Loaded model and tokenizer.
        """
        try:
            model = AutoModelForCausalLM.from_pretrained(self.model_name)
            model.eval()
            tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            return model, tokenizer
        
        except Exception as e:
            raise RuntimeError(f"Error loading the model and tokenizer: {str(e)}")

    def generate(self, message : str):
       
        try:
            inputs = self.tokenizer.encode(
                message,
                return_tensors="pt",
            )

            with torch.no_grad():
                
                outputs = self.model.generate(
                    inputs,
                    max_length=self.max_length,
                    num_return_sequences=1,
                    no_repeat_ngram_size=self.no_repeat_ngram_size
                )

            response = self.tokenizer.decode(
                outputs[0],
                skip_special_tokens=True,
                clean_up_tokenization_spaces=True
            )

            return response

        except Exception as e:
            raise RuntimeError(f"Error generating a response: {str(e)}")