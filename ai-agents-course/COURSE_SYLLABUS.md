# AI Agents with Python — Beginner to Production (2026)

**For:** college students and working professionals who want to become an AI Engineer / AI Agent Developer.

**Total:** 20 modules, 153 lessons, about 19–20 hours.

Canonical syllabus. Modules are produced in order, one per request. Every module ends with a fully implemented, tested practical project. Modules 1–6 are built and their lesson titles are final; for later modules, lesson titles may be refined while a module is built.

## Overview

| Module | Title | Project | Lessons | Status |
|---:|---|---|---:|---|
| 0 | Your Developer Setup | Your First GitHub Repository | 3 | Planned |
| 1 | Python for AI Engineering | Python AI Toolkit | 7 | Completed |
| 2 | LLM Fundamentals and API Integration | AI Study Assistant | 7 | Completed |
| 3 | Prompt Engineering and Structured Outputs | AI Resume Analyzer | 6 | Completed |
| 4 | AI Agent Architecture | Smart Calculator Agent | 6 | Completed |
| 5 | Tool Calling and Function Execution | Personal Productivity Agent | 7 | Completed |
| 6 | Agent Memory and Conversation State | Persistent AI Study Companion | 7 | Completed |
| 7 | Reliable and Efficient Agents | Resilient API Agent | 10 | Planned |
| 8 | Model Context Protocol (MCP) | Restricted File Assistant MCP Server | 8 | Planned |
| 9 | Embeddings and Vector Search | Semantic Search Engine | 7 | Planned |
| 10 | Retrieval-Augmented Generation (RAG) | Chat With Your PDFs + Ask Your Database | 11 | Planned |
| 11 | LangGraph Fundamentals | AI Content Workflow | 7 | Planned |
| 12 | Multi-Agent Systems | AI Research Team | 7 | Planned |
| 13 | Web Research and Automation Agents | Research Assistant | 7 | Planned |
| 14 | Testing and Evaluation of AI Agents | AI Agent Evaluation Suite | 9 | Planned |
| 15 | AI Agent Security | Secure Document Agent | 9 | Planned |
| 16 | FastAPI for AI Applications | Authenticated AI Agent API | 10 | Planned |
| 17 | Docker, Deployment, and Monitoring | Deployed AI Agent API | 8 | Planned |
| 18 | Full-Stack AI Agent Application | Production AI Workspace | 8 | Planned |
| 19 | AI Career Switch | Your AI Engineer Portfolio | 9 | Planned |
| | **Total** | | **153** | |

## Start here

### Module 0: Your Developer Setup

*Project: Your First GitHub Repository*

1. The Terminal: Folders, Files and Running Commands
   - terminal vs shell vs command; why developers use the terminal; opening it on Windows (Git Bash, PowerShell), macOS, Linux and VS Code
   - anatomy of a command; the folder tree; absolute vs relative paths; pwd, ls, cd, .., ~
   - files: echo with > and >>, cat, touch, wc, cp, mv, rm, rm -r (and why rm has no undo); hidden dotfiles and ls -a
   - running Python with arguments (sys.argv); exit codes and $?; "No such file" and "command not found"; PATH and which
   - PowerShell equivalents; speed habits: Tab, up arrow, Ctrl+C, clear, --help
2. Virtual Environments, pip and the .env File: Why Every Project Gets Its Own
   - the version-clash problem; isolation; python3 -m venv .venv; activating on every shell; what activate does to PATH
   - pip and PyPI; exact pins (==, >=, ~=); pip freeze > requirements.txt; rebuilding a venv from requirements.txt
   - what to commit and what never to commit; python -m pip; uv (used from Module 7)
   - environment variables (export, os.environ.get); .env and .env.example; python-dotenv; never printing secrets; revoking a leaked key
   - project: the setup checker (5 of 6 checks before Git)
3. Git and GitHub: Save, Commit, Push and Share Your Work
   - version control; Git vs GitHub; working folder, staging area, repository, remote
   - git config; init, status, .gitignore and check-ignore, add, commit, log; good commit messages
   - diff and restore; branches with switch -c, merge and fast-forward
   - GitHub: new repository, signing in (Credential Manager, gh auth login, SSH); remote add, push -u, clone, pull; a pushed secret
   - project: Your First GitHub Repository (6 of 6 checks, 26 tests, README)

## Part I — Foundations

### Module 1: Python for AI Engineering

*Project: Python AI Toolkit*

