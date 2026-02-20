import os
import sys 
from fastmcp import FastMCP
from langchain_neo4j import Neo4jGraph, GraphCypherQAChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_core.documents import Document

mcp = FastMCP("RulexGraphAsistant")
os.environ["GOOGLE_API_KEY"] = "..."
graph = Neo4jGraph(url="neo4j+s://98cb7da2.databases.neo4j.io", username="neo4j", password="...")
llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.0) 
llm_transformer = LLMGraphTransformer(llm=llm) # Initialize the LLMGraphTransformer with the language model
chain = GraphCypherQAChain.from_llm(
      llm, 
      graph=graph, 
      verbose=True, 
      allow_dangerous_requests=True)

@mcp.tool()
def update_quantum_database() -> str:

    try:
        text = "The Quantum Processor utilizes cryogenic cooling. This environment minimizes thermal noise for qubit stability."
        docs = [Document(page_content=text)] 
        graph_documents = llm_transformer.convert_to_graph_documents(docs) 
        graph.add_graph_documents(graph_documents)
        return "Graph updated successfully with quantum documentation."
    except Exception as e:
        return f"Update failed: {str(e)}"


@mcp.tool()
def query_quantum_knowledge(question: str) -> str :
      try:
           response = chain.invoke({"query": question})
           return f"AI answer: {response['result']}"
      except Exception as e:
             return f"An error occurred: {str(e)}"
       
if __name__ == "__main__":
      mcp.run(transport='stdio')