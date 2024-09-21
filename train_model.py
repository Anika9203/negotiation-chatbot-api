from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import load_dataset
from transformers import DataCollatorWithPadding

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("distilbert/distilgpt2")
model = AutoModelForCausalLM.from_pretrained("distilbert/distilgpt2")
tokenizer.pad_token = tokenizer.eos_token  # Set the padding token to the EOS token

# Load the dataset
dataset = load_dataset('json', data_files='negotiation_dataset1.json')

def preprocess_function(examples):
    return tokenizer(
        examples['customer_input'],  # Adjusting to match the correct input field
        text_target=examples['chatbot_response'],  # Adjusting to match the correct target field
        truncation=True,
        padding='max_length',  # Or use padding='longest' for dynamic padding
        max_length=64  # Adjust this to your needs
    )

# Tokenize the dataset
tokenized_dataset = dataset.map(preprocess_function, batched=True)

# Access the 'train' split and split it into train and validation
tokenized_data = tokenized_dataset['train']
split_dataset = tokenized_data.train_test_split(test_size=0.2)

# Initialize the data collator
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# Set up training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",  # Changed eval_strategy to evaluation_strategy
    learning_rate=2e-5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=3,
    weight_decay=0.01,
)

# Create the Trainer instance
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=split_dataset['train'],
    eval_dataset=split_dataset['test'],
    data_collator=data_collator
)

# Start the training
trainer.train()