1. Welcome, the Agent Loop, and Your Python Setup
2. Python Core Data: Variables, Lists, Dictionaries and Sets
3. Functions, Classes and Exceptions
4. Modules, Packages, Files, JSON and Environment Variables
5. Type Hints, HTTP Requests and Async
6. Project, Part 1: Plan, Data Model and Validation
7. Project, Part 2: Reports, CLI, Tests and Wrap-up

### Module 2: LLM Fundamentals and API Integration

*Project: AI Study Assistant*

1. How LLMs Work: Tokens, Context Windows and Generation
2. Your First API Call: Keys, Requests and Responses
3. Conversations: Message History and the Growing Context
4. Controlling Output: Limits, Streaming and Structured JSON
5. Production Basics: Errors, Rate Limits, Retries and Costs
6. Project, Part 1: AI Study Assistant, Client, Costs and Explanations
7. Project, Part 2: Quizzes, Chat, Tests and Wrap-up

### Module 3: Prompt Engineering and Structured Outputs

*Project: AI Resume Analyzer*

1. Prompt Anatomy: Instructions, Context and Constraints
2. Examples, XML Tags and Task Decomposition
3. Structured Outputs: Pydantic Schemas and Parsing Failures
4. Prompt Versioning and Evaluations
5. Project, Part 1: AI Resume Analyzer, Extraction and Comparison
6. Project, Part 2: Reports, Demo, Tests and Wrap-up

## Part II — Build Agents from Scratch

### Module 4: AI Agent Architecture

*Project: Smart Calculator Agent*

1. Chatbots, Workflows and Agents: What Makes an AI Agent
2. Inside an Agent: Model, Instructions, Tools and State
3. The Agent Loop: Decide, Act, Observe, Repeat
4. Stopping Safely: Step Limits, Tool Errors and Safe Tools
5. Project, Part 1: Smart Calculator Agent, Tools and the Loop
6. Project, Part 2: Traces, Demo, Tests and Wrap-up

### Module 5: Tool Calling and Function Execution

*Project: Personal Productivity Agent*

1. Tool Calling: How a Model Uses Your Functions
2. Many Tools: A Registry, Schemas from Pydantic, Parallel Calls
3. Validating Tool Inputs: Never Trust, Always Check
4. Timeouts and Failures: When a Tool Never Answers
5. Permissions and Human Confirmation: Ask Before You Act
6. Project, Part 1: Personal Productivity Agent, Store, Tools and Policy
7. Project, Part 2: The Loop, the Demo, Tests and Wrap-up

### Module 6: Agent Memory and Conversation State

*Project: Persistent AI Study Companion*

1. Why Agents Forget: Stateless APIs and Conversation History
2. Short-Term Memory: Context Windows and Sliding Windows
3. Summary Memory: Compressing a Long Conversation
4. Long-Term Memory: Facts That Outlive a Conversation
5. Saving Memory in SQLite: Sessions, Users, Retention and Deletion
6. Project, Part 1: The Persistent AI Study Companion
7. Project, Part 2: One Turn, a Two-Day Demo, Privacy, Tests and Wrap-up

### Module 7: Reliable and Efficient Agents

*Project: Resilient API Agent*

1. Why Agents Fail in Production: Errors, Slow Calls and Rate Limits (429)
2. Retries Done Right: Exponential Backoff, Jitter and Timeouts
3. Rate-Limit-Aware Concurrency: Many Calls Without Getting Blocked
   - a limit on calls running at the same time
   - reading the rate-limit and retry-after information a provider sends back
4. Circuit Breakers: Stop Calling a Service That Is Down
5. Fallbacks and Other Providers: OpenAI, Gemini and a Local Model with Ollama
   - one small ModelClient interface, many providers behind it
   - provider-independent error handling
   - structured output reliability across providers
6. Choosing and Routing Models: Small vs Large, Cost vs Quality
   - routing by task complexity
   - escalating to a larger model only when a check fails
   - comparing cost and quality on your own test cases
7. Caching: Response Caches and Prompt Caching
8. Context Engineering: What Goes In, What Stays Out
   - counting tokens before a call and estimating its cost
   - trimming large tool results, ordering content, token and cost budgets
9. Project, Part 1: Resilient API Agent, Retry, Breaker and Fallback Chain (setup with uv)
10. Project, Part 2: Budgets, Logging, Tracing, Tests and Wrap-up

## Part III — Knowledge and Tool Connectivity

### Module 8: Model Context Protocol (MCP)

*Project: Restricted File Assistant MCP Server*

1. What MCP Is: Hosts, Clients and Servers, and Why It Exists
2. Tools, Resources and Prompts: The Three Things a Server Offers
   - tool discovery and capability negotiation
