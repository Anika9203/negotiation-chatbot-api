import random
import json
import re

# Sample product list
PRODUCTS = {
    "laptop": {"price": 1200, "min_offer": 900, "max_offer": 1300, "description": "High-performance laptop with 16GB RAM and 512GB SSD."},
    "phone": {"price": 800, "min_offer": 600, "max_offer": 1000, "description": "Latest smartphone with excellent camera and battery life."},
    "headphones": {"price": 200, "min_offer": 150, "max_offer": 250, "description": "Noise-canceling headphones with superior sound quality."},
}

def negotiate_price(product, customer_offer, previous_offer):
    min_offer = PRODUCTS[product]["min_offer"]
    max_offer = PRODUCTS[product]["max_offer"]

    if customer_offer < min_offer:
        return f"The offer is too low. The minimum we can accept is ${min_offer}. Try again."
    elif customer_offer >= max_offer:
        return f"Your offer is too high. The maximum we can accept is ${max_offer}."
    else:
        # Generate a counteroffer
        counter_offer = (customer_offer + max_offer) // 2
        if counter_offer > max_offer:
            counter_offer = max_offer

        # Make sure to not suggest a counteroffer lower than the customer's previous offer
        if counter_offer < previous_offer:
            counter_offer = previous_offer + 10  # Increment by a small amount

        return f"How about ${counter_offer}? Let's negotiate further."

def extract_offer(customer_input):
    offer_match = re.search(r'\b\d+\b', customer_input)
    if offer_match:
        return int(offer_match.group())
    return None

def chat_with_customer():
    print("Welcome to the Negotiation Chatbot! Type 'exit' to end the chat.")
    print("Available products:")
    for product in PRODUCTS.keys():
        print(f"- {product.capitalize()}")

    product = None
    previous_offer = 0
    while True:
        customer_input = input("Customer: ").strip().lower()
        if customer_input in ["exit", "quit"]:
            print("Chatbot: Ending the chat. Thank you!")
            break
        
        if "want to buy" in customer_input:
            for item in PRODUCTS.keys():
                if item in customer_input:
                    product = item
                    product_info = PRODUCTS[product]
                    print(f"Chatbot: {product_info['description']}")
                    print(f"Chatbot: The price range is ${product_info['min_offer']} - ${product_info['max_offer']}. What’s your offer?")
                    break
            else:
                print("Chatbot: Sorry, we don't have that product.")
        
        elif "offer" in customer_input and product:
            offer = extract_offer(customer_input)
            if offer is not None:
                response = negotiate_price(product, offer, previous_offer)
                print(f"Chatbot: {response}")
                if "final" in customer_input or "deal" in customer_input.lower():
                    print("Chatbot: Great! The final price is ${}. Thank you for your purchase!".format(offer))
                    break
                previous_offer = offer  # Update the previous offer
            else:
                print("Chatbot: Please provide a valid offer amount.")
        
        else:
            print("Chatbot: I'm here to help with your purchasing needs!")

if __name__ == "__main__":
    chat_with_customer()
