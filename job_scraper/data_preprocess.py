import re
from collections import Counter
import json

import nltk
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag


# Function to clean the text data
def clean_text(text):
    text = re.sub(r'[^\w\s]', '$', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespaces
    text = text.lower()  # Convert to lowercase
    return text

# Function to extract keywords and technologies
def extract_keywords(data):
    keyword_list = []
    word_trash = ["experience", "ability", "work", "must", "etc", "g", "familiarity", "knowledge", "required", "engineering", "development", "self", "able", "proficiency", "assist", "learn", "collaborate", "hands", "related field", "work independently", "support", "internship", "electrical engineering", "working", "preferred", "others", "solving skills", "familiar", "experience working", "business", "well", "world", "understanding", "time", "part", "contribute", "planning", "results", "duration", "interest", "economics", "currently pursuing", "projects", "technology", "related fields", "end", "pursuing", "high", "problem", "non", "one", "design", "analysis", "create", "science", "candidate", "software development", "variety", "real", "stakeholders", "written", "candidates", "1 year", "program", "research", "help", "cross", "develop", "commitment", "proficient", "strong analytical", "business analytics", "tools", "security", "students", "assists", "learning", "monday", "university", "communication skills", "duties", "verbal", "verbal communication skills", "avaliable", "intern", "finance", "excellent communication skills", "reports", "opportunity", "work closely", "interns", "fast", "information", "perform", "procedures", "reccomendations", "2023", "friday", "desire", "detail", "focus", "needed", "application", "basic knowledge", "critical thinking", "starter", "hour", "equivalent experience", "graduate", "collaboration", "physics", "implementation", "critical thinking", "starter", "hour", "project", "programming languages", "use", "network", "excellent written", "team environment", "dental", "following areas", "good communication", "recognition", "motion", "teamwork skills", "creating", "testing", "communications", "employment", "first", "company","customers", "maintenance","state", "product", "spark" ,"production","software","team members" ,"identify opportunities","good communication skills","assigned","build","cleaning","improvement","organization","passions","u","set","0","study","4","medical","reporting","strong background","training","major","summarize research findings","patent submissions","publication record","first robotics","inspiration","awim", "iclr"]

    # technology_keywords = ["python", "r using advanced modeling techniques", "developing tableau dashboards", "presenting tableau dashboards", "data visualization techniques", "hoc sql queries", "undergraduate", "graduate degree", "mathematics", "present data", "preferably tableau", "preferably python", "sql", "r", "statistics", "computer science", "matlab", "git preferred", "scrum", "azure cloud", "devops", "machine learning", "ai","bachelors program", "clear visualizations", "devops experience", "synthesize complex data", "modern machine learning techniques", "multimodal machine learning", "deep learning", "ai multimodal representation", "generative media", "based computer vision", "master", "ph", "artificial intelligence", "deep learning architecture", "training multimodal deep learning architectures", "frameworks like pytorch", "tensorflow", "help achieve business targets using r", "develop visualizations", "data analysis", "pandas", "numpi", "numpy", "clustering", "classification techniques", "visualize", "microsoft azure", "azure", "utilize python programming language", "bachelor", "azure storage", "python programming", "data manipulation", "natural language processing", "ai techniques", "java", "c", "html", "javascript", "css", "language models", "gpt", "cloud services", "aws", "google cloud", "bs", "ms", "go", "ruby", "mysql", "ms sql", "kafka", "airflow", "splunk", "ml model", "sas", "python programming language", "data visualization tools", "powerbi", "tableau", "hyperion", "brio", "analyzing data", "data collection", "algorithms", "machine learning concepts", "phd", "computer vision", "neural networks", "hive", "hadoop", "nosql databases", "mongodb", "neo4j", "neptune", "cassandra", "hbase", "cypher", "gremlin","applied mathematics", "nlp", "natural language generation", "nlg", "nlu", "natural language understanding", "unsupervised learning", "ml libraries like tensorflow", "pytorch", "ml", "nlp problem", "excel", "matplotlib", "seaborn", "tidyverse packages like dplyr", "tidymodels", "ggplot", "packages like caret", "bayesian statistics", "cloud", "gcp", "microsoft word", "powerpoint", "ml technologies", "ml frameworks", "frameworks", "data processing technologies", "apache hadoop", "tensor flow", "data scructures", "data modeling", "elk stack", "contianer technology", "aws services including s3", "amazon ecs", "edge machine learning", "familiarity using python", "phd graduates", "currently enrolled master", "recent master", "phd students", "sklearn", "various machine learning techniques", "bayesian methods", "faire", "deep learning frameworks including pytorch", "nvidia triton", "mlops concepts", "ml pipelines", "machine learning pipeline", "performing data analysis", "visualization techniques", "maintain complex data pipelines", "databases", "experience using r", "experience using sql", "produce engaging data visualizations", "git", "version control systems", "docker", "r shiny", "bi", "qlik", "data mining", "predictive analytics", "product development including visualizaitons", "build scaled data engineering algorithms", "large data sets using python", "advanced python", "sql skills", "visualization", "experience using data mining", "visualization tools like tableau", "viya preffered", "tools like aws", "sagemaker preferred", "microsoft office product required", "excel preferred", "datasets", "analysis pipeline", "jenkins", "kubernetes", "redis", "openai", "build articicial intelligence algorithms utilizing machine learning", "chatgpt", "sql query management", "elt design", "mine large amounts", "perform data analysis", "predictive analytics solutions", "end pipeline", "machine learning model", "machine learning approaches", "natural language processes", "internal r", "data mining algorithms", "snowflake", "basic sql programming experience", "microsoft excel", "technologies like git", "linux", "ml techniques", "data etl includes identifying", "ml models", "ml solutions","current processes using ai", "program prototypes jupyter notebooks", "use aws instances", "operate ai", "reinforcement learning", "transfer learning", "visualizations", "big data skills", "recent deep learning platforms", "snorkel", "database skills", "microsoft office", "visualization experience", "microsoft power bi", "gis", "google analytics", "build predictive models", "ai algorithms perofrmance", "ai team", "llm", "large language models", "hugging face", "iccv", "sql query", "create etl pipelines", "optimal database schema", "data pipeline architecture", "data visualization tool", "data pipeliens", "database engineering concepts", "gitlab", "ai chatbot", "solve ai", "emerging ai trends", "ai technologies", "improving data collection", "creating visualizations","power bi", "linux os", "ubuntu", "read hat", "windows", "java architectural solutions", "cloud native architecture", "google cloud platform", "ws","ml concepts", "aws cloud", "chatbots using platforms", "conversational ai models using frameworks", "hugging face", "math", "stats", "writting api", "postman","deep learning framework", "visual", "applying deep learning", "ms office applications", "generative ai", "load unsctructured data", "microsoft office programs", "especially excel", "nlp techniques", "keras", "torch", "neural network frameworks", "tensorflow", "py", "moicrosoft power bi", "knowledge using data visualization tools", "plotly", " spark nlp", "nosql data base", "data interfacing", "time mlops dashboards","cloud architecture", "art machine learning models", "natural language processing tasks including information extraction", "master student", "elnlp", "deep learning technologies", "top nlp", "machine learning venues", "specific nlp tasks", "master degree", "information extraction", "developing nlp models", "api guided text generation", "language generation tasks", "developing nlp models", "apply machine learning models", "architects", "gpgpu architectures", "cpu architectures", "excellent c", "compute apis", "cuda", "opencl", "vulkan etc", "ml networks", "pytorch desireable", "os", "machine learning systems", "python development", "mxnet", "least one deep learning framework", "gpu implementations", "latest dl research", "nvidia", "dl frameworks", "excellent python skills", "gpu programming", "developing computer vision", "machine learning algorithms", "sfm", "solid python", "opencv", "language modeling", "vector", "microsoft suite", "google suite", "ms excel", "sas experience", "vector calculus", "level python", "modern deep learning techniques", "cnns", "basic computer vision concepts", "opengl", "art ml models", "deep reinforcement learning", "using python", "machine learning platforms", "different machine learning domains like natural language processing", "computer vision applications", "optimize sql queries", "tableau preferred", "reinforcement learning algorithms", "imitation learning", "currently pursuing ms", "linux systems", "developing machine learning models", "least one popular deep learning framework", "least one popular deep learning framework", "deep neural network architectures", "generative models", "classical machine learning models", "database administration", "microsoft sql server database engine", "sql server reporting services", "sql server integration services", "strong excel fundementals", "sql scripts", "dc gpu performance team", "ml workload execution", "python skills", "including opencv", "pillow", "streamlit", "accessing rtsp streams", "api", "mlops skills", "git version control system", "docker swarm mode", "ci", "cd", "pipelines", "cv", "phd student", "persuing phd", "large language model", "database tools", "database programming experience", "run machine learning model", "debugging", "debugging data processing scripts", "amazon web services"]

    for job in data:
        obj = {
            "title": job['title'],
            "reqs": "",
            "vectorized": [],
            "link": job['link']
        }
        for req in job['reqs']:
            cleaned_req = clean_text(req)
            tokens = word_tokenize(cleaned_req)

            # Remove stopwords
            stop_words = set(stopwords.words('english'))

            # tokens = [token for token in tokens if token not in stop_words]
            formatted_tokens = []
            for token in tokens:
                if token not in stop_words:
                    formatted_tokens.append(token)
                else:
                    formatted_tokens.append("$")

            # Extract keywords and technologies
            current_group = []

            for item in formatted_tokens:
                if item == "$":
                    if current_group:
                        obj['reqs'] = obj['reqs'] + " " + " ".join(current_group)
                        current_group = []
                else:
                    current_group.append(item)

            # Add the last group if it exists
            if current_group:
                obj['reqs'] = obj['reqs'] + " " + " ".join(current_group)
            # tagged_keyword_list = pos_tag(obj['reqs'])
            # obj["reqs"] = [word for word, tag in tagged_keyword_list if tag != 'VB' and word not in word_trash ]
            keyword_list.append(obj)

    return keyword_list

# Data provided in the question
# data = [
#     {"name": "Data Science Intern\n- job post", "reqs": ["Assist in data collection, cleaning, and preprocessing tasks to ensure high-quality datasets for analysis.", "Conduct data analysis using statistical methods and data visualization techniques.", "Support the development and implementation of machine learning models and algorithms.", "Collaborate with the team to identify areas for improvement and contribute to data-driven solutions.", "Assist in the creation of data visualizations and reports to communicate findings to stakeholders.", "Stay updated on the latest trends and advancements in data science and apply them to the internship projects.", "Learn from experienced data scientists and professionals in the field, seeking guidance and feedback.", "Collaborate with cross-functional teams, including developers and product managers, to support data-driven decision-making.", "Contribute to the continuous improvement of data processes and methodologies within the organization.", "Currently pursuing a degree in Data Science, Computer Science, Statistics, or a related field.", "Strong analytical skills and a passion for working with data.", "Proficiency in programming languages such as Python or R.", "Familiarity with data manipulation and analysis libraries (e.g., pandas, NumPy).", "Basic understanding of statistical analysis and machine learning concepts.", "Experience with data visualization tools is a plus.", "Excellent problem-solving and critical-thinking abilities.", "Strong communication skills and the ability to work effectively in a team.", "Self-motivated and eager to learn and contribute to data science projects.", "Enthusiasm for the mobile app industry and an interest in data-driven decision-making.", "Ability to adapt to a fast-paced and dynamic work environment.", "Day shift", "Monday to Friday", "Optional: Have you familiarized yourself with the app, are you passionate about finance, which feature do you feel excited to work on? www.redvest.app"]},
#     # Other job postings...
# ]
with open("aggregate_job_info.json", "r") as f:
    data = json.load(f)

mongo_obj = []
for e in data:
    word_trash = ["experience", "ability", "work", "must", "etc", "g", "familiarity", "knowledge", "required", "engineering", "development", "self", "able", "proficiency", "assist", "learn", "collaborate", "hands", "related field", "work independently", "support", "internship", "electrical engineering", "working", "preferred", "others", "solving skills", "familiar", "experience working", "business", "well", "world", "understanding", "time", "part", "contribute", "planning", "results", "duration", "interest", "economics", "currently pursuing", "projects", "technology", "related fields", "end", "pursuing", "high", "problem", "non", "one", "design", "analysis", "create", "science", "candidate", "software development", "variety", "real", "stakeholders", "written", "candidates", "1 year", "program", "research", "help", "cross", "develop", "commitment", "proficient", "strong analytical", "business analytics", "tools", "security", "students", "assists", "learning", "monday", "university", "communication skills", "duties", "verbal", "verbal communication skills", "avaliable", "intern", "finance", "excellent communication skills", "reports", "opportunity", "work closely", "interns", "fast", "information", "perform", "procedures", "reccomendations", "2023", "friday", "desire", "detail", "focus", "needed", "application", "basic knowledge", "critical thinking", "starter", "hour", "equivalent experience", "graduate", "collaboration", "physics", "implementation", "critical thinking", "starter", "hour", "project", "programming languages", "use", "network", "excellent written", "team environment", "dental", "following areas", "good communication", "recognition", "motion", "teamwork skills", "creating", "testing", "communications", "employment", "first", "company","customers", "maintenance","state", "product", "spark" ,"production","software","team members" ,"identify opportunities","good communication skills","assigned","build","cleaning","improvement","organization","passions","u","set","0","study","4","medical","reporting","strong background","training","major","summarize research findings","patent submissions","publication record","first robotics","inspiration","awim", "iclr"]
    

# Generate a list of possible keywords from the data
keyword_freq = extract_keywords(data=data)
# # print(keyword_freq)
# counted = Counter(keyword_freq)
# print(counted)
# print(len(counted))

with open("technology_keywords.json", "w") as f:
    json.dump(keyword_freq, f)

# Print keyword frequencies
# print("Keyword Frequencies:")
# for keyword, freq in keyword_freq.items():
#     print(keyword, "-", freq)

