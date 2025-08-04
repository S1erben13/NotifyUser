# NotifyUser

**A system to send messages in many ways, with an extra way to be sure it gets there**

### Features

- **Multi-channel**: Email, SMS (MTS Exolve), Telegram
- **Fallback**: Automatically switches channels if primary fails
- **Modular**: Easy to add new providers

### Quick Start

1. Clone repo & install deps:
   ```bash  
   git clone https://github.com/yourusername/notification-system.git  
   cd notification-system  
   pip install -r requirements.txt  
   cp .env.example .env
2. Configure .env with your credentials
3. Run:

    ``` bash
    python main.py  

Config (.env)
    ``` ini

    # Telegram  
    TELEGRAM_BOT_TOKEN=your_token  
    TELEGRAM_USER_ID_TARGET=123  
    
    # Email  
    DOMAIN=smtp.yourprovider.com  
    LOGIN=your@email.com  
    PASSWORD="your_pass"  
    
    # SMS  
    PHONE_NUMBER_TARGET=+123456789  
    API_KEY=your_exolve_key  

### How It Works

1. Tries channels in order: Telegram → SMS → Email

2. If TEST=True, tests all channels

3. Logs results for each attempt

### Add New Notifier

1. Create notifiers/new_service.py following base template

2. Add to NOTIFIERS in main.py

#### Dependencies: Python 3.8+, aiogram (Telegram), python-dotenv
