import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
    __version__ = "0.0.0" #Version of the project
    
    REPO_NAME = "Rising-Village-Prediction-Model" #Name of project Reopository at github
    AUTHOR_USER_NAME = "samaTech-sys"#Github username of the developer
    SRC_REPO = "raisingVillage" #Folder with project files 
    AUTHOR_EMAIL = "collinetazuba@gmail.com" #Email of project developer 
    
    setuptools.setup(
        name=SRC_REPO, 
        version=__version__, 
        author=AUTHOR_USER_NAME, 
        author_email=AUTHOR_EMAIL, 
        description="This project develops and trains a predictive model to identify households at risk of not achieving $2/day. This intervention helps stakeholders come up with targeted interventions.", 
        long_description=long_description, 
        long_description_content_type="text/markdown", 
        url="https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}", 
        project_urls={
            "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
        }, 
        package_dir={"": "src"}, 
        packages= setuptools.find_packages(where="src")
    )