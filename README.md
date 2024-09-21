# negotiation-chatbot-api
# Negotiation Chatbot

## Overview

This project implements a negotiation chatbot designed to simulate a negotiation process between a customer and a supplier. The chatbot utilizes sentiment analysis and predefined pricing logic to enhance the negotiation experience. It can handle multiple products, engage in back-and-forth dialogues, and generate a dataset for training.

## Project Structure
negotiation_chatbot/
│
├── dataset_generator.py        # Contains code to generate the dataset
├── negotiation_logic.py         # Contains the negotiation logic and sentiment analysis
├── train_model.py               # Contains the training code for the model
└── requirements.txt             # Contains dependencies

## Features

- **Product Listings**: The chatbot can present various products along with their descriptions and price ranges.
- **Dynamic Negotiation**: Engages in realistic negotiations by generating counteroffers based on customer input and previous offers.
- **Sentiment Analysis**: Utilizes sentiment analysis to adjust responses based on customer sentiment.
- **Custom Dataset Generation**: Automatically generates a dataset in JSON format for fine-tuning the model.
- **Model Training**: Fine-tunes a pre-trained model (DistilGPT-2) for negotiation tasks.

## Dependencies
transformers
datasets
vaderSentiment
torch
flask

