from langchain_core.prompts import ChatPromptTemplate
import google.generativeai as genai

from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_GEMINI_API_KEY'))

template = (
    "You are an expert summarizer and information extractor. Your task is to analyze and summarize the following text content from a web page's DOM: {dom_content}"
    "Please follow these instructions carefully:"
    "1. **Extract Key Insights:** Thoroughly analyze the text and extract the most important insights. Prioritize information that is central to the main topic or argument of the text."
    "2. **Provide a Concise Summary:** Create a clear and concise summary of the key points. Aim for clarity and brevity while ensuring all crucial information is included."
    "3. **Include Relevant Examples:** Where appropriate, include brief examples from the text to illustrate key points. These examples should be directly relevant and help to clarify or reinforce the main ideas."
    "4. **Maintain Context:** Ensure that the extracted information and summary maintain the context and intent of the original content. Avoid misrepresenting or oversimplifying complex ideas."
    "5. **Use Clear Structure:** Organize the summary in a logical structure. Use bullet points or numbered lists for distinct ideas or steps, if applicable."
    "6. **Highlight Important Terms:** Identify and include any important terms, concepts, or definitions that are crucial to understanding the content."
    "7. **Quantify When Possible:** If the text includes significant statistics, numbers, or data points, include these in your summary."
    "8. **Indicate Uncertainty:** If any part of the text is ambiguous or open to interpretation, briefly note this in your summary."
    "9. **Length and Detail:** Aim for a summary that captures the essence of the content in about 3-5 paragraphs or 15-20 bullet points, depending on the complexity and length of the original text. Adjust as necessary to fully capture key insights."
    "10. **Focus on Relevance:** Ensure all extracted information is directly relevant to the topic. Omit tangential or irrelevant details."
    "11. **No Additional Commentary:** Do not include any personal opinions, analysis, or extra information not present in the original text."
    "Your output should be a well-structured, informative summary that captures the key insights of the text and provides relevant examples. Ensure your summary would be understandable and valuable to someone who hasn't read the original text."
)


def parse_with_gemini(dom_chunks):
    prompt = template.format(
        dom_content="\n".join(i for i in dom_chunks)
    )
    model = genai.GenerativeModel('gemini-1.5-flash')
    # chain = prompt | model
    
    response = model.generate_content(prompt)

    return response.text
