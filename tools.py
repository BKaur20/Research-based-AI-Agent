from langchain.tools import Tool
from datetime import datetime
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain.tools import DuckDuckGoSearchRun

def save_to_txt(data: str,filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    formatted_text = f"---Research Output---\nTimestamp: {timestamp}\n\n{data}\n"
    with open(filename, "a") as file:
        file.write(formatted_text)
    
    return f"Data saved to {filename} at {timestamp}"


save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves the research output to a text file. Input should be the data to save."
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information. Input should be a search query."
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

