# Web scraping script to load and parse specific content from a blog post

from langchain_community.document_loaders import WebBaseLoader
import bs4

# Load and parse specific content from a blog post
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    # Parse only the content within the specified classes
    bs_kwargs=dict(parse_only=bs4.SoupStrainer(class_=["post-title", "post-content"]))
    )
docs = loader.load()

print(docs[0])


