from rag.generator import Generator

generator = Generator()

response = generator.generate(
    "What is annual leave?"
)

print(response)

