from crewai import Agent,LLM
from tools import yt_tool


# Create a senior blog content researcher
blog_researcher = Agent(
    role = 'Blog research from youtube videos',
    goal = 'get the relevant video content for the topic{topic} from Yt channel',
    verbose=True,
     backstory=(
       "Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion" 
    ),
    # llm=LLM(model="ollama/qwen2.5", base_url="http://localhost:11434"),
    tools=[yt_tool],
    allow_delegation=True
)

# creating a senior blog writer agent with YT tool
blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    # llm= LLM(model="ollama/qwen2.5", base_url="http://localhost:11434"),
    tools=[yt_tool],
    allow_delegation=False


)