# Customer Support Assistant - Supervised Fine-Tuning Project

A comprehensive project demonstrating **Supervised Fine-Tuning (SFT)** techniques for creating a specialized customer support assistant. This project showcases the complete pipeline from dataset preparation to deployment of a fine-tuned language model.

## 🎯 Project Overview

This project focuses on learning and implementing **Supervised Fine-Tuning (SFT)** to create a customer support assistant. The model has been fine-tuned on customer support conversations to provide contextually appropriate and helpful responses to support queries.

## 📁 Project Structure

```
rlhf-and-sft-test/
├── README.md                     # This file
├── .gitignore                    # Git ignore file
└── Plain-SFT/                    # 🔥 Main SFT Implementation
    ├── app.py                    # Gradio web interface for testing
    ├── prompts.py                # Prompt templates and utilities
    ├── requirement.txt           # Project dependencies
    ├── Supervised_FineTuning.ipynb  # 📚 Complete SFT tutorial notebook
    └── __pycache__/              # Python cache files (auto-generated)
```

## 🚀 Key Features

- **Complete SFT Pipeline**: End-to-end supervised fine-tuning implementation
- **Interactive Web Interface**: Gradio-based chat interface for testing the fine-tuned model
- **Educational Focus**: Detailed notebook explaining SFT concepts and implementation
- **Customer Support Specialization**: Model fine-tuned specifically on customer support conversations

## 🛠️ Fine-Tuning Process

The project demonstrates a complete SFT workflow located in the [`Plain-SFT/`](Plain-SFT/) directory:

1. **Data Preparation**: Customer support conversation datasets
2. **Model Selection**: Base model selection and configuration
3. **Training Pipeline**: Supervised fine-tuning implementation
4. **Evaluation**: Model performance assessment
5. **Deployment**: Web interface for interaction testing

## 📖 Learning Resources

### Main Tutorial: [`Plain-SFT/Supervised_FineTuning.ipynb`](Plain-SFT/Supervised_FineTuning.ipynb)

This comprehensive Jupyter notebook contains:
- SFT theory and fundamental concepts
- Step-by-step implementation guide
- Dataset preparation techniques
- Training loop and optimization strategies
- Model evaluation methods
- Best practices and troubleshooting tips

## 🔧 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd rlhf-and-sft-test
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   cd Plain-SFT
   pip install -r requirement.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

## 📋 Key Files Description

### [`Plain-SFT/app.py`](Plain-SFT/app.py)
- Main application file with Gradio web interface
- Loads and serves the fine-tuned customer support model
- Handles conversation history and response generation
- Provides interactive testing environment

### [`Plain-SFT/prompts.py`](Plain-SFT/prompts.py)
- Contains prompt templates and formatting utilities
- Manages conversation structure for the assistant
- Implements proper prompt formatting for the fine-tuned model

### [`Plain-SFT/Supervised_FineTuning.ipynb`](Plain-SFT/Supervised_FineTuning.ipynb)
- **Core educational content** - Complete SFT tutorial and implementation
- Dataset preparation and preprocessing steps
- Model training and fine-tuning code
- Evaluation metrics and model assessment
- Export and deployment preparation

### [`Plain-SFT/requirement.txt`](Plain-SFT/requirement.txt)
- Lists all Python dependencies required for the project
- Includes packages for model training, web interface, and data processing

## 🎓 Learning Objectives

This project teaches:
- **Supervised Fine-Tuning fundamentals** and best practices
- Dataset preparation techniques for conversational AI
- Training pipeline implementation and optimization
- Model evaluation and validation strategies
- Deployment approaches for fine-tuned language models

## 🚀 Usage

1. **Start the application**: 
   ```bash
   cd Plain-SFT
   python app.py
   ```

2. **Access the interface**: Open your browser to the provided local URL (typically `http://127.0.0.1:7860`)

3. **Chat with the assistant**: Enter customer support queries to test the fine-tuned model

4. **Explore the notebook**: Study the [`Supervised_FineTuning.ipynb`](Plain-SFT/Supervised_FineTuning.ipynb) for detailed implementation

## 🎯 Model Details

- **Training Method**: Supervised Fine-Tuning (SFT)
- **Domain Specialization**: Customer support conversations
- **Interface**: Gradio web application for easy testing
- **Implementation**: Complete pipeline from data preparation to deployment

## 🤝 Contributing

This is an educational project focused on learning SFT techniques. Feel free to:
- Explore the code and notebooks
- Modify the implementation for your own datasets
- Extend the functionality for other domains
- Share improvements and learnings

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**🎓 Educational Note**: This project is designed to teach Supervised Fine-Tuning concepts through hands-on implementation. The [`Plain-SFT/`](Plain-SFT/) directory contains all the core learning materials, with the [`Supervised_FineTuning.ipynb`](Plain-SFT/Supervised_FineTuning.ipynb) notebook serving as the primary educational resource for understanding SFT implementation.