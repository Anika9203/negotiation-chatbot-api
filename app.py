from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM

app = Flask(__name__)

# Load the fine-tuned model and tokenizer
model_name = "distilbert/distilgpt2"  # Update this with your model path
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

@app.route('/negotiate', methods=['POST'])
def negotiate():
    data = request.get_json()
    prompt = data['prompt']
    
    # Encode the prompt and generate a response
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    
    # Generate response
    response_ids = model.generate(input_ids, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)
    response = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
