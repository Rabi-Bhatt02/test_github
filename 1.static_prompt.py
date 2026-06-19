from langchain_core.prompts import PromptTemplate

static_prompt=PromptTemplate(
    input_Variable=[],
    template="Write a short fun facta about knowledge representation."
)

prompt_text=static_prompt.format()
print(prompt_text)