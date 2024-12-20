import google.generativeai as genai

#This function take a script (.txt) and topic (string) and uses that to send a prompt to gemini to create flashcards. 
#The function has a default model, temperature, and max output tokens, which can be adjusted as needed
def generate_flashcards_twoparts(script, topic, model_name="gemini-1.5-pro", temperature=0.2, max_output_tokens=8000, revision_temperature=0.2):
    """
    Generates Anki flashcards from a podcast script using the Gemini API.

    Args:
        script: The text content of the podcast script.
        topic: The main topic of the podcast (used in the prompt).
        model_name: The name of the Gemini model to use (default: "gemini-1.5-pro").
        temperature: The temperature parameter for controlling creativity (default: 0.7).
        max_output_tokens: The maximum number of tokens in the response (default: 1000).
        revision_temperature: The temperature parameter for the flashcard revision step

    Returns:
        The generated flashcards as a string.
    """
    
    model = genai.GenerativeModel(model_name)
    prompt = f"""
    You are an expert Anki flashcard generator. Please create a set of detailed notes organized by the topic '{topic}' from the podcast script below:
    {script}. For each subtopic within '{topic}', create a set of cloze deletion flashcards.  
    
    Each flashcard should follow this exact format:
    Field 1: [Flashcard content]
    Field 2: [Notes content]
    Do not use any bolding or additional formatting.
    Please note, this is a medical podcast and as a result, the script may have spelling innaccuracies for medical terms.
    Good flashcards connect different concepts, explain mechanisms, and link basic science to clinical practice. 
    Notes section should include thorough explanation of the flashcard. 

    Example flashcards:
    (As you can see in the examples, the {{{{c#:cloze}}}} represents which number cloze it is in the flashcard.
    A flashcard can have multiple clozes where the clozes increase in number as they go, and can also have clozes with the same number if appropriately grouped):

    Field 1: IV anesthetic infusions often cause pain on injection due to vascular irritation from {{{{c1::propylene glycol}}}}, which is used to increase the {{{{c1::solubility}}}} of IV anesthetics in water.

    Field 2: Etomidate contains a carboxylated imidazole ring-containing anesthetic compound and is structurally unrelated to other anesthetic agents.
    The imidazole ring provides water solubility in acidic solutions and lipid solubility at physiological pH.
    Therefore, etomidate is dissolved in propylene glycol, which often causes pain on injection but can be reduced by prior intravenous injection of lidocaine.

    Field 1:
    In obstructive lung diseases, the FEV1 is {{{{c1::decreased}}}}, the FVC is {{{{c1::normal or slightly decreased}}}}, and the FEV1/FVC ratio is {{{{c2::decreased}}}}.

    Field 2:
    FEV1 = Forced expiratory volume in 1 second.
    FVC = Forced vital capacity.
    The decreased FEV1/FVC ratio is a key marker for obstructive lung disease.
    In obstructive diseases, you have a very hard time exhaling.
    FEV1 is very decreased because you can't get a lot of air out in one second.
    You get the initial flow that's relatively normal, just the air that's in the trachea and upper airways, but then immediately in less than a second, you have the very steep decrease in flow that's scooping out of the curve and that leads your FEV1 to be very reduced.
    Then you have an FVC that is relatively normal and so you have a small numerator and a relatively normal large denominator and that leads to a very decreased FEV1/FVC ratio.
    This same ratio for restrictive diseases is relatively unchanged or even increased

    """
    response = model.generate_content(
        prompt,
        generation_config={"temperature": temperature, "max_output_tokens": max_output_tokens},
    )
    initial_flashcards = response.text.strip()
    print('round one complete')

    # Revision prompt
    revision_prompt = f"""
    You are an expert Anki flashcard reviewer. You created these flashcards {initial_flashcards} based on this script {script}.
    Please review the script and flashcards, and create additional flashcards for any missed topics from the script. 
    Maintain the formatting of the original flashcards. Return a final set of flashcards that includes both the original flashcards and any new flashcards.
    """
    response = model.generate_content(
        revision_prompt,
        generation_config={"temperature": revision_temperature, "max_output_tokens": max_output_tokens},
    )
    revised_flashcards = response.text.strip()

    return revised_flashcards