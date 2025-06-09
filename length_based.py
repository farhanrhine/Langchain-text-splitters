from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('C:/text-splitters/langchain-text-splitters/Entrepreneurship.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)

print("page content of result is ",result[0].page_content)
print("length of result is ",len(result))
print("metadata of result is ",result[0].metadata)
