from tools import web_search, scrape_url
from agents import build_search_agent, build_search_reader_agent, writer_chain, critic_chain
from rich import print

def run_pipeline(topic: str) -> dict:
    state = {}
    #search agent working
    print("\n"+" =*50")
    print("Step 1:search agent is working...")
    print("=*50")

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages" : [("user",f"Find recent information on the topic: {topic}")]
    })
    
    state["search_result"] = search_result["messages"][-1].content
    print("\n"+" =*50")
    print(state["search_result"])
    
    
    #output of : print(search_result)
    # {
#     "messages": [
#         HumanMessage(content="What is the capital of France?"),
#         AIMessage(content="", tool_calls=[{"name": "web_search", ...}]),
#         ToolMessage(content="Title: Capital of France - Wikipedia..."),
#         AIMessage(content="The capital of France is Paris.")
#     ]
# }


    #reader agent working
    print("\n"+" =*50")
    print("Step 2:reader agent is working...")
    print("=*50")
    
    reader_agent = build_search_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_result'][:800]}"
        )]
    })
    
    state["scraped_result"] = reader_result["messages"][-1].content
    print("\n"+" =*50")
    print("\nScraped Result:",state["scraped_result"])
    
    #writer chain working
    print("\n"+" =*50")
    print("Step 3:writer chain is working...") 
    print("=*50")
    
    research_combined = (
        f"SEARCH RESULTS:\n{state['search_result']}\n\n"
        f"DETAILED SCRAPED RESULTS:\n{state['scraped_result']}"
    )
    state['report'] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })
    
    print("\n"+" =*50")
    print("\nGenerated Report:\n",state['report'])
    
    state['feedback'] = critic_chain.invoke({
        "report": state['report']
    })  
    
    print("\n"+" =*50")
    print("\nStep 4: Critique of the Report:\n",state['feedback'])
    
    return state

if __name__ == "__main__":
    topic = input("\n Enter a research topic: ")
    run_pipeline(topic)
    
    