import sqlite3

responses = {
    "admissions eligibility": "Eligibility: For undergraduate programs, a minimum of 50% in 12th grade is required. For postgraduate programs, a bachelor's degree is mandatory.",
    "admissions process": "The admission process involves applying online through our portal. You need to fill out the application form, upload the necessary documents, and pay the application fee.",
    "admissions dates": "Admissions commence on April 1st and close on June 30th.",
    "admissions exams": "We accept scores from JEE, CAT, and our own entrance examination.",
    "programs undergraduate": "Available undergraduate programs include B.Tech, B.Sc, BCA, and BA.",
    "programs postgraduate": "Available postgraduate programs include M.Tech, M.Sc, MCA, and MA.",
    "programs diploma": "We offer diplomas in Digital Marketing, Data Science, and other fields.",
    "programs research": "Research areas include Computer Science, Physics, and Management.",
    "fees structure": "The fee structure is as follows: Undergraduate programs start at $10,000 per year, and postgraduate programs start at $15,000 per year.",
    "fees payment": "Payments can be made via Net Banking, Credit/Debit Card, or UPI.",
    "fees scholarships": "We offer merit-based and need-based scholarships.",
    "fees refund": "Refunds are allowed within 30 days with a 10% deduction.",
    "facilities library": "Our library houses over 50,000 books and e-resources.",
    "facilities hostel": "We have separate hostels for boys and girls, equipped with modern amenities.",
    "facilities sports": "We offer facilities for cricket, football, a gym, and more.",
    "facilities transport": "Bus services are available across the city.",
    "placements statistics": "We have a 95% placement rate, with an average package of $50,000 per year.",
    "placements recruiters": "Top recruiters include Google, Amazon, and Infosys.",
    "placements internships": "We offer internships with industry leaders.",
    "placements alumni": "Our alumni include top industry professionals and successful entrepreneurs.",
    "contact department": "For departmental inquiries, email admissions@college.com or call +123-456-7890.",
    "contact general": "For general inquiries, email info@college.com or call +123-456-0000.",
    "contact social": "Follow us on Facebook, Twitter, and Instagram.",
    "greetings": "Hello! How can I assist you today? You can ask me about admissions, programs, fees, facilities, placements, or contact information."
}

def populate_db():
    conn = sqlite3.connect('chatbot.db')
    cursor = conn.cursor()
    for key, value in responses.items():
        cursor.execute("INSERT INTO responses (keyword, response) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    populate_db()
