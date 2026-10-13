from bs4 import BeautifulSoup

def analyze_seo(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(),'html.parser')

    print("="*40)
    print("Seo Analysis report")
    print("="*40)

    title = soup.title.string if soup.title else "No Title Found"
    print(f"Title Tag : {title}")

    h1_tags = [h1.text.strip() for h1 in soup.find_all('h1')]
    print(f"H1 Count : {len(h1_tags)}")
    print(f"H1 Content : {h1_tags}")

    meta_desc = soup.find('meta', attrs={'name' : 'description'})
    desc_content = meta_desc['content'] if meta_desc else "Missing Meta Description"
    print(f"Meta Decsription: {desc_content}")

    print("=" *40)

if __name__ == "__main__":
    analyze_seo("Practical2/index.html")
