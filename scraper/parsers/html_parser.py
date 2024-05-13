import re
import time
import json

class Simplifier():
    def __init__(self):
        self.input_file = "temp_data.txt"
        self.output_file = "final.json"
        self.computer_science_skills = [
    "design patterns",
    
    "agile methodologies",
    "version control",
    "debugging",
    "problem solving",
    "unit testing",
    "integration testing",
    "continuous integration",
    "continuous deployment",
    "web development",
    "mobile development",
    "cloud computing",
    "containerization",
    "microservices",
    "restful APIs",
    "graphql",
    "database management",
    "big data",
    "natural language processing",
    "computer vision",
    "data analysis",
    "data visualization",
    "cybersecurity",
    "networking",
    "operating systems",
    "devops",
    "automation",
    "scripting",
    "shell scripting",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "google cloud platform",
    "terraform",
    "ansible",
    "jenkins",
    "git",
    "github",
    "bitbucket",
    "jira",
    "slack",
    "docker-compose",
    "bash",
    "python",
    "javascript",
    "typescript",
    "java",
    "c++",
    "c#",
    "ruby",
    "go",
    "rust",
    "php",
    "sql",
    "html",
    "css",
    "react",
    "angular",
    "vue.js",
    "node.js",
    "express.js",
    "flask",
    "django",
    "spring boot",
    "laravel",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "keras",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "plotly",
    "tensorflow.js",
    "tensorflow lite",
    "opencv",
    "nltk",
    "spacy",
    "puppeteer",
    "selenium",
    "pytest",
    "jest",
    "mocha",
    "chai",
    "karma",
    "protractor",
    "postman",
    "swagger",
    "grafana",
    "prometheus",
    "elasticsearch",
    "kibana",
    "logstash",
    "splunk",
    "mongoDB",
    "mysql",
    "postgresql",
    "sqlite",
    "oracle",
    "redis",
    "firebase",
    "cassandra",
    "apache kafka",
    "rabbitMQ",
    "nginx",
    "apache",
    "tomcat",
    "jboss",
    "linux",
    "unix",
    "windows",
    "macos",
    "ios",
    "android",
    "raspberry pi",
    "arduino",
    "ansible",
    "chef",
    "puppet",
    "saltstack",
    "terraform",
    "vault",
    "kubernetes",
    "openshift",
    "istio",
    "helm",
    "prometheus",
    "grafana",
    "jaeger",
    "elasticsearch",
    "logstash",
    "kibana",
    "docker",
    "docker-compose",
    "jenkins",
    "travis CI",
    "circleCI",
    "gitlab CI",
    "github actions",
    "aws",
    "azure",
    "google cloud platform",
    "terraform",
    "ansible",
    "serverless",
    "lambda",
    "cloud functions",
    "api gateway",
    "s3",
    "ec2",
    "rds",
    "dynamodb",
    "cloudwatch",
    "sns",
    "sqs",
    "vpc",
    "route53",
    "cloudfront",
    "cognito",
    "iam",
    "azure functions",
    "azure app service",
    "azure cosmos db",
    "azure devops",
    "azure functions",
    "google cloud functions",
    "google app engine",
    "google cloud SQL",
    "google cloud storage",
    "firebase",
    "firebase authentication",
    "firebase firestore",
    "firebase real-time database",
    "firebase storage",
    "firebase functions",
    "firebase hosting",
    "firebase analytics",
    "firebase performance monitoring",
    "firebase remote config",
    "firebase test lab",
    "firebase crashlytics",
    "firebase dynamic links",
    "firebase in-app messaging",
    "firebase app indexing",
    "firebase cloud messaging",
    "firebase ML Kit",
    "firebase ML Kit for Firebase",
    "firebase ML Kit SDK",
    "firebase A/B Testing",
    "firebase app distribution",
    "firebase App Store Connect",
    "firebase cloud storage",
    "firebase ML Kit",
    "firebase notifications",
    "firebase performance",
    "firebase push notifications",
    "firebase remote configuration",
    "firebase test lab",
    "firebase user engagement",
    "firebase dynamic links",
    "firebase hosting",
    "firebase in-app messaging",
    "firebase app indexing",
    "firebase crashlytics",
    "firebase analytics",
    "firebase predictions",
    "firebase A/B testing",
    "firebase ML",
    "mariadb"
]
        self.data = self.convert_data()
        self.fields = [
            "front end",
            "back end",
            " ui ",
            " ux ",
            "data science",
            "artificial intelligence",
            " ai ",
            "devops",
            "cyber security",
            "networks",
            "computer vision",
            "designer",
            " ml ",
            "deep learning",
            "full stack",
            "full-stack",
            "web development"
            "ui ",
            "ux ",
            "ai ",
            "ml ",
            " ai",
            " ux",
            " ui",
            " ml",
        ]
    def convert_data(self):
        #converts the raw file into a list of lists
        with open('temp_data.txt','r', encoding='utf-8') as file:
            contents = file.read()

        raw_lists = contents.strip().split('][')
        lists = []
        for raw_list in raw_lists:
            cleaned_list = '[' + raw_list.strip('[]') + ']'
            lists.append(eval(cleaned_list))
        return lists

    def clean_raw_description(self):
        #removes html tags,newlines,other junk
        for list in self.data:
            list[-1] = re.sub(r'<[^>]*>', ' ', list[-1])
            list[-1] = re.sub('\n',' ',list[-1])
            list[-1] = re.sub(r'show more|show less', '', list[-1]).strip()


    def get_skills(self,text): 
        #checks to see if skills in the skill list occur in the text
        skill_list = []
        for skill in self.computer_science_skills:
            x = re.search(f'({skill.lower()} )',text)
            if x!=None:
                skill_list.append(skill)
        return skill_list
    
    def getfields(self,text): #gets fields based on the job titles
        field = []
        for i in self.fields:            
            if  re.search(f'({i})',text.lower()):
                if i in ["computer vision" ," ai ","artificial intelligence" ," ml " , "deep learning","ml"," ai"," ml","ai ","ml "]:
                    i = "ai"
                elif i in ["front end","back end" ," ui " ," ux " ,"full stack","full-stack","designer"," ui"," ux","ux ","ui "]:
                    i = "web development"
                field.append(i)
        if len(field)>0:            
            return field[0]
        else:
            return ""


    def simplify_data(self):
        self.clean_raw_description()
        all_lists = []
        for list in self.data:
            skills = self.get_skills(list[-1])
            field =  self.getfields(list[1])
            list[-1] = skills
            list.append(field)
            all_lists.append(list)
        self.store(all_lists)
        

    def store(self,data):
        
        with open('final.json','a',encoding='utf-8') as file:
            
            file.write("[" + "\n")
            for list in data:
                dict_data = {
                    "title" : list[1],
                    "company" : list[2],
                    "location" : list[3],
                    "post-date" : list[4],
                    "skills" : list[5],
                    "fields" : list[6],
                }
                formatted_data = json.dumps((dict_data),ensure_ascii=False)
                file.write(formatted_data + ",\n")
            file.write("]")
p = Simplifier()

p.simplify_data()