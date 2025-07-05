from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
import os

index = None

def build_user_index(filepath):
    global index
    try:
        # Check if API key is available
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key or api_key == "your_groq_api_key_here":
            raise Exception("GROQ API key not configured")
        
        documents = SimpleDirectoryReader(input_files=[filepath]).load_data()
        index = VectorStoreIndex.from_documents(documents)
    except Exception as e:
        raise Exception(f"Failed to build index: {str(e)}")

def generate_with_style(prompt):
    global index
    try:
        if index is None:
            return {"output": "Upload writing samples first."}
        query_engine = index.as_query_engine()
        response = query_engine.query(prompt)
        # Convert response to string safely
        return {"output": str(response)}
    except Exception as e:
        return {"output": f"Error generating with style: {str(e)}"}