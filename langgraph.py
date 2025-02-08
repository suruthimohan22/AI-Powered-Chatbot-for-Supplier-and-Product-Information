from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFaceHub

llm = HuggingFaceHub(repo_id="gpt2", model_kwargs={"temperature": 0.7})

def summarize_supplier_data(data):
    template = """
    Summarize the following supplier data:
    {data}
    """
    prompt = PromptTemplate(input_variables=["data"], template=template)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(data)
