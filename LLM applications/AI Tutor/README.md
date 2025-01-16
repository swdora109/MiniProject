# AI Tutor: An Interactive Language Learning Tool 🌐

Welcome to the AI Tutor project! This repository contains the code for an AI-powered tutoring system built using LangChain. The system is designed to enhance language learning for Korean-speaking English learners through personalized feedback and advanced text-to-speech capabilities.


## Table of Contents
- [Key Features](#key-features-)
- [Usage](#usage-)
- [Example](#example-)
- [What I Learned](#what-i-learned-)
- [Technologies Used](#technologies-used-)
- [Limitations and Contribution Notes](#limitations-and-contribution-notes-)
- [How to Contribute](#how-to-contribute-)
- [Acknowledgments](#acknowledgments-)
  <br> <br>


## Key Features 🎨
### Scoring Feedback
- Analyze user-written sentences and provide scores (on a 10.0 scale) for:
  - Vocabulary usage
  - Coherence
  - Clarity
  - Overall quality

### Grammar Assistance
- Detect grammatical errors and provide explanations in Korean.
- Suggest corrected versions of sentences.

### Text-to-Speech Integration
- Listen to the pronunciation of corrected sentences.
- Improve language learning with auditory support.

### Modular and Extensible Design
- Customize and expand the tutor for various subjects and languages with ease. <br> <br>

## Usage 🔧
1. Input a sentence into the tutor.
2. Receive scores (on a 10.0 scale) for vocabulary, coherence, clarity, and overall quality.
3. Review explanations for grammar issues in Korean and view suggested corrections.
4. Use the text-to-speech feature to listen to the corrected sentence and practice pronunciation. <br> <br>


## Example 📝

#### Initial Screen 🖥️
<img width="1250" alt="main" src="https://github.com/user-attachments/assets/1a0fe1f5-2716-45bc-b446-94ba49a31235" />

### Input:
She don't like to eat apples because they doesn't taste good to her and she think they are too hard to chew, but her brother say that apples are his favorite fruit and he always tell her that she should try to eat them more often.

### Output:
- **Grammar Issue**: 
  - 'She don't like' should be corrected to 'doesn't'.
  - 'they doesn't taste' should be corrected to 'don't'.
  - 'she think' should be corrected to 'thinks'.
  - 'her brother say' should be corrected to 'says'.
  - 'he always tell' should be corrected to 'tells'.

- **Corrected Sentence**: She doesn't like to eat apples because they don't taste good to her and she thinks they are too hard to chew, but her brother says that apples are his favorite fruit and he always tells her that she should try to eat them more often.
- **Scores**: Vocabulary: 6 / 10, Coherence: 5 / 10, Clarity: 5 / 10, Overall score: 5 / 10
- **Text-to-Speech**: Plays audio of the corrected sentence. <br> <br>

#### Output Screen 🖥️
<img width="1255" alt="image" src="https://github.com/user-attachments/assets/607ecb88-bf6e-4b34-906a-3c349f41d0fe" />
<br> <br>

## What I Learned 🌟
Through developing this AI Tutor project, I have gained valuable insights and skills, including:
- **AI and Language Processing**: Understanding the intricacies of natural language processing (NLP) and how to leverage LangChain for building a conversational AI.
- **Error Detection and Feedback**: Developing algorithms to accurately detect grammatical errors and provide constructive feedback to users.
- **Text-to-Speech Integration**: Integrating text-to-speech APIs to enhance the user experience through auditory learning.
- **Modular and Extensible Design**: Designing the system in a way that allows for easy customization and expansion to other subjects and languages.
- **Prompt Engineering and Parameter Adjustment**: Recognizing the critical importance of crafting effective prompts and fine-tuning parameters to achieve optimal AI performance and user interaction.

**As an experienced language teacher with over four years of teaching the Korean language, working on this project has been particularly fulfilling. It has allowed me to contribute to the development of an advanced educational tool aimed at enhancing language acquisition. This experience has not only honed my technical skills but also expanded my understanding of how AI can be effectively applied to real-world language learning challenges.** <br> <br>


## Technologies Used 🛠️
- LangChain: For building conversational AI.
- Python: For backend logic and processing.
- Text-to-Speech API: For generating audio output. <br> <br>


## Limitations and Contribution Notes 📋
This project requires private API keys for certain functionalities (e.g., text-to-speech services). As a result, contributions may be limited unless contributors have access to the required API keys. <br> <br>


## How to Contribute 🎓
We welcome contributions to improve AI Tutor! To get started:
1. Fork the repository.
2. Create a new branch for your feature:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add new feature"
    ```
4. Push your branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request for review. <br> <br>


## Acknowledgments 🤝
- LangChain
- Contributors and the open-source community


Thank you for exploring the AI Tutor project! We hope it aids in enhancing language learning experiences.

