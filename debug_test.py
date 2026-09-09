from src.ingestion.loaders import load_filing

record = load_filing("data/raw/sec-edgar-filings/CRM/10-K/0001108524-26-000060/full-submission.txt")
text = record["text"]

idx = text.find("Total stockholders")
print(text[idx-1500:idx+300])