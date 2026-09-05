# Hybrid Rag Benchmark

A benchmark suite for comparing dense, sparse, and hybrid retrieval strategies in RAG pipelines — measuring retrieval quality (recall@k, MRR), answer accuracy, and latency tradeoffs with cross-encoder reranking and traceable citations.

Most RAG projects assume hybrid retrieval + reranking is "better" and ship it without checking. This project measures it instead: comparing dense-only, sparse-only (BM25), hybrid, and hybrid+reranked retrieval head to head on a custom benchmark, so the gains (or lack of them) are backed by numbers, not vibes.

## Results

> _Populate this after running `scripts/run_benchmark.py`. Lead with the headline numbers._

| Strategy            | Recall@5 | MRR  | Answer Accuracy | Avg Latency (ms) |
|----------------------|----------|------|------------------|-------------------|
| Dense only           | –        | –    | –                | –                 |
| BM25 only            | –        | –    | –                | –                 |
| Hybrid (RRF)         | –        | –    | –                | –                 |
| Hybrid + Reranked    | –        | –    | –                | –                 |

See [`results/`](results/) for full benchmark output and plots.

## Architecture

1. **Ingestion** — parse and clean raw documents, preserve section/page metadata for citation tracing
2. **Chunking** — configurable chunking strategies (fixed-size, semantic/paragraph-aware), compared for retrieval impact
3. **Retrieval**
   - Dense: FAISS + embedding model
   - Sparse: BM25
   - Hybrid: Reciprocal Rank Fusion (RRF) of dense + sparse
   - Reranking: cross-encoder reranks top-k hybrid results
4. **Generation** — LLM API call (generation quality held constant across strategies, so results isolate retrieval quality)
5. **Citation tracking** — every generated answer traces back to source chunk + document + page
6. **Evaluation** — recall@k, MRR, LLM-judged answer accuracy against custom ground-truth QA pairs, plus latency reporting per strategy

## Repo structure