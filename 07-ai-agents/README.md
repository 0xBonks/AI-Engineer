# Module 07: AI Agents

## Overview

Learn to build AI agents that can use tools, make decisions, and orchestrate complex workflows. Master the Model Context Protocol (MCP), implement ReAct prompting patterns, use OpenAI Functions/Tools, and design multi-agent systems for sophisticated AI applications.

## Learning Objectives

By completing this module, you will be able to:

- Identify appropriate use cases for AI agents and implement ReAct prompting patterns
- Understand Model Context Protocol (MCP) components and architecture
- Build both MCP clients and servers for agent communication
- Implement OpenAI Functions/Tools for agent tool use
- Design and implement multi-agent orchestration patterns

## Prerequisites

- **Completed**: Module 06 (RAG Systems)
- **Required**: Strong understanding of LLMs, prompting, and APIs
- **Recommended**: Experience with async programming and system design

## Estimated Time

**15-20 hours** to complete all exercises and demos

## Key Concepts

### 1. Agent Fundamentals
- What are AI agents?
- Agent vs chatbot vs assistant
- Autonomous vs semi-autonomous agents
- Agent architectures (ReAct, Plan-Execute, etc.)
- When to use agents vs traditional code
- Limitations and risks

### 2. ReAct Pattern
- Reasoning + Acting paradigm
- Thought-Action-Observation cycles
- Self-correction and iteration
- Prompt engineering for ReAct
- Implementation patterns
- Debugging agents

### 3. Model Context Protocol (MCP)
- MCP architecture and components
- Servers: Expose resources and tools
- Clients: Connect to servers and use tools
- Protocol specifications
- Security considerations
- Use cases and examples

### 4. Tool Use (OpenAI Functions/Tools)
- Function calling basics
- Tool schema definition
- Parallel function calling
- Streaming with tools
- Error handling
- Cost considerations

### 5. Multi-Agent Systems
- Agent collaboration patterns
- Supervisor-worker architecture
- Agent-to-agent communication
- State management
- Conflict resolution
- Orchestration frameworks

## Structure

```
07-ai-agents/
├── README.md                                  # This file
├── notebooks/                                 # Interactive tutorials
│   ├── 01-agent-fundamentals.ipynb
│   ├── 02-react-pattern.ipynb
│   ├── 03-mcp-basics.ipynb
│   ├── 04-openai-tools.ipynb
│   ├── 05-multi-agent-systems.ipynb
│   └── 06-production-agents.ipynb
├── exercises/                                 # Hands-on challenges
│   ├── 01-simple-agent.py
│   ├── 02-react-implementation.py
│   ├── 03-mcp-server.py
│   ├── 04-mcp-client.py
│   ├── 05-tool-calling-agent.py
│   ├── 06-multi-agent-system.py
│   └── 07-production-agent.py
├── tests/                                     # Automated validation
│   └── test_exercises.py
└── solutions/                                 # Reference implementations
    └── solutions/
```

## Topics Covered

### AI Agents vs Traditional Code
- **Agents**: Flexible, adaptable, handle ambiguity
- **Traditional**: Predictable, efficient, testable
- **Use agents when**: Requirements are complex or changing

### ReAct Prompting
- **Concept**: Interleave reasoning and actions
- **Pattern**: Think → Act → Observe → Repeat
- **Example**: "I need to find the weather. Let me search..."

### Model Context Protocol
- **Concept**: Standard for AI-to-tool communication
- **Architecture**: Servers expose tools, clients consume them
- **Example**: MCP server for database access

### OpenAI Tools API
- **Concept**: LLM decides when to call functions
- **Pattern**: Define tools → LLM chooses → Execute → Return
- **Example**: Calculator, weather API, database query

### Multi-Agent Orchestration
- **Concept**: Multiple specialized agents collaborate
- **Patterns**: Supervisor, peer-to-peer, hierarchical
- **Example**: Researcher + Writer + Reviewer agents

## Exercises

### Exercise 1: Simple Agent
**File**: `exercises/01-simple-agent.py`

Build a basic agent that can use simple tools.

**Success Criteria**:
- Agent understands available tools
- Selects appropriate tool for task
- Returns result to user

### Exercise 2: ReAct Implementation
**File**: `exercises/02-react-implementation.py`

Implement ReAct pattern with thought-action-observation loop.

**Success Criteria**:
- Agent shows reasoning process
- Iterates until solution found
- Handles multi-step problems

### Exercise 3: MCP Server
**File**: `exercises/03-mcp-server.py`

Create an MCP server that exposes tools and resources.

**Success Criteria**:
- Implement MCP protocol
- Expose at least 3 tools
- Handle requests correctly

### Exercise 4: MCP Client
**File**: `exercises/04-mcp-client.py`

Build an MCP client that connects to servers.

**Success Criteria**:
- Discover available tools
- Call tools via MCP
- Handle responses

### Exercise 5: Tool Calling Agent
**File**: `exercises/05-tool-calling-agent.py`

Use OpenAI Tools API to build an agent with multiple tools.