3. Building an MCP Server in Python
4. Connecting Your Server to Claude, and Using Ready-Made MCP Servers
   - risks of connecting an untrusted third-party server
   - tool output validation
5. Remote MCP: HTTP Transport and Authorization
   - OAuth fundamentals: tokens and scopes
   - server authentication and trust boundaries
6. Testing an MCP Server and Staying Compatible Across Versions
7. Project, Part 1: Restricted File Assistant, Allowed Folders and Path Safety
8. Project, Part 2: Client, Demo, Tests and Wrap-up

### Module 9: Embeddings and Vector Search

*Project: Semantic Search Engine*

1. What Embeddings Are: Meaning as Numbers
2. Cosine Similarity: Measuring How Close Two Texts Are
3. Chunking Text: Size, Overlap and Metadata
4. Vector Databases: Building and Querying a Search Index
   - updating and deleting entries
   - metadata filtering at query time
5. Keyword Search (BM25) and Measuring Search Quality
   - precision@k and recall@k
   - benchmarking different chunk sizes and settings
   - speed, memory and cost trade-offs
6. Project, Part 1: Semantic Search Engine, Ingest and Index
7. Project, Part 2: Filters, Quality Report, Tests and Wrap-up

### Module 10: Retrieval-Augmented Generation (RAG)

*Project: Chat With Your PDFs · Mini project: Ask Your Database*

1. The RAG Pipeline: Ingest, Retrieve, Generate
2. Loading and Chunking PDFs, Including Scanned Pages and Images with Vision
3. Retrieve Then Answer: Citations and Saying "I Don't Know"
4. Hybrid Search and Reranking: Better Results from the Same Documents
5. Query Rewriting and Agentic RAG: Retrieval as a Tool
6. Keeping the Index Fresh: Document Versions, Incremental Indexing and Deletion
7. Who Can See What: Access Control and Multi-User Document Isolation
8. Talking to Databases: A Safe Read-Only SQL Agent
9. Evaluating RAG: Retrieval Quality and Answer Quality
   - RAG evaluation datasets
   - citation correctness
   - retrieval failure analysis
10. Project, Part 1: Chat With Your PDFs, Ingestion and Retrieval
11. Project, Part 2: Grounded Answers, Citations, Tests and Wrap-up

## Part IV — Advanced Orchestration

### Module 11: LangGraph Fundamentals

*Project: AI Content Workflow*

1. Why Graphs: State, Nodes and Edges
2. Conditional Routing and Loops
3. Checkpoints and Persistence: Pause Today, Continue Tomorrow (with checkpoint recovery)
4. Human-in-the-Loop: Interrupts, Approval and Resuming
5. Safe to Run Twice: Idempotent Nodes and Failed-Node Recovery
   - duplicate execution prevention
   - state versioning and workflow evolution
6. Project, Part 1: AI Content Workflow, Graph and State
7. Project, Part 2: Approval Step, Demo, Tests and Wrap-up

### Module 12: Multi-Agent Systems

*Project: AI Research Team*

1. One Agent or Many: When Several Agents Help and When They Don't
2. Orchestrator and Worker Agents
3. Handoffs and Sharing Context Between Agents (with shared-state consistency)
4. Parallel Agents: Speed, Cost and Coordination Failures
5. The Framework Landscape: Claude Agent SDK, OpenAI Agents SDK, CrewAI and LangGraph
   - framework vs custom orchestration, compared on one task
6. Project, Part 1: AI Research Team, Roles and Handoffs
7. Project, Part 2: Parallel Research, Review, Tests and Wrap-up

### Module 13: Web Research and Automation Agents

*Project: Research Assistant*

1. Web Search and Fetch Tools (with SSRF and unsafe URL-fetch prevention)
2. Reading Pages Safely: Untrusted Content, Site Terms and Rate Limits
3. Browser Automation Basics (with failure recovery)
4. Source Checking: Comparing and Trusting Sources
5. Writing a Cited Report
6. Project, Part 1: Research Assistant, Search, Fetch and Extract
7. Project, Part 2: Source Checks, Cited Brief, Tests and Wrap-up

## Part V — Quality and Security

### Module 14: Testing and Evaluation of AI Agents

*Project: AI Agent Evaluation Suite*

1. Unit Tests vs Evals: Two Different Questions
2. Building Test Sets: Real Cases, Edge Cases and Expected Outcomes
3. Agent Metrics: Tool-Selection Accuracy, Task-Completion Rate and Multi-Step Success
4. Grading: Code Checks and LLM-as-Judge (and human evaluation)
5. Regression Testing: Did the New Prompt Break an Old Case? (with GitHub Actions)
6. Measuring Cost and Latency
7. Observability in Practice: Tracing with Langfuse, LangSmith and OpenTelemetry
   - production trace analysis
   - continuous production evaluation
