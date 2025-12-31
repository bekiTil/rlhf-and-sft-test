# Customer Support Assistant - Advanced Fine-Tuning Project

A comprehensive project demonstrating **Supervised Fine-Tuning (SFT)** and **Reinforcement Learning with Direct Preference Optimization (DPO)** techniques for creating a specialized customer support assistant. This project showcases the complete pipeline from dataset preparation to deployment of fine-tuned language models.

## 🎯 Project Overview

This project focuses on learning and implementing advanced fine-tuning techniques:
- **Supervised Fine-Tuning (SFT)** to create a customer support assistant
- **Direct Preference Optimization (DPO)** to align the model with human preferences

Both models have been fine-tuned on customer support conversations to provide contextually appropriate and helpful responses to support queries.

## 📁 Project Structure

```
rlhf-and-sft-test/
├── README.md                     # This file
├── .gitignore                    # Git ignore file
├── Plain-SFT/                    # 🔥 Supervised Fine-Tuning Implementation
│   ├── app.py                    # Gradio web interface for SFT model
│   ├── prompts.py                # Prompt templates and utilities
│   ├── requirement.txt           # Project dependencies
│   ├── Supervised_FineTuning.ipynb  # 📚 Complete SFT tutorial notebook
│   └── __pycache__/              # Python cache files (auto-generated)
└── RL-dpo/                       # 🚀 Direct Preference Optimization Implementation
    ├── app.py                    # Gradio web interface for DPO model
    ├── prompts.py                # Prompt templates for DPO model
    ├── requirement.txt           # DPO-specific dependencies
    ├── DPO_Training.ipynb        # 📚 Complete DPO tutorial notebook
    └── __pycache__/              # Python cache files (auto-generated)
```

## 🚀 Key Features

- **Complete SFT Pipeline**: End-to-end supervised fine-tuning implementation
- **Advanced DPO Training**: Reinforcement learning with human preference alignment
- **Interactive Web Interfaces**: Gradio-based chat interfaces for testing both models
- **Educational Focus**: Detailed notebooks explaining both SFT and DPO concepts
- **Customer Support Specialization**: Models fine-tuned specifically on customer support conversations
- **Model Comparison**: Side-by-side comparison of SFT vs DPO approaches

## 🛠️ Fine-Tuning Approaches

### Supervised Fine-Tuning (Plain-SFT/)
The project demonstrates a complete SFT workflow:

1. **Data Preparation**: Customer support conversation datasets
2. **Model Selection**: Base model selection and configuration  
3. **Training Pipeline**: Supervised fine-tuning implementation
4. **Evaluation**: Model performance assessment
5. **Deployment**: Web interface for interaction testing

### Direct Preference Optimization (RL-dpo/)
Advanced reinforcement learning approach:

1. **Preference Data Collection**: Human preference datasets
2. **DPO Training**: Direct preference optimization without traditional RL
3. **Policy Alignment**: Aligning model outputs with human preferences
4. **Comparative Evaluation**: Performance comparison with SFT baseline
5. **Advanced Deployment**: Enhanced interface for preference-aligned model

## 📖 Learning Resources

### SFT Tutorial: [`Plain-SFT/Supervised_FineTuning.ipynb`](Plain-SFT/Supervised_FineTuning.ipynb)

Comprehensive SFT notebook covering:
- SFT theory and fundamental concepts
- Step-by-step implementation guide
- Dataset preparation techniques
- Training loop and optimization strategies
- Model evaluation methods
- Best practices and troubleshooting tips

### DPO Tutorial: [`RL-dpo/DPO_Training.ipynb`](RL-dpo/DPO_Training.ipynb)

Advanced DPO notebook covering:
- Direct Preference Optimization theory
- Preference dataset preparation
- DPO training implementation
- Human preference alignment techniques
- Comparative analysis with SFT
- Advanced evaluation metrics

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

### For SFT Model:
3. **Install SFT dependencies**:
   ```bash
   cd Plain-SFT
   pip install -r requirement.txt
   ```

4. **Run the SFT application**:
   ```bash
   python app.py
   ```

### For DPO Model:
3. **Install DPO dependencies**:
   ```bash
   cd RL-dpo
   pip install -r requirement.txt
   ```

4. **Run the DPO application**:
   ```bash
   python app.py
   ```

## 📋 Key Files Description

