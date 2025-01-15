from typing import List
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.schema import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser
import langchain_core.pydantic_v1 as pyd1
import pyperclip
from audio_recorder_streamlit import audio_recorder
from openai import OpenAI
import base64

client = OpenAI(api_key= "TYPE YOUR API KEY HERE")
st.set_page_config(page_title="AI 영어 튜터", layout='wide')

def mp3_player():
    with open("./answer.mp3", "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """
        st.markdown(md, unsafe_allow_html=True)


class Grammar(pyd1.BaseModel):
    reason_list: List[str] = pyd1.Field(description="문법적으로 틀린 이유. 틀린 것이 없을 경우 빈 리스트. 한국어로 작성. 문법 오류 있을 시 오류 당 하나만 출력")


def build_grammar_chain(model):
    parser = JsonOutputParser(pydantic_object=Grammar)
    format_instruction = parser.get_format_instructions()
    human_msg_prompt = HumanMessagePromptTemplate.from_template("{input}\n--\n 위 영어 텍스트에 대해 문법적으로 틀린 부분을 찾아 나열할 것. 형식은 아래 포맷형식으로 출력할 것. value의 값은 한국어로 작성\n{format_instruction}",
                                                               partial_variables={"format_instruction" : format_instruction})
    
    prompt_template = ChatPromptTemplate.from_messages(
        [
            human_msg_prompt
        ]
    )
    chain = prompt_template | model | parser
    return chain

class Correction(pyd1.BaseModel):
    reason: str = pyd1.Field(description="작성된 영어 문장이 어색하거나 잘못된 이유. 반드시 한국어로 작성할 것")
    correct_sentence: str = pyd1.Field(description="수정된 문장")

def build_corr_chain(model):
    parser = JsonOutputParser(pydantic_object=Correction)
    format_instruction = parser.get_format_instructions()
    human_msg_prompt = HumanMessagePromptTemplate.from_template("{input}\n--\n 위 영어 문장이 문법적으로 틀렸거나 어색한 이유를 다음 포맷에 맞춰 응답할 것. 결과는 반드시 한국어로 작성할 것. \n{format_instruction}",
                                                               partial_variables={"format_instruction" : format_instruction})
    
    prompt_template = ChatPromptTemplate.from_messages(
        [
            human_msg_prompt
        ]
    )
    chain = prompt_template | model | parser
    return chain

class EnglishProficiencyScore(pyd1.BaseModel):
    vocabulary: int = pyd1.Field(description="어휘, 단어의 적절성 0~10점 사이 점수로 표현할 것")
    coherence: int = pyd1.Field(description="일관성, 0~10점 사이 점수로 표현할 것")
    clarity: int = pyd1.Field(description="명확성, 0~10점 사이 점수로 표현할 것")
    overall_score: int = pyd1.Field(description="총점, 0~10점 사이 점수로 표현할 것")

def build_proficiency_score_chain(model):
    parser = JsonOutputParser(pydantic_object=EnglishProficiencyScore)
    format_instruction = parser.get_format_instructions()
    
    human_msg_prompt_template = HumanMessagePromptTemplate.from_template(
        "{input}\n---\nEvaluate the overall English proficiency of the above text. Consider grammar, vocabulary, coherence, etc. Follow the format: {format_instruction}",
        partial_variables={"format_instruction": format_instruction})

    prompt_template = ChatPromptTemplate.from_messages(
        [
            human_msg_prompt_template
        ],
    )
    
    chain = prompt_template | model | parser
    return chain



if "model" not in st.session_state:
    model = ChatOpenAI(model="gpt-4o-2024-08-06", temperature=0, openai_api_key= "TYPE YOUR API KEY HERE")
    st.session_state.model = model

if "grammar_analy_chain" not in st.session_state:
    st.session_state.grammar_analy_chain = build_grammar_chain(st.session_state.model)

if 'correction_chain' not in st.session_state:
    st.session_state.correction_chain = build_corr_chain(st.session_state.model)

if 'proficiency_score_chain' not in st.session_state:
    st.session_state.proficiency_score_chain = build_proficiency_score_chain(st.session_state.model)
    

grammar_analysis = ""
user_input = ""

st.title("AI 영어 튜터")

user_input = st.text_area("검사 받고 싶은 문장을 입력하세요: ")

st.button("검사하기")

# st.write(user_input)

if user_input:
    st.subheader("문장 분석 결과")
    with st.container(border=True):
        with st.spinner("분석 진행중...."):
            grammar_analysis = st.session_state.grammar_analy_chain.invoke({'input' : user_input})
            grammar_reasons = [reason for reason in grammar_analysis['reason_list']] 
            result = "\n".join([f"- {reason}" for reason in grammar_reasons])
            st.markdown(result)
        st.subheader("교정 후 문장")
        corr = st.session_state.correction_chain.invoke({'input' : user_input})
        st.markdown(corr['correct_sentence'])
        if corr['correct_sentence']:
            pyperclip.copy(corr['correct_sentence'])
            st.success("복사됨")
            res_audio = client.audio.speech.create(
                                    model='tts-1',
                                    voice='onyx',
                                    input=corr['correct_sentence']
                            )
            res_audio.stream_to_file("./answer.mp3")
            mp3_player()

with st.sidebar:
    st.title("AI Assistant")

    Analyzing = st.container(border=True)

    if user_input:
        with st.spinner("Analyzing.."):
            proficiency_result = st.session_state.proficiency_score_chain.invoke({'input' : user_input})
        
    with st.container(border=True):
        if user_input and proficiency_result:
            score = proficiency_result['vocabulary']
            score_text = (f"Vocabulary: {score} / 10 ")
            if score >= 8:
                st.success(score_text)
            elif 4 <= score < 8:
                st.warning(score_text)
            else:
                st.error(score_text)

    with st.container(border=True):
        if user_input and proficiency_result:
            score = proficiency_result['coherence']
            score_text = (f"Coherence: {score} / 10 ")
            if score >= 8:
                st.success(score_text)
            elif 4 <= score < 8:
                st.warning(score_text)
            else:
                st.error(score_text)

    with st.container(border=True):
        if user_input and proficiency_result:
            score = proficiency_result['clarity']
            score_text = (f"Clarity: {score} / 10 ")
            if score >= 8:
                st.success(score_text)
            elif 4 <= score < 8:
                st.warning(score_text)
            else:
                st.error(score_text)

    with st.container(border=True):
        if user_input and proficiency_result:
            score = proficiency_result['overall_score']
            score_text = (f"Overall score: {score} / 10 ")
            if score >= 8:
                st.success(score_text)
            elif 4 <= score < 8:
                st.warning(score_text)
            else:
                st.error(score_text)


    with Analyzing:
        if grammar_analysis and user_input:
            with st.spinner("Analyzing correctness.."):
                n_wrong = len(grammar_analysis['reason_list'])
    
                if n_wrong or proficiency_result['overall_score'] < 5:
                    st.error(f"{n_wrong} alert")
                else:
                    st.success(f"완벽한 문장입니다!")
