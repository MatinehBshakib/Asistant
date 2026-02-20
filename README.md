# 🧠 RulexGraphAssistant MCP Server

**RulexGraphAssistant** is a Model Context Protocol (MCP) server that bridges the gap between unstructured text, Knowledge Graphs, and Generative AI.

Built using `FastMCP` and `LangChain`, this server allows AI assistants (like Claude or IDE-based agents) to autonomously update a Neo4j graph database with new knowledge and query that database using natural language.

## 🚀 Key Features

* **Graph RAG (Retrieval Augmented Generation):** Combines the power of Google's **Gemini 3 Flash** with **Neo4j** to perform accurate, context-aware queries.
* **Unstructured to Structured Data:** Uses `LLMGraphTransformer` to automatically extract entities and relationships from raw text and inject them into the graph.
* **Text-to-Cypher:** Automatically translates natural language questions into Cypher queries to retrieve precise answers from the database.
* **MCP Compliant:** runs on `stdio` transport, making it compatible with any MCP client (Claude Desktop, Cursor, etc.).

---

## 🛠️ Tools Exposed

This server exposes two primary tools to the MCP client:

### 1. `update_quantum_database`

* **Function:** Ingests technical documentation (currently focused on Quantum Processors) into the knowledge graph.
* **Process:** It takes raw text, uses the LLM to identify nodes (concepts) and edges (relationships), and commits them to the Neo4j instance.
* **Use Case:** "Add the latest research on cryogenic cooling to the database."

### 2. `query_quantum_knowledge`

* **Function:** Answers questions based *only* on the data stored in the Neo4j graph.
* **Process:** Uses a QA Chain to generate a Cypher query, execute it against the DB, and synthesize a natural language response.
* **Use Case:** "How does cryogenic cooling affect qubit stability?"

---

## ⚙️ Tech Stack

* **Python:** Core logic.
* **FastMCP:** Lightweight framework for building MCP servers.
* **LangChain:** Orchestration for LLM interactions and Graph transformation.
* **Neo4j:** The underlying Graph Database (supports AuraDB).
* **Google Gemini:** The LLM used for extraction and reasoning (`gemini-3-flash-preview`).

---

## 📦 Installation & Setup

### Prerequisites

* Python 3.10+
* A Neo4j Database instance (Local or [Neo4j Aura](https://www.google.com/search?q=https://neo4j.com/cloud/aura/)).
* A Google Cloud API Key with access to Gemini models.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/rulex-graph-assistant.git
cd rulex-graph-assistant

```

### 2. Install Dependencies

```bash
pip install fastmcp langchain-neo4j langchain-google-genai langchain-experimental neo4j

```

### 3. Configuration

> **⚠️ Security Note:** The source code currently contains placeholders for credentials. For production use, it is highly recommended to use Environment Variables or a `.env` file rather than hardcoding credentials.

Open `server.py` and configure the following lines, or set them in your environment:

```python
os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY"
graph = Neo4jGraph(
    url="neo4j+s://your-db-id.databases.neo4j.io", 
    username="neo4j", 
    password="YOUR_DB_PASSWORD"
)

```

---

## 🖥️ Usage

You can run the MCP server directly using Python. Since it uses the `stdio` transport, it is designed to be called by an MCP client, but you can test the entry point locally:

```bash
python server.py

```

### connecting to Claude Desktop

To use this with Claude Desktop, add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "rulex-graph": {
      "command": "python",
      "args": ["/absolute/path/to/rulex-graph-assistant/server.py"]
    }
  }
}

```

---

## 🔮 Future Improvements

* [ ] Abstract credentials into a `.env` file.
* [ ] Add a tool to accept dynamic text input for database updates (currently hardcoded).
* [ ] Implement schema validation for the Graph Transformer to ensure consistent node types.
* [ ] Add error handling for API rate limits.

---

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)

---
