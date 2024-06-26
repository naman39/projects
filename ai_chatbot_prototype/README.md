# AI Chatbot Prototype

Welcome to the AI Chatbot prototype repository! This prototype is built using **langflow**, integrating ASTRA DB vector database and utilizing the OpenAI API to power the chatbot and generate embeddings.

## Getting Started

To run this prototype on your machine, follow these instructions:

### Prerequisites

- Python 3.10 is required. Note that some versions beyond 3.12 might not be compatible.
- Ensure you have pip installed.
- You will find the api keys and endpoint in AstraDB missing: use the following and run the application:
- **OPEN_AI_API:** sk-proj-oLlx7MEPC0JjZbHdwl8MT3BlbkFJm0UZVjAo6v8cB5wmBbDY
- **ASTRA-TOKEN:** AstraCS:ELXAmQGxpdqNPzFlwCZOKtrP:a0ee4e5eb0637762c2021fc376df11cbbb4b6003fcf5a847b50b029c1693e81a
- **ASTRA-ENDPOINT:** https://9b5ddf64-0fdf-4a56-83d2-7b10d29ca544-us-east1.apps.astra.datastax.com
- **ASTRA-COLLECTION:** pdf

### Installation

Install **langflow** and its dependencies:

#### Mac/Linux:

```pip3 install langflow --pre --force-reinstall```

#### Windows:

```pip install langflow --pre --force-reinstall```

### Running the Chatbot

1. After installing **langflow**, navigate to the project directory in your terminal or command prompt.
   
2. Execute the following command to start the chatbot:

```langflow run```

3. A GUI window might open up, resembling this: ![Screenshot 2024-06-17 at 5 13 46 AM](https://github.com/naman39/projects/assets/59209974/d18de078-6296-4d44-9a21-dddf1b658c07)
 Drag and drop your JSON file to view its structure.

4. Click on "Run" to execute the chatbot.

## Additional Notes

- **langflow** provides the underlying framework for this chatbot prototype, facilitating easy integration and development.
- Ensure your Python environment is set up correctly with the required dependencies before running the chatbot.

<img width="813" alt="Screenshot 2024-06-17 at 5 23 58 AM" src="https://github.com/naman39/projects/assets/59209974/e4352ccc-0cb1-4c24-a0ff-1ba6f98eba35">

## Thank you!

Thank you for exploring my chatbot prototype. Feel free to contribute, raise issues, or provide feedback. Happy chatting!

---
