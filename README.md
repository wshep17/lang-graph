# lang-graph

Learning LangGraph by building small agents.

## Setup

```bash
source .venv/bin/activate
```

## Run an agent

From the project root:

```bash
make hello-world-agent
make calculator-agent
make help
```

## Layout

```
agents/
  hello-world-agent/   # basic one-node graph
  calculator/          # calculator agent + utilities
```

Each agent’s entrypoint is `<name>-agent.py`.
