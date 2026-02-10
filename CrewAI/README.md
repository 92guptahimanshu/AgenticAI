# Crew-AI

This is an Agentic AI code where I have added two agents :
One will read the transcript from Youtube channel.
Other will write the blog based on the transcript provided by first agent.


User need to create his .env file only with OPENAI_API_KEY variable.
📘 CrewAI YouTube Blog Generator

An AI-powered multi-agent application built using CrewAI that analyzes YouTube channel content and generates high-quality technical blog posts automatically.

This project uses AI agents to:

🔍 Research YouTube videos

🧠 Extract relevant insights

✍️ Generate structured blog content

🚀 Automate content creation workflows

🏗️ Architecture

The system uses a multi-agent architecture:

👨‍🔬 Blog Researcher Agent

Searches YouTube channel

Extracts relevant video content

Summarizes technical insights

✍️ Blog Writer Agent

Converts research into engaging blog content

Structures article professionally

Simplifies complex AI/ML concepts

🛠️ Tech Stack

Python 3.11

CrewAI

CrewAI Tools

LangChain OpenAI

YouTube Channel Search Tool

OpenAI GPT Models

dotenv

📂 Project Structure
Crew-AI/
│
├── main.py
├── tools.py
├── config.py
├── .env
├── requirements.txt
└── README.md

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone [https://github.com/92guptahimanshu/AgenticAI/CrewAI.git](https://github.com/92guptahimanshu/AgenticAI.git)
cd crew-ai-youtube-blog

2️⃣ Create Virtual Environment
python -m venv crewenv
source crewenv/bin/activate      # Mac/Linux
crewenv\Scripts\activate         # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt


If installing manually:

pip install crewai crewai-tools langchain-openai python-dotenv

4️⃣ Setup Environment Variables

Create a .env file:

OPENAI_API_KEY=your_openai_api_key


If using YouTube API:

YOUTUBE_API_KEY=your_youtube_api_key

🚀 How It Works

User provides a topic.

Researcher Agent searches the specified YouTube channel.

Extracts relevant transcripts and insights.

Writer Agent generates a structured blog post.
