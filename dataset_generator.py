import json
import random

# Sample product list
PRODUCTS = {
    "laptop": {
        "price": 1200,
        "description": "High-performance laptop with 16GB RAM and 512GB SSD.",
        "min_offer": 900,
        "max_offer": 1300
    },
    "phone": {
        "price": 800,
        "description": "Latest smartphone with excellent camera and battery life.",
        "min_offer": 600,
        "max_offer": 1000
    },
    "headphones": {
        "price": 200,
        "description": "Noise-canceling headphones with superior sound quality.",
        "min_offer": 150,
        "max_offer": 250
    },
}

# Function to generate dataset
def generate_dataset(num_samples):
    dataset = []
    for _ in range(num_samples):
        product = random.choice(list(PRODUCTS.keys()))
        product_info = PRODUCTS[product]
        
        entry = {
            "customer_input": f"I want to buy a {product}.",
            "chatbot_response": f"{product_info['description']} Price range: {product_info['min_offer']} to {product_info['max_offer']}."
        }
        
        dataset.append(entry)

        # Customer negotiation example
        customer_offer = random.randint(product_info["min_offer"], product_info["max_offer"])
        negotiation_entry = {
            "customer_input": f"No, I can offer {customer_offer}.",
            "chatbot_response": f"Great! I can accept your offer of {customer_offer}. It's a deal!"
        }
        
        dataset.append(negotiation_entry)
    
    return dataset

# Generate dataset and save to JSON
dataset = generate_dataset(10)
formatted_dataset = json.dumps(dataset, indent=4)

with open('negotiation_dataset1.json', 'w') as f:
    f.write(formatted_dataset)

print("Dataset generated and saved as 'negotiation_dataset1.json'")