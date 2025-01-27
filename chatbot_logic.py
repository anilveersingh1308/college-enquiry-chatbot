import sqlite3

responses = {
    "admissions": {
        "eligibility": "Eligibility: UG requires 50% in 12th; PG requires a bachelor's degree.",
        "process": "Apply online via our portal. Fill the form, upload documents, and pay the fee.",
        "dates": "Admissions start April 1 and close June 30.",
        "exams": "We accept JEE, CAT, and our entrance exam."
    },
    "programs": {
        "undergraduate": "Available programs: B.Tech, B.Sc, BCA, BA.",
        "postgraduate": "Available programs: M.Tech, M.Sc, MCA, MA.",
        "diploma": "Diplomas in Digital Marketing, Data Science, etc.",
        "research": "Research areas include Computer Science, Physics, Management."
    },
    "fees": {
        "structure": "Fees: UG starts at $10,000/year; PG starts at $15,000/year.",
        "payment": "Pay via Net Banking, Credit/Debit Card, or UPI.",
        "scholarships": "Merit-based and need-based scholarships available.",
        "refund": "Refunds allowed within 30 days with a 10% deduction."
    },
    "facilities": {
        "library": "Library has 50,000+ books and e-resources.",
        "hostel": "Separate hostels for boys and girls with modern amenities.",
        "sports": "Facilities for cricket, football, gym, and more.",
        "transport": "Bus services available across the city."
    },
    "placements": {
        "statistics": "95% placement rate. Avg package: $50,000/year.",
        "recruiters": "Top recruiters: Google, Amazon, Infosys.",
        "internships": "Internships offered with industry leaders.",
        "alumni": "Alumni include top industry professionals and entrepreneurs."
    },
    "contact": {
        "department": "Email: admissions@college.com; Phone: +123-456-7890.",
        "general": "Email: info@college.com; Phone: +123-456-0000.",
        "social": "Follow us on Facebook, Twitter, Instagram."
    },
    "default": "I'm sorry, I didn't understand. Can you rephrase your question?"
}

def get_response(user_message, greeted):
    user_message = user_message.lower()
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    
    # Handle common greetings
    greetings = ["hi", "hello", "hey", "greetings"]
    if any(greet in user_message for greet in greetings):
        return "Hello! How can I assist you today? You can ask me about admissions, programs, fees, facilities, placements, or contact information.", True
    
    # Define keywords and their corresponding responses
    keywords = {
        "admissions": ["eligibility", "process", "dates", "exams", "all"],
        "programs": ["undergraduate", "postgraduate", "diploma", "research", "all"],
        "fees": ["structure", "payment", "scholarships", "refund", "all"],
        "facilities": ["library", "hostel", "sports", "transport", "all"],
        "placements": ["statistics", "recruiters", "internships", "alumni", "all"],
        "contact": ["department", "general", "social", "all"],
    }
    
    # Split the user message into words
    words = user_message.split()
    
    # Try to find a response for each keyword in the user message
    for category, sub_keywords in keywords.items():
        if category in user_message:
            responses = []
            for sub_keyword in sub_keywords:
                cursor.execute("SELECT response FROM responses WHERE keyword LIKE ?", (f"%{category} {sub_keyword}%",))
                result = cursor.fetchone()
                if result and result[0] not in responses:
                    responses.append(result[0])
            if responses:
                conn.close()
                return "\n".join(responses), greeted
            # If no subcategory is specified, return all data in the category
            for sub_keyword in sub_keywords:
                cursor.execute("SELECT response FROM responses WHERE keyword LIKE ?", (f"%{category} {sub_keyword}%",))
                result = cursor.fetchone()
                if result and result[0] not in responses:
                    responses.append(result[0])
            if responses:
                conn.close()
                return "\n".join(responses), greeted
    
    # Try to find a response for each word in the user message
    responses = []
    for word in words:
        cursor.execute("SELECT response FROM responses WHERE keyword LIKE ?", (f"%{word}%",))
        result = cursor.fetchone()
        if result and result[0] not in responses:
            responses.append(result[0])
    if responses:
        conn.close()
        return "\n".join(responses), greeted
    
    # If no response is found, return the default response
    conn.close()
    return "I'm sorry, I didn't understand. Can you rephrase your question? You can ask me about admissions, programs, fees, facilities, placements, or contact information.", greeted
