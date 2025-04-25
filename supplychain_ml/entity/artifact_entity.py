from dataclasses import dataclass #its a decorator which creates a variable for an empty class without any functions


@dataclass
class DataIngestionArtifact:
    trained_file_path: str
    test_file_path: str
    

