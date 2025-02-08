import streamlit as st
from transformers import pipeline

# Load the Question-Answering pipeline
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Define a dictionary for common symptoms and their responses
def healthcare_chatbot(user_input):
    # Define specific answers based on common health queries
    symptom_responses = {
        "fever": (
            "For fever, you can take medications such as acetaminophen (Tylenol) or ibuprofen (Advil). "
            "Make sure to stay hydrated and rest. If the fever persists for more than a couple of days, "
            "consult a doctor."
        ),
        "sneezing": (
            "Sneezing might be caused by allergies, a cold, or irritants. "
            "You can use antihistamines like cetirizine or loratadine for allergies, "
            "or a nasal spray if you suspect allergies. For a cold, rest and fluids are recommended. "
            "Consult a doctor if the sneezing persists."
        ),
        "headache": (
            "For headaches, medications such as ibuprofen, acetaminophen, or aspirin can help relieve symptoms. "
            "You can also apply a cold or warm compress to your forehead or neck. If headaches are frequent, "
            "please consult a doctor."
        ),
        "cold": (
            "For a cold, staying hydrated and resting are important. You can use over-the-counter medications like decongestants, "
            "cough syrups, and antihistamines to alleviate symptoms. Make sure to get enough sleep, and if symptoms worsen, "
            "see a doctor."
        ),
        "stomach ache": (
            "Stomach aches can be caused by indigestion, gas, or even stress. Over-the-counter antacids like Tums or Pepto-Bismol "
            "may help. If the pain is severe or persistent, it’s important to consult a healthcare provider."
        ),
        "cough": (
            "For a cough, over-the-counter cough syrups, expectorants, and cough drops can help relieve symptoms. "
            "Staying hydrated and using honey in warm water might also soothe your throat. If the cough lasts longer than a few weeks, "
            "consult a doctor."
        ),
        "diabetes": (
            "For managing diabetes, it’s important to monitor your blood sugar levels regularly. Medications like metformin, "
            "insulin, or other prescribed drugs may be necessary. A balanced diet, regular exercise, and proper weight management "
            "are essential. Please consult a doctor for personalized advice."
        ),
        "high blood pressure": (
            "Managing high blood pressure involves medication such as ACE inhibitors, beta-blockers, or diuretics. "
            "Lifestyle changes such as reducing salt intake, exercising, and managing stress are important. Please consult a healthcare provider."
        ),
        "anxiety": (
            "For anxiety, cognitive behavioral therapy (CBT) and medications such as selective serotonin reuptake inhibitors (SSRIs) "
            "are commonly prescribed. Regular physical activity, meditation, and relaxation techniques can also help manage symptoms."
        ),
        "depression": (
            "For depression, counseling, psychotherapy, and medications like antidepressants (SSRIs, SNRIs) can help. "
            "It's also helpful to maintain social connections and practice self-care. Please consult a doctor for personalized treatment."
        ),
        "asthma": (
            "Asthma can be managed with inhalers, bronchodilators, and corticosteroids. It’s important to avoid asthma triggers, "
            "such as smoke or allergens. If symptoms worsen, consult a doctor for a tailored treatment plan."
        ),
        "arthritis": (
            "For arthritis, medications such as non-steroidal anti-inflammatory drugs (NSAIDs), disease-modifying anti-rheumatic drugs (DMARDs), "
            "and biologics can help manage symptoms. Regular exercise and physical therapy may also help improve joint mobility."
        ),
        "allergies": (
            "For allergies, antihistamines like loratadine or cetirizine can provide relief. Nasal sprays or decongestants may also be helpful. "
            "Avoiding allergens and using air purifiers in your home might reduce symptoms."
        ),
        "heart disease": (
            "For heart disease, lifestyle changes such as eating a heart-healthy diet, exercising regularly, and controlling stress are important. "
            "Medications like statins, beta-blockers, or aspirin may also be prescribed. Always consult a healthcare provider."
        ),
        "stroke": (
            "For stroke recovery, it's important to seek immediate medical attention at the onset of symptoms. Rehabilitation, including physical therapy, "
            "speech therapy, and occupational therapy, can be crucial for recovery. Medications like blood thinners may be used to prevent future strokes."
        ),
        "pneumonia": (
            "Pneumonia is typically treated with antibiotics or antiviral medications depending on the cause. Rest, fluids, and proper nutrition are important. "
            "Consult a doctor immediately if you suspect pneumonia."
        ),
        "migraine": (
            "Migraines are often treated with medications like triptans, NSAIDs, or preventive medications. It’s important to identify triggers such as stress, "
            "lack of sleep, or certain foods. Consider lifestyle changes like regular sleep patterns and reducing stress."
        ),
        "gastroenteritis": (
            "For gastroenteritis (stomach flu), staying hydrated is essential. Clear liquids, oral rehydration solutions, and a bland diet can help. "
            "Avoid dairy and high-fat foods. If symptoms are severe or last more than a few days, consult a doctor."
        ),
        "flu": (
            "For the flu, antiviral medications like oseltamivir (Tamiflu) may be prescribed, especially if taken early. Rest, hydration, and over-the-counter medications "
            "for fever and aches can provide relief. Get the flu vaccine annually for prevention."
        ),
        "COVID-19": (
            "For COVID-19, follow public health guidelines, including isolation and testing. If symptoms worsen, such as difficulty breathing, seek emergency medical help. "
            "Rest, hydration, and medications for fever may help alleviate mild symptoms."
        ),
    }

    # Check for specific symptoms and return tailored responses
    user_input_lower = user_input.lower()
    for symptom, response in symptom_responses.items():
        if symptom in user_input_lower:
            return response
    
    # General context for other questions
    context = (
        "This is a healthcare assistant chatbot designed to provide basic guidance on health-related queries. "
        "It is not a substitute for professional medical advice. Always consult a healthcare provider for serious concerns. "
        "For example, sneezing could be caused by allergies or a cold, and fever could indicate an infection. "
        "Please be sure to consult a doctor for accurate diagnosis and treatment."
    )

    # Fallback to the question-answering model for other queries
    try:
        response = qa_pipeline(question=user_input, context=context)
        return response['answer']
    except Exception:
        return "I'm sorry, I couldn't process your query. Please try again."

# Main function for Streamlit app
def main():
    st.title("Healthcare Assistant Chatbot")

    user_input = st.text_input("How can I assist you today?")

    if st.button("Submit"):
        if user_input:
            st.write("*User*: ", user_input)
            with st.spinner("Processing your query, please wait..."):
                response = healthcare_chatbot(user_input)
            st.write("*Healthcare Assistant*: ", response)
        else:
            st.write("Please enter a message to get a response.")

# Run the app
if _name_ == "_main_":
    main()