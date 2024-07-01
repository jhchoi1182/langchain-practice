from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup


def ice_break_with(name: str) -> str:
    linkedin_useename = lookup(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_useename)

    summary_template = """
        링크드인의 유저 정보를 줄테니 아래 요구사항에 맞춰 답변을 생성해주세요.
        1. 짧은 요약
        2. 흥미로운 사실 2가지

        {information}
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template)

    # temperature :  언어 모델이 얼마나 창의적인지 (0이면 창의적이지 않음)
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    parser = StrOutputParser()

    chain = summary_prompt_template | llm | parser

    res = chain.invoke(input={"information": linkedin_data})

    print(res)


if __name__ == "__main__":
    ice_break_with(name="Eden Marco")