**Success Criteria**:
- Define 5+ tool schemas
- LLM selects correct tools
- Execute and return results

### Exercise 6: Multi-Agent System
**File**: `exercises/06-multi-agent-system.py`

Build a system with multiple specialized agents.

**Success Criteria**:
- 3+ agents with different roles
- Supervisor coordinates agents
- Complete complex workflow

### Exercise 7: Production Agent
**File**: `exercises/07-production-agent.py`

Build a production-ready agent with error handling and monitoring.

**Success Criteria**:
- Robust error handling
- Logging and observability
- Cost tracking
- Safety guardrails

## Resources

### Official Documentation
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Anthropic Tool Use](https://docs.anthropic.com/claude/docs/tool-use)

### Frameworks
- [LangGraph](https://github.com/langchain-ai/langgraph) - Multi-agent graphs
- [CrewAI](https://github.com/joaomdmoura/crewAI) - Role-based agents
- [AutoGen](https://github.com/microsoft/autogen) - Multi-agent framework

### Recommended Reading
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
- [LangChain Agents Guide](https://python.langchain.com/docs/modules/agents/)
- [Building LLM Agents](https://lilianweng.github.io/posts/2023-06-23-agent/)

## Next Steps

After completing this module:

1. ✅ Build an agent for a real-world task
2. ✅ Experiment with multi-agent collaboration
3. ➡️ **Choose Your Path**:
   - Module 08: Multimodal AI (add vision/audio to agents)
   - Module 09: Testing & Validation (test agent behavior)

## Code Patterns

### ReAct Pattern
```python
def react_agent(task: str, max_iterations: int = 5) -> str:
    """Agent using ReAct pattern."""
    
    for i in range(max_iterations):
        # Thought: Reason about what to do
        thought_prompt = f"""Task: {task}
        
Thought {i+1}: What should I do next?"""
        
        thought = llm_call(thought_prompt)
        
        # Action: Decide on action
        action_prompt = f"{thought}\n\nAction {i+1}:"
        action = llm_call(action_prompt)
        
        # Observation: Execute and observe result
        observation = execute_action(action)
        
        # Check if done
        if is_complete(observation):
            return observation
    
    return "Task not completed within iteration limit"
```

### OpenAI Tools Pattern
```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                },
                "required": ["location"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
    tools=tools,
    tool_choice="auto"
)

# Check if model wants to call function
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    result = get_weather(tool_call.function.arguments)
    
    # Return result to model
    messages.append(response.choices[0].message)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result
    })
    
    final_response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
```

### Multi-Agent Pattern
```python
class Supervisor:
    def __init__(self, agents: list[Agent]):
        self.agents = agents
    
    def delegate(self, task: str) -> str:
        # Decide which agent to use
        agent = self.select_agent(task)
        
        # Execute task
        result = agent.execute(task)
        
        # Verify result
        if not self.verify(result):
            # Retry with different agent
            agent = self.select_alternate_agent(task)
            result = agent.execute(task)
        
        return result

class ResearchAgent(Agent):
    def execute(self, task: str) -> str:
        # Research and gather information
        pass

class WriterAgent(Agent):
    def execute(self, task: str) -> str:
        # Write based on research
        pass
```

## Agent Architecture Patterns

### Single Agent with Tools
**Best for**: Simple tasks with clear tool usage
```
User → Agent → [Tool1, Tool2, Tool3] → Result
```

### ReAct Agent
**Best for**: Complex reasoning tasks
```
User → Think → Act → Observe → Think → ... → Result
```

### Supervisor-Worker
**Best for**: Delegating tasks to specialists
```
User → Supervisor → [Worker1, Worker2, Worker3] → Supervisor → Result
```

### Peer-to-Peer
**Best for**: Collaborative problem solving
```
User → Agent1 ↔ Agent2 ↔ Agent3 → Result
```

## Common Issues

### Agent Loops Infinitely
- Set max iterations limit
- Add explicit stopping conditions
- Improve ReAct prompts
- Track state to detect loops

### Wrong Tool Selection
- Improve tool descriptions
- Provide better examples
- Use few-shot prompting
- Add tool selection hints

### High Costs
- Limit max iterations
- Cache tool results
- Use GPT-3.5 for simple agents
- Implement early stopping

### Unpredictable Behavior
- Add extensive logging
- Test with diverse inputs
- Implement guardrails
- Use temperature=0 for consistency

## Tool Design Best Practices

1. **Clear Descriptions**: Be specific about what tool does
2. **Strong Typing**: Use JSON schema for parameters
3. **Error Handling**: Return meaningful error messages
4. **Idempotency**: Same input → same output
5. **Documentation**: Include examples in description

## Notes

- **Agents are Probabilistic**: Not deterministic like traditional code
- **Cost Adds Up**: Agents make many LLM calls
- **Test Thoroughly**: Agents can behave unexpectedly
- **MCP is New**: Standard still evolving, exciting potential
- **Portfolio Project**: Build multi-agent system for your portfolio

---

**Module Status**: 🚧 Content Development | ⬅️ Prev: RAG Systems | ⏭️ Next: Multimodal AI
