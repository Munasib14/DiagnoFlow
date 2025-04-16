import os

project_structure = {
    "chestxray_groq_pipeline": {
        "app": {
            "api": {
                "v1": ["endpoints.py"],
                "__files__": ["dependencies.py"]
            },
            "core": ["config.py", "logger.py"],
            "services": [
                "ocr.py",
                "data_preprocessing.py",
                "nlp_pipeline.py",
                "llm_chain.py",
                "vector_store.py",
                "image_utils.py",
                "database.py",
                "monitoring.py"
            ],
            "models": ["schemas.py"],
            "tasks": ["celery_worker.py"],
            "utils": ["file_handler.py"],
            "__files__": ["main.py", "__init__.py"]
        },
        "db": {
            "chroma": []
        },
        "data": {
            "raw": [],
            "processed": []
        },
        "logs": ["runtime.log"],
        "tests": ["test_api.py", "test_ocr.py", "test_llm_chain.py"],
        "docker": ["Dockerfile", "docker-compose.yml"],
        "__files__": [
            ".env",
            "requirements.txt",
            "run.sh",
            "README.md"
        ]
    }
}

def create_structure(base_path, struct):
    for key, value in struct.items():
        if key == "__files__":
            for file in value:
                open(os.path.join(base_path, file), 'a').close()
        else:
            dir_path = os.path.join(base_path, key)
            os.makedirs(dir_path, exist_ok=True)
            if isinstance(value, dict):
                create_structure(dir_path, value)
            elif isinstance(value, list):
                for file in value:
                    open(os.path.join(dir_path, file), 'a').close()



if __name__ == "__main__":
    create_structure(".", project_structure)
    print("Project structure created successfully.")