from phi.tools.youtube_tools import YouTubeTools
from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.googlesearch import GoogleSearch

load_dotenv()

GROQ_API_KEY = "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"

agent = Agent(model=Groq(id = "deepseek-r1-distill-llama-70b",api_key=GROQ_API_KEY ))


agent.print_response("How are you?")

YT_agent = Agent(
    model=Groq(id = "deepseek-r1-distill-llama-70b",api_key=GROQ_API_KEY ),
    tools=[YouTubeTools()],
    show_tool_calls=True,
    description="You are a YouTube agent. Obtain the details of a YouTube video and answer questions.",
)

agent.print_response("Summarize this video https://www.youtube.com/watch?v=ZS4kSdA_fjo", markdown=True)


WEB_agent = Agent(
    model=Groq(id = "deepseek-r1-distill-llama-70b",api_key=GROQ_API_KEY ),
    tools=[GoogleSearch()],
    description="You are a news agent that helps users find the latest news.",
    instructions=[
        "Given the channel name by user, provide the latest news about channel",
        "Search for 10 news items and select the top 4 unique items.",
        "Search in English and in Tamil.",
    ],
    show_tool_calls=True,
    #debug_mode=True,
)
agent.print_response("Karthik's show", markdown=True)


team_Agents = Agent(
  model=Groq(id = "deepseek-r1-distill-llama-70b",api_key=GROQ_API_KEY ),
  team = [YT_agent,WEB_agent],
  instruction = ("summarise the viedo based on the url provided by the user and gather latest information about the channel")
)

team_Agents.print_response("Summarize this video https://www.youtube.com/watch?v=ZS4kSdA_fjo and gather latest information about the channel")