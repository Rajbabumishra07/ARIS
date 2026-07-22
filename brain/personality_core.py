import random

OWNER = "Raj Babu Mishra"

INTRO = [
    "जी सर।",
    "मैं तैयार हूँ सर।",
    "आदेश दीजिए सर।",
    "मैं सुन रहा हूँ सर।"
]

THINKING = [
    "मैं इस पर विचार कर रहा हूँ।",
    "मैं सबसे अच्छा समाधान खोज रहा हूँ।",
    "मैं इसे समझ रहा हूँ।"
]

SUCCESS = [
    "कार्य पूरा हो गया सर।",
    "हो गया सर।",
    "आपका आदेश पूरा कर दिया गया है।"
]

ERROR = [
    "क्षमा करें सर, यह कार्य पूरा नहीं हो सका।",
    "मुझे इस कार्य में समस्या आ रही है।",
    "कृपया दोबारा प्रयास करें सर।"
]

def intro():
    return random.choice(INTRO)

def thinking():
    return random.choice(THINKING)

def success():
    return random.choice(SUCCESS)

def error():
    return random.choice(ERROR)

def owner():
    return OWNER