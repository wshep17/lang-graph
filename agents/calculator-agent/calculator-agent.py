import langgraph.graph

from utilities import add, subtract, multiply, divide

# Step 1: Initialize the model
model = init_chat_model(
    "claude-sonnet-4-6",
    temperature=0
)

# Step 2: Wrap calculator functions as tools the model can call
tools = [
    Tool(
        name="add",
        description="Add two numbers",
        func=add,
    ),
    Tool(
        name="subtract",
        description="Subtract two numbers",
        func=subtract,
    ),
    Tool(
        name="multiply",
        description="Multiply two numbers",
        func=multiply,
    ),
    Tool(
        name="divide",
        description="Divide two numbers",
        func=divide,
    ),
]

# Step 3: Augment the model with the tools
augmented_model = model.bind_tools(tools)

# Define the state for the graph
class State(TypedDict):
    messages: Annotated[list, add_messages]
    llm_calls: int

# Define the model node with the augmented model
model_node = Model(model=augmented_model)

# Define the tool node with the tools
tool_node = ToolNode(tools=tools)

# Define the graph
graph = StateGraph(State)

# Connect the nodes
graph.add_edge(START, model_node)