from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

import scraper

# Initialize the model
model = OllamaLLM(model='llama3.1')

# Define the prompt template
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully:\n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

def parse(chunks, description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_result = []

    for i, chunk in enumerate(chunks, start=1):
        try:
            # Invoke the model for each chunk
            response = chain.invoke({
                "dom_content": chunk,
                "parse_description": description,
            })

            # Append the response to the results
            parsed_result.append(response)

        except Exception as e:
            print(f"An error occurred while processing chunk {i}: {e}")
            parsed_result.append('')  # Append empty string in case of error

    # Join all responses into a single string
    return "\n".join(parsed_result)