### Supervised Fine-Tuning Files (Plain-SFT/)

#### [`Plain-SFT/app.py`](Plain-SFT/app.py)
- SFT model Gradio web interface
- Loads `BekiTila/bitext-sft-tinyllama-support` model
- Handles conversation history and response generation
- Provides interactive testing environment for SFT model

#### [`Plain-SFT/prompts.py`](Plain-SFT/prompts.py)
- Prompt templates for SFT model
- Conversation structure management
- SFT-specific prompt formatting

#### [`Plain-SFT/Supervised_FineTuning.ipynb`](Plain-SFT/Supervised_FineTuning.ipynb)
- **Core SFT educational content**
- Complete SFT tutorial and implementation
- Dataset preparation and preprocessing
- Model training and fine-tuning code
- Evaluation metrics and assessment

### Direct Preference Optimization Files (RL-dpo/)

#### [`RL-dpo/app.py`](RL-dpo/app.py)
- DPO model Gradio web interface  
- Loads `BekiTila/bitext-dpo-tinyllama-support` model
- Advanced conversation handling with preference alignment
- Interactive testing environment for DPO model

#### [`RL-dpo/prompts.py`](RL-dpo/prompts.py)
- Prompt templates optimized for DPO model
- Preference-aligned conversation structure
- DPO-specific prompt formatting

#### [`RL-dpo/DPO_Training.ipynb`](RL-dpo/DPO_Training.ipynb)
- **Core DPO educational content**
- Complete DPO tutorial and implementation
- Preference dataset preparation
- DPO training pipeline
- Human preference alignment techniques

## 🎓 Learning Objectives

This project teaches:
- **Supervised Fine-Tuning fundamentals** and best practices
- **Direct Preference Optimization** theory and implementation
- Dataset preparation for conversational AI
- Advanced training pipeline implementation
- Model evaluation and validation strategies
- Preference alignment techniques
- Comparative analysis of different fine-tuning approaches
- Deployment strategies for fine-tuned models

## 🚀 Usage

### Testing the SFT Model:
1. **Start the SFT application**: 
   ```bash
   cd Plain-SFT
   python app.py
   ```
2. **Access the interface**: Open your browser to `http://127.0.0.1:7860`

### Testing the DPO Model:
1. **Start the DPO application**: 
   ```bash
   cd RL-dpo
   python app.py
   ```
2. **Access the interface**: Open your browser to `http://127.0.0.1:7860`

### Learning:
- **Explore SFT**: Study [`Plain-SFT/Supervised_FineTuning.ipynb`](Plain-SFT/Supervised_FineTuning.ipynb)
- **Explore DPO**: Study [`RL-dpo/DPO_Training.ipynb`](RL-dpo/DPO_Training.ipynb)
- **Compare Models**: Test both interfaces to see the difference in responses

## 🎯 Model Details

### SFT Model (`Plain-SFT/`)
- **Base Model**: TinyLlama architecture
- **Fine-tuned Model**: `BekiTila/bitext-sft-tinyllama-support`
- **Training Method**: Supervised Fine-Tuning
- **Specialization**: Customer support conversations

### DPO Model (`RL-dpo/`)
- **Base Model**: SFT model as starting point
- **Fine-tuned Model**: `BekiTila/bitext-dpo-tinyllama-support`
- **Training Method**: Direct Preference Optimization
- **Specialization**: Human preference-aligned customer support

## 🔬 Comparison & Analysis

The project enables comparison between:
- **SFT approach**: Traditional supervised fine-tuning
- **DPO approach**: Preference-based reinforcement learning
- **Response quality**: Human preference alignment effectiveness
- **Training efficiency**: Computational requirements and training time

## 🤝 Contributing

This is an educational project focused on learning advanced fine-tuning techniques. Feel free to:
- Explore both SFT and DPO implementations
- Modify the code for your own datasets
- Experiment with different preference alignment techniques
- Extend functionality for other domains
- Share improvements and learnings

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**🎓 Educational Note**: This project is designed to teach both Supervised Fine-Tuning and Direct Preference Optimization concepts through hands-on implementation. The [`Plain-SFT/`](Plain-SFT/) directory focuses on traditional SFT techniques, while [`RL-dpo/`](RL-dpo/) demonstrates advanced preference alignment methods. Both directories contain comprehensive educational notebooks