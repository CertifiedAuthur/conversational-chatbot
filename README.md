# Conversational Q&A Chatbot

Welcome to the **Conversational Q&A Chatbot** project! This chatbot is designed to provide engaging and interactive conversations by utilizing OpenAI's powerful language models. The chatbot is built using Streamlit for the user interface, allowing users to input queries and receive intelligent, context-aware responses.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Conversational Interface:** A user-friendly chat interface that mimics a conversation with a human assistant.
- **Comedic AI Assistant:** The chatbot is configured to respond with a humorous and light-hearted tone.
- **Real-time Response:** Powered by OpenAI's language models, the chatbot generates responses quickly and accurately.
- **API Key Management:** Securely manage your OpenAI API key via the Streamlit sidebar.
- **Session Persistence:** Keeps track of the conversation history within the session, allowing for context-aware replies.

## Demo

A live demo of the chatbot can be accessed at [Chatbot Demo Link](#) (replace with your live link if deployed).

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/CertifiedAuthur/conversational-chatbot.git
   cd conversational-chatbot
   ```

2. **Set Up a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**

   Create a `.env` file in the project root and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your-openai-api-key
   ```

## Usage

1. **Start the Streamlit Application:**

   ```bash
   streamlit run app.py
   ```

2. **Interact with the Chatbot:**
   - Open your web browser and go to `http://localhost:8501`.
   - Enter your OpenAI API key in the sidebar.
   - Type a query in the text box and click "Ask the question" to receive a response.

## Configuration

### OpenAI API Key

To use this chatbot, you'll need an OpenAI API key. You can set this key in two ways:

1. **Environment Variable:** Add your key to a `.env` file as shown in the installation steps.
2. **Streamlit Sidebar:** Enter the API key directly in the sidebar of the Streamlit app.

### Temperature Setting

The chatbot's response creativity is controlled by the `temperature` parameter in the `ChatOpenAI` initialization. Adjust the `temperature` value in `app.py` to tweak the balance between creativity and determinism in responses:

```python
chat = ChatOpenAI(temperature=0.5)  # Lower values make the model more deterministic
```

## Project Structure

```bash
├── app.py                # Main application file
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (e.g., OpenAI API key)
└── README.md             # Project documentation
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
