import stanza
from collections import Counter

def summarize_text(text):
    return text

marathi_stopwords = {
    "आणि", "में", "हो", "की", "ते", "आपण", "सर्व", "काही", "तेव्हा", "पण",
    "असे", "मध्ये", "जरी", "म्हणजे", "ही", "त्याला", "त्यांच्या", "यांच्या",
    "वर", "साठी", "आहे", "तरी", "चांगले", "फक्त", "सुद्धा", "अधिक", "दुसरे",
    "तुम्ही", "किंवा", "तिथे", "कधी", "काय", "नंतर", "आधी", "जास्त",
    "तुम्ही", "एक", "कशासाठी", "कस", "तिथे", "त्यामुळे", "खूप", "किंवा", "संपूर्ण",
    "खाली", "वरील", "म्हणजेच", "तिला", "आणखी", "शक्य", "दृश्य", "दुसऱ्या", "चुक",
    "यांना", "यांनी", "या", "त्यामुळे", "होते", "होंते", "नाही", "होता", "होती",
    "होतं", "आहेत", "आला", "झाला", "झाली", "आल्या", "झाले", "त्यांना", "त्याचा",
    "ल्या", "माझा", "माझ्या", "आपल्या", "आपला", "आमचा", "आमच्या", "तुमचा", "तुमच्या",
    "त्यांनी", "त्या", "यांनी", "याचा", "यांनी", "दुसरा", "पहिला", "मग", "म्हणून",
    "कुणी", "कोण", "कुठे", "कसा", "किती", "तिथेच", "तिथल्या", "तसाच", "तेच",
    "तिथून", "पुन्हा", "हेच", "जेव्हा", "जिथे", "कोणत्याही", "म्हणजेच", "जे", "तर",
    "मात्र", "होणार", "होतात", "अजून", "पुढे", "कायम", "जास्त", "थोडं", "तेवढं",
    "त्याच", "तेवढाच", "त्यात", "यामुळे", "म्हणजे", "तुमचं", "त्याचं", "यांचं",
    "हवं", "हवी", "कधीही", "कुठल्याही", "सारखं", "काहीतरी", "कुठेही", "कधीच"
}


# Stanza pipeline for Marathi
stanza.download("mr")
nlp = stanza.Pipeline("mr", use_gpu=True)

def extract_keywords(text):
    # Removing unwanted characters
    cleaned_text = text.replace("\x00", "").strip()

    # Run Stanza NLP pipeline on the text
    doc = nlp(cleaned_text)

    # Extract tokens along with their POS tags
    relevant_keywords = []
    for sentence in doc.sentences:
        for word in sentence.words:
            # This includes nouns, proper nouns, and adjectives, ignoring stopwords
            if word.upos in {"NOUN", "PROPN", "ADJ"} and word.text not in marathi_stopwords:
                relevant_keywords.append(word.text)


    freq = Counter(relevant_keywords)
    top_keywords = [word for word, _ in freq.most_common(10)]

    return top_keywords




