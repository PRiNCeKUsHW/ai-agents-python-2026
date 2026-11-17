# AI Agents with Python 2026: Beginner to Production

Source code for the YouTube course **AI Agents with Python 2026: Beginner to Production**:
20 modules (153 lessons, about 19–20 hours) that take you from your first terminal command to a deployed,
tested, secure AI agent application, and then to your first AI Engineer job.

**For:** college students and working professionals who want to become an AI Engineer / AI Agent Developer.

Every module has narrated lesson videos, English captions, a fully working project with tests,
a quiz and an extension challenge.

> Arrived from a YouTube description? Each video links straight to its module folder below.

## Modules

| # | Module | Project | Lessons | Status |
|---|--------|---------|---|--------|
| 0 | [Your Developer Setup](ai-agents-course/modules/module-00-developer-setup) (Hinglish) | [Your First GitHub Repository](ai-agents-course/modules/module-00-developer-setup/project/my-first-repo) | 3 | Ready (video rendered) |
| 1 | [Python for AI Engineering](ai-agents-course/modules/module-01-python-ai-engineering) | [Python AI Toolkit](ai-agents-course/modules/module-01-python-ai-engineering/project/python-ai-toolkit) | 7 | Published |
| 2 | [LLM Fundamentals and API Integration](ai-agents-course/modules/module-02-llm-fundamentals) | [AI Study Assistant](ai-agents-course/modules/module-02-llm-fundamentals/project/ai-study-assistant) | 7 | Published |
| 3 | [Prompt Engineering and Structured Outputs](ai-agents-course/modules/module-03-prompt-engineering) | [AI Resume Analyzer](ai-agents-course/modules/module-03-prompt-engineering/project/ai-resume-analyzer) | 6 | Published |
| 4 | [AI Agent Architecture](ai-agents-course/modules/module-04-agent-architecture) | [Smart Calculator Agent](ai-agents-course/modules/module-04-agent-architecture/project/smart-calculator-agent) | 6 | Published |
| 5 | [Tool Calling and Function Execution](ai-agents-course/modules/module-05-tool-calling) | [Personal Productivity Agent](ai-agents-course/modules/module-05-tool-calling/project/productivity-agent) | 7 | Published |
| 6 | [Agent Memory and Conversation State](ai-agents-course/modules/module-06-agent-memory) | [Persistent AI Study Companion](ai-agents-course/modules/module-06-agent-memory/project/study-companion) | 7 | Ready (video rendered) |
| 7 | Reliable and Efficient Agents | Resilient API Agent | 10 | Coming soon |
| 8 | Model Context Protocol (MCP) | Restricted File Assistant MCP Server | 8 | Coming soon |
| 9 | Embeddings and Vector Search | Semantic Search Engine | 7 | Coming soon |
| 10 | Retrieval-Augmented Generation (RAG) | Chat With Your PDFs + Ask Your Database | 11 | Coming soon |
| 11 | LangGraph Fundamentals | AI Content Workflow | 7 | Coming soon |
| 12 | Multi-Agent Systems | AI Research Team | 7 | Coming soon |
| 13 | Web Research and Automation Agents | Research Assistant | 7 | Coming soon |
| 14 | Testing and Evaluation of AI Agents | AI Agent Evaluation Suite | 9 | Coming soon |
| 15 | AI Agent Security | Secure Document Agent | 9 | Coming soon |
| 16 | FastAPI for AI Applications | Authenticated AI Agent API | 10 | Coming soon |
| 17 | Docker, Deployment, and Monitoring | Deployed AI Agent API | 8 | Coming soon |
| 18 | Full-Stack AI Agent Application | Production AI Workspace | 8 | Coming soon |
| 19 | AI Career Switch | Your AI Engineer Portfolio | 9 | Coming soon |

After the course: three portfolio capstones (AI Research Assistant, Enterprise Knowledge Assistant,
AI Workflow Automation Platform), each with a public repository, README, architecture diagram,
tests, demo video and known limitations.

Full syllabus: [ai-agents-course/COURSE_SYLLABUS.md](ai-agents-course/COURSE_SYLLABUS.md)

New to a term? The [glossary](ai-agents-course/GLOSSARY.md) explains every technical word in plain language.

Test yourself: the [question bank](ai-agents-course/QUESTION_BANK.md) has every question asked in the videos (quick checks, quizzes, practice and interview questions), with click-to-reveal answers.

## Run a project

You need Python 3.11 or newer. For example, the Module 2 project:

```bash
cd ai-agents-course/modules/module-02-llm-fundamentals/project/ai-study-assistant
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m pytest                 # 23 tests, no API key needed
python -m study --offline explain "Python decorators"
```

Every project README has its own setup steps. From Module 2 on, the projects call the
Anthropic API. Each one also has an offline mode with a built-in fake API, so you can follow
along and run the tests without a key. To use a real model, copy `.env.example` to `.env`
and add your own `ANTHROPIC_API_KEY`. Never commit that file.

## Repository layout

```text
ai-agents-course/        the course: modules, projects, lesson scripts, captions, video tooling
  modules/module-NN-*/   one folder per module (README, project/, source/, quiz.md, QUESTIONS.md, captions/)
  studio/                Remotion project that renders the lesson videos
  tools/                 build, render and validation scripts
fastapi-course/          an earlier FastAPI course
bytetitan-ep14-counter/  "Python in 60 Seconds" short (HyperFrames)
hyperframes/, remotion/  video tooling experiments
01_basics/               early JavaScript practice
```

Rendered videos and narration audio are not stored in the repository. Watch the lessons on
YouTube, or rebuild them with the tools in `ai-agents-course/` (see its README).
