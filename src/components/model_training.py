import pandas as pd
from src.logger import logging
from src.entity import ModelTrainerConfig
from src.utils.common import data_object, tokenize_data
import torch
from torch.utils.data import DataLoader
from transformers import (
    AutoModelForSequenceClassification, 
    AdamW, 
    get_scheduler
)
from tqdm.auto import tqdm

class ModelTrainer:
    def __init__(self, train_data_path, valid_data_path, config: ModelTrainerConfig):
        self.train_texts_path = train_data_path
        self.valid_texts_path = valid_data_path
        self.config = config


    def train_model(self):
        train_df = pd.read_csv(self.train_texts_path)
        valid_df = pd.read_csv(self.valid_texts_path)

        data = data_object(train_df.iloc[0:9, :], valid_df.iloc[0:9, :])

        data_collator, tokenized_data = tokenize_data(data, self.config.model_ckpt)

        # define dataloaders for further process
        train_dataloader = DataLoader(
            tokenized_data["train"], shuffle=True, batch_size=self.config.train_batch_size, collate_fn=data_collator
        )
        eval_dataloader = DataLoader(
            tokenized_data["validation"], batch_size=self.config.train_batch_size, collate_fn=data_collator
        )

        for batch in train_dataloader:
            break
        {k: v.shape for k, v in batch.items()}

        # instantiate classification model 
        model = AutoModelForSequenceClassification.from_pretrained(self.config.model_ckpt, num_labels = self.config.num_labels)
        # Add optimizer in model and learning rate
        print(type(self.config.learning_rate))
        optimizer = AdamW(model.parameters(), lr=float(self.config.learning_rate))
        # set epochs, training steps and scheduler
        num_epochs = self.config.num_train_epochs
        num_training_steps = num_epochs * len(train_dataloader)
        lr_scheduler = get_scheduler(
            "linear",
        optimizer=optimizer,
        num_warmup_steps=self.config.num_warmup_steps,
        num_training_steps=num_training_steps,
        )

        # set hardware for model training
        device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
        model.to(device)
        device

        # training loop 
        # shows progress of training
        progress_bar = tqdm(range(num_training_steps))
        model.train()

        for epoch in range(num_epochs):
            for batch in train_dataloader:
                batch = {k: v.to(device) for k, v in batch.items()}
                outputs = model(**batch)
                loss = outputs.loss
                loss.backward()

                optimizer.step()
                lr_scheduler.step()
                optimizer.zero_grad()
                progress_bar.update(1)

        model_save_path = self.config.trained_model_dir
        model.save_pretrained(model_save_path)