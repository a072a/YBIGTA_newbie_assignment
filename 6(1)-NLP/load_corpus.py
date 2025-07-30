# 구현하세요!
from datasets import load_dataset

def load_corpus() -> list[str]:
    corpus: list[str] = []
    # 구현하세요!
    dataset = load_dataset("google-research-datasets/poem_sentiment")

    for split in ["train", "validation", "test"]:
        for item in dataset[split]:
            text = item["verse_text"]
            words = text.split(" ")
            corpus += words
    
    corpus = corpus[:7000]
    return corpus