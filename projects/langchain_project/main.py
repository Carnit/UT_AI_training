# project to do youtube script generator

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import List

# Load environment variables
load_dotenv()


# Define the script structure using Pydantic
class YouTubeScript(BaseModel):
    title: str
    hook: str
    introduction: str
    main_points: List[str]
    conclusion: str
    tags: List[str]
    estimated_duration: str


# Prompt + LLM setup
class ScriptGenerator:
    def __init__(self, google_api_key: str):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=google_api_key,
            temperature=0.7,
            max_output_tokens=3000,
        )
        self.parser = PydanticOutputParser(pydantic_object=YouTubeScript)
        self.prompt = PromptTemplate(
            input_variables=["topic"],
            template="""You are a helpful YouTube content assistant. Generate a complete script based on the topic: {topic}

            Include:
            - A catchy title
            - A hook (1-2 sentences)    
            - A brief introduction
            - 3 to 5 bullet-pointed main ideas
            - A conclusion with a call-to-action
            - 5-8 relevant YouTube tags
            - Estimated duration

            {format_instructions}
            """,
            partial_variables={
                "format_instructions": self.parser.get_format_instructions()
            },
        )
        self.chain = self.prompt | self.llm | self.parser

    def generate(self, topic: str) -> YouTubeScript:
        return self.chain.invoke({"topic": topic})


# Main logic
def main():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Please set your GOOGLE_API_KEY in the .env file.")
        return

    topic = input("🎬 Enter your video topic: ")
    generator = ScriptGenerator(api_key)

    print("\n⏳ Generating script...")
    script = generator.generate(topic)

    print("\n✅ Script Generated:")
    print(f"\nTitle: {script.title}")
    print(f"\nHook: {script.hook}")
    print(f"\nIntroduction: {script.introduction}")
    print("\nMain Points:")
    for i, point in enumerate(script.main_points, 1):
        print(f"  {i}. {point}")
    print(f"\nConclusion: {script.conclusion}")
    print(f"\nTags: {', '.join(script.tags)}")
    print(f"Estimated Duration: {script.estimated_duration}")


if __name__ == "__main__":
    main()
