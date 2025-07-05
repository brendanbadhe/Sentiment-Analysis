""" Executing this function initiates the application of sentiment
    analysis to be executed over the IBM Watson SDK and deployed on
    IBM Cloud.
"""

from ibm_cloud_sdk_core.api_exception import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import NaturalLanguageUnderstandingV1


def sentiment_analyzer(text_to_analyze):
    """This code receives the text from the flask server and
    runs sentiment analysis over it. The output returned shows the label and its confidence
    score for the provided text.
    """
    try:
        # Details for IBM Watson NLU instance
        api_key = "API_KEY"
        url = (
            "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/"
            "instances/INSTANCE"
        )

        authenticator = IAMAuthenticator(api_key)
        nlu = NaturalLanguageUnderstandingV1(
            version="2022-08-10", authenticator=authenticator
        )
        nlu.set_service_url(url)

        response = nlu.analyze(
            text=text_to_analyze, features={"sentiment": {}}
        ).get_result()

        return response["sentiment"]["document"]

    except ApiException:
        return {"label": None, "score": None}
