# NewsGuardian

NewsGuardian is a real-time news verification tool designed to combat misinformation and enhance news literacy. Leveraging the power of Phi-2, GPT-4, and advanced text-to-speech models, NewsGuardian analyzes and verifies news articles, fact-checks claims, and provides users with reliable sources and context to navigate the news landscape effectively.

## Features

- **Real-Time Analysis:** Analyze news articles in real-time using Phi-2 and GPT-4.
- **Fact-Checking:** Fact-check claims and statements against a database of verified sources.
- **Contextualization:** Provide users with additional context and background information.
- **Text-to-Speech Integration:** Generate audio summaries of news articles for accessibility.

## How it Works

1. **Input:** Users input a news article URL or text into the NewsGuardian interface.
2. **Analysis:** NewsGuardian utilizes Phi-2 and GPT-4 to analyze the content.
3. **Verification:** Cross-references the information against a database of verified sources.
4. **Output:** Generates a comprehensive report summarizing the analysis and highlighting any misinformation detected.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Jaweria-B/NewsGuardian.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   streamlit run app.py
   ```

## Usage

1. Input a news article URL or text into the provided interface.
2. Wait for NewsGuardian to analyze and verify the content.
3. Review the generated report, which includes information on misinformation and recommended actions.

## Future Directions

- **Expansion of Language Support:** Support for a wider range of languages.
- **Integration with Social Media Platforms:** Provide real-time fact-checking on popular social media platforms.
- **Collaboration with News Organizations:** Provide additional context, analysis, and fact-checking services within news articles.

## Contributing

Contributions are welcome! If you'd like to contribute to NewsGuardian, please fork the repository and submit a pull request with your changes.

## Acknowledgements

- Special thanks to OpenAI for providing access to Phi-2 and GPT-4 models.
- Text-to-speech models utilized in this project are courtesy of [Model Zoo](https://modelzoo.co/).

