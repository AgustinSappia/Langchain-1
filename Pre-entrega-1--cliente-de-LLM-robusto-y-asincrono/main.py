import asyncio
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI(model="gpt-4o", temperature=0.7)
parser = StrOutputParser()

# --- responder la pregunta ---
prompt_chain = (
    ChatPromptTemplate.from_template(
        "responde la siguiente pregunta: {pregunta}"
    )
    | model
    | parser
)



async def main():
    # .abatch procesa varios productos a la vez (más eficiente que un for con ainvoke)
    prompt = {"pregunta": "Que es la entropia"}
    resp = await prompt_chain.ainvoke(prompt)
    print(resp)


if __name__ == "__main__":
    asyncio.run(main())
