import validators
import streamlit as st
from langchain_classic.prompts import PromptTemplate
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader
from langchain_groq import ChatGroq
import os
from pytube import YouTube
from dotenv import load_dotenv
load_dotenv()
YOUTUBE_PROXY = os.getenv("YOUTUBE_PROXY")

proxy={"http": YOUTUBE_PROXY, "https": YOUTUBE_PROXY} if YOUTUBE_PROXY else None

original_init = YouTube.__init__


def patched_init(self, url, *args, **kwargs):
    kwargs["proxies"] = proxy
    original_init(self, url, *args, **kwargs)

YouTube.__init__ = patched_init


# Streamlit app
st.set_page_config(page_title="LangChain: Summarize Text From YouTube or Websites",page_icon="🐧")
st.title("LangChain: Summarize Text From YT or Website")
st.subheader("Summarize URL")

#Get the Groq API Key and url(YT or website)to be summarized
with st.sidebar:
    groq_api_key=st.text_input('Groq API Key',value="",type='password') or " "


url=st.text_input("URL",label_visibility="collapsed")
#
llm=ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct",groq_api_key=groq_api_key)

prompt_template="""
Provide a summary of the following content in 300 words:
Content:{text}
"""
prompt=PromptTemplate(template=prompt_template,input_variables=["text"])


if st.button("Summarize the Content from YT or Website"):
    # Validate all the inputs
    if not groq_api_key.strip() or not url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(url):
        st.error('Please enter a valid Url. It can may be a YT video url or website url')

    else:
        try:
            with st.spinner("Waiting..."):
                # Loading the website or yt video data
                if "youtube.com" in url:
                    loader=YoutubeLoader.from_youtube_url(youtube_url=url,add_video_info=False) #add_video_info=True-->Tells us weather we want to add video info or not
                else:
                    loader=UnstructuredURLLoader(urls=[url],ssl_verified=False,
                                                 headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                    # When we are hitting the particular url the web server is also demanding what kind of headers we put on top of it like Which user agent
                    # Those headers are there to make your request look like it’s coming from a real web browser, not a bot. This is extremely important when scraping URLs.
                docs=loader.load()

                ##Chain for Summarization
                chain=load_summarize_chain(llm,chain_type='stuff',prompt=prompt)
                output_summary_chain=chain.run(docs)
                st.success(output_summary_chain)

        except Exception as e:
            st.exception(f"Exception: {e}")
                    

                    