8. Project, Part 1: Evaluation Suite, Dataset and Graders
9. Project, Part 2: Reports, Regression Run, Tests and Wrap-up

### Module 15: AI Agent Security

*Project: Secure Document Agent*

1. Thinking Like an Attacker: The OWASP Top 10 for LLM Applications
2. Prompt Injection: Direct Attacks and Hidden Instructions in Documents (direct and indirect)
3. Protecting Secrets and Least-Privilege Tools
   - secrets management
   - unsafe tool execution and SSRF
4. Input and Output Filtering, PII and Data Privacy
5. Multi-Tenant Data Isolation: One Customer Must Never See Another's Data
6. Sandboxing and Audit Logs (with security incident handling)
7. Supply-Chain Security: Dependencies and Vulnerability Scanning
8. Project, Part 1: Secure Document Agent, Defences
9. Project, Part 2: Adversarial Tests, Audit Trail and Wrap-up

## Part VI — Production

### Module 16: FastAPI for AI Applications

*Project: Authenticated AI Agent API*

1. FastAPI Basics: Routes, Pydantic and Automatic Docs
2. Endpoints for an Agent: Request Validation and Errors
3. Streaming Responses
4. Authentication: API Keys and Tokens
5. Persistence: PostgreSQL and Migrations
6. Redis Fundamentals: Keys, Expiry and a Shared Cache
7. Long-Running Agents: Background Jobs, Status Checks and Resuming After a Crash
   - task queues and background workers
   - job cancellation
8. Jobs That Survive Failure: Idempotency, Retries and Dead-Letter Queues
   - duplicate job prevention
   - multiple workers and simple locks
   - safe recovery after a crash
9. Project, Part 1: Authenticated AI Agent API, Endpoints and Auth
10. Project, Part 2: Streaming, Background Jobs, Tests and Wrap-up

### Module 17: Docker, Deployment, and Monitoring

*Project: Deployed AI Agent API*

1. Dockerfiles and Containers
2. Environment Configuration and Secrets (with production configuration management)
3. Deploying to the Cloud
4. CI/CD: Test and Deploy on Every Push
   - GitHub Actions pipeline: test, build, scan, deploy
   - dependency and container image scanning
5. Releasing Safely: Versioned Images and Rollback
6. Health Checks, Logs, Metrics and Alerts (with infrastructure health monitoring)
7. Cost Monitoring and Scaling
8. Project: Deploy the AI Agent API and Wrap-up

### Module 18: Full-Stack AI Agent Application

*Project: Production AI Workspace*

1. Architecture: How the Pieces Fit Together (multi-tenant architecture and trade-offs)
2. A Frontend for the Agent API
3. Users, Data and Authentication (with user-level data isolation)
4. Memory, RAG and Tools Working Together
5. Rate Limiting, Usage Tracking and Observability (with usage limits and quotas)
6. Production Error Handling and End-to-End Integration Testing
7. Final Deployment
8. Demo, Tests and Course Wrap-up

## Part VII — Career

### Module 19: AI Career Switch

*Project: Your AI Engineer Portfolio*

1. AI Roles Explained: AI Engineer, ML Engineer and Data Scientist
2. Prompting, RAG or Fine-Tuning: Choosing the Right Tool
   - agent, workflow, RAG or traditional software
3. Working in an Existing Codebase: Read, Debug and Change It Safely
   - reading an unfamiliar AI codebase
   - debugging an existing agent
   - regression tests before every change
4. From 18 Projects to a Portfolio: READMEs, Demo Videos and GitHub
5. Resume and LinkedIn for Career Switchers
6. The AI System Design Interview
   - cost and infrastructure estimation
   - architecture trade-offs
7. Interview Practice: Using the Course Question Banks
   - practical interview scenarios and mock interviews
8. Working with AI Coding Tools: Claude Code and Cursor
9. Your 90-Day Plan and How to Stay Current

## Portfolio capstones (after Module 19, on request)

| Capstone | What it shows |
|---|---|
| 1. AI Research Assistant | web search and fetching, source verification, agent orchestration, cited reports, evaluation |
| 2. Enterprise Knowledge Assistant | RAG, hybrid search and reranking, document permissions, citation verification, SQL, evaluation |
| 3. AI Workflow Automation Platform | multi-step workflows, human approval, background jobs, persistent state, authentication, monitoring |

Each capstone has a public GitHub repository, a professional README, an architecture diagram, setup instructions, automated tests, a short demo video, a deployed demo where feasible, and known limitations.
