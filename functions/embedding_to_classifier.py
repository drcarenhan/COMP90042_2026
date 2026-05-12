import torch
import numpy as np
import transformers as ppb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

"""look at jupyter notebook for more details on inputs and outputs
run this outside function and pass it in as frozen_bert so that llm doesnt have 
to load everytime:
model_class, pretrained_weights = (ppb.DistilBertModel, 'distilbert-base-uncased')
my_frozen_bert = model_class.from_pretrained(pretrained_weights)"""
def train_embedding_classifier(input_ids, attention_mask, labels, test_size=0.2, random_state=42, frozen_bert=None):
    """
    Takes tokenized inputs and labels, extracts DistilBERT embeddings, 
    and trains a Logistic Regression classifier.
    """
    if frozen_bert is None:
        print("No model provided. Loading DistilBERT model...")
        model_class, pretrained_weights = (ppb.DistilBertModel, 'distilbert-base-uncased')
        frozen_bert = model_class.from_pretrained(pretrained_weights)
    else:
        print("Using provided DistilBERT model...")

    print("Generating embeddings (this may take a moment)...")
    with torch.no_grad():
        output_embeddings = frozen_bert(input_ids, attention_mask=attention_mask)
        
    # Extract features for classification ([CLS] tokens) and convert to numpy
    features = output_embeddings[0][:, 0, :].numpy()
    
    print("Splitting data and training classifier...")
    # Splitting the data
    train_features, test_features, train_labels, test_labels = train_test_split(
        features, labels, test_size=test_size, random_state=random_state
    )
    
    # Initialize and train the Logistic Regression model
    classifier = LogisticRegression(max_iter=1000)
    classifier.fit(train_features, train_labels)
    
    # Optional: print out a quick accuracy score on the test split
    score = classifier.score(test_features, test_labels)
    print(f"Training complete! Test split accuracy: {score:.4f}")
    
    return classifier