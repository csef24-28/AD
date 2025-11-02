import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Count how many recognized words appear in the message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Percentage of recognized words
    percentage = float(message_certainty) / float(len(recognised_words))

    # Check for required words
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Return probability score
    if has_required_words or single_response:
        return int(percentage * 100)
    return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Shortcut to add responses
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(
            message, list_of_words, single_response, required_words
        )

    # Responses
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response("I'm doing fine, and you?", ['how', 'are', 'you', 'doing'], required_words=['how'])
    response("You're welcome!", ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])

    # Long responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    return check_all_messages(split_message)


# Chat loop
while True:
    print('Bot:', get_response(input('You: ')))