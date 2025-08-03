import torch
from torch import nn, Tensor, LongTensor
from torch.utils.data import Dataset, DataLoader
from torch.optim import Adam

from transformers import PreTrainedTokenizer

from typing import Literal

# 구현하세요!
class CBOWDataset(Dataset):
    def __init__(self, token_ids: list[int], window_size: int):
        self.data = []
        for i in range(window_size, len(token_ids) - window_size):
            context = token_ids[i - window_size:i] + token_ids[i + 1:i + window_size + 1]
            target = token_ids[i]
            self.data.append((context, target))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        context, target = self.data[idx]
        return torch.tensor(context, dtype=torch.long), torch.tensor(target, dtype=torch.long)


class SkipGramDataset(Dataset):
    def __init__(self, token_ids: list[int], window_size: int):
        self.data = []
        for i in range(window_size, len(token_ids) - window_size):
            target = token_ids[i]
            for j in range(-window_size, window_size + 1):
                if j == 0:
                    continue
                context = token_ids[i + j]
                self.data.append((target, context))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        target, context = self.data[idx]
        return torch.tensor(target, dtype=torch.long), torch.tensor(context, dtype=torch.long)

class Word2Vec(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        d_model: int,
        window_size: int,
        method: Literal["cbow", "skipgram"]
    ) -> None:
        super().__init__()
        self.vocab_size = vocab_size
        self.d_model = d_model
        self.embeddings = nn.Embedding(vocab_size, d_model)
        self.weight = nn.Linear(d_model, vocab_size, bias=False)
        self.window_size = window_size
        self.method = method
        # 구현하세요!
        

    def embeddings_weight(self) -> Tensor:
        return self.embeddings.weight.detach()

    def fit(
        self,
        corpus: list[str],
        tokenizer: PreTrainedTokenizer,
        lr: float,
        num_epochs: int,
        batch_size: int = 128
    ) -> None:
        criterion = nn.CrossEntropyLoss()
        optimizer = Adam(self.parameters(), lr=lr)
        # 구현하세요!
        token_ids: list[int] = tokenizer.convert_tokens_to_ids(corpus)
        token_ids = [t for t in token_ids if t != tokenizer.pad_token_id]
        
        print(f"[디버깅] 원래 token 개수: {len(token_ids)} → 1000개로 제한")
        
        
        if self.method == "cbow":
            dataset = CBOWDataset(token_ids, self.window_size)
            self._train_cbow(dataset, lr, num_epochs, batch_size)

        elif self.method == "skipgram":
            dataset = SkipGramDataset(token_ids, self.window_size)
            self._train_skipgram(dataset, lr, num_epochs, batch_size)


    def _train_cbow(
        self,
        dataset: Dataset,
        lr: float,
        num_epochs: int,
        batch_size: int
        # 구현하세요!
    ) -> None:
        # 구현하세요!
        dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
        criterion = nn.CrossEntropyLoss()
        optimizer = Adam(self.parameters(), lr=lr)
        device = next(self.parameters()).device
    
        for epoch in range(num_epochs):
            total_loss = 0.0
            print(f"[CBOW] Epoch {epoch + 1}/{num_epochs}")
            for contexts, targets in dataloader:
                contexts = contexts.to(device)  
                targets = targets.to(device)

                optimizer.zero_grad()
                emb = self.embeddings(contexts)      
                emb_mean = emb.mean(dim=1)            
                logits = self.weight(emb_mean)      
                loss = criterion(logits, targets)
                loss.backward()
                optimizer.step()

                total_loss += loss.item()
            print(f"  Loss: {total_loss:.4f}")


    def _train_skipgram(
        self,
        dataset: Dataset,
        lr: float,
        num_epochs: int,
        batch_size: int
        # 구현하세요!
    ) -> None:
        dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
        criterion = nn.CrossEntropyLoss()
        optimizer = Adam(self.parameters(), lr=lr)
        device = next(self.parameters()).device
    
        for epoch in range(num_epochs):
            total_loss = 0.0
            print(f"[Skip-gram] Epoch {epoch + 1}/{num_epochs}")
            for targets, contexts in dataloader:
                targets = targets.to(device)
                contexts = contexts.to(device)

                optimizer.zero_grad()
                emb = self.embeddings(targets)      
                logits = self.weight(emb)            
                loss = criterion(logits, contexts)
                loss.backward()
                optimizer.step()

                total_loss += loss.item()
            print(f"  Loss: {total_loss:.4f}")
