import os
import logging
import replicate
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys from environment variables
replicate_api = os.getenv("REPLICATE_API_TOKEN")

input = {
    "top_p": 1,
    "prompt": "Write a story in the style of James Joyce. The story should be about a trip to the Irish countryside in 2083, to see the beautiful scenery and the AI robots that are tending the farms, harvesting crops, and managing the environment.",
    "temperature": 0.75,
    "max_new_tokens": 5000
}

for event in replicate.stream("meta/llama-2-13b-chat", input=input ):
    print(event, end="")

#=> " Sure, I'd be happy to help! Here's a story in the style